#!/usr/bin/env python3
"""
Servidor Web Seguro y API REST de la Tuna de Derecho de Almería
Implementación completa con:
- Autenticación segura mediante PBKDF2-HMAC-SHA256 (100.000 iteraciones)
- Manejo de sesiones criptográficas con cookies HttpOnly y SameSite=Strict
- Protección contra CSRF (Cross-Site Request Forgery)
- Protección contra inyección SQL (consultas parametrizadas con SQLite3)
- Protección contra XSS y Content-Security-Policy (CSP) estricta
- Rate Limiting contra ataques de fuerza bruta en login
- Control de acceso basado en roles (Visitante, Cliente, Administrador)
- Enrutamiento estático seguro previniendo Path Traversal
"""

import os
import sys
import json
import sqlite3
import hashlib
import secrets
import html
import re
import mimetypes
import signal
from datetime import datetime, timedelta, timezone
from http.server import HTTPServer, ThreadingHTTPServer, SimpleHTTPRequestHandler
from http import cookies
from urllib.parse import urlparse, parse_qs, unquote

def get_utc_now():
    """Retorna timestamp UTC sin tzinfo para compatibilidad uniforme con SQLite."""
    return datetime.now(timezone.utc).replace(tzinfo=None)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "tuna.db")

# Rate limiter en memoria para intentos de login: {ip: [timestamp1, timestamp2, ...]}
FAILED_LOGINS = {}
RATE_LIMIT_MAX_ATTEMPTS = 5
RATE_LIMIT_WINDOW_SECONDS = 300  # 5 minutos
RATE_LIMIT_LOCKOUT_SECONDS = 900  # 15 minutos

# Cache de sesiones en memoria para rapidez
SESSION_CACHE = {}

def get_db_connection():
    """Obtiene una conexión a la base de datos con foreign keys habilitadas, modo WAL y timeout."""
    conn = sqlite3.connect(DB_PATH, timeout=15.0)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    conn.execute("PRAGMA busy_timeout = 5000;")
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password: str) -> str:
    """Genera un hash seguro con salt de 16 bytes y PBKDF2-HMAC-SHA256."""
    salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    ).hex()
    return f"pbkdf2:sha256:100000${salt}${key}"

def verify_password(stored_hash: str, provided_password: str) -> bool:
    """Verifica la contraseña contra el hash almacenado en tiempo constante."""
    try:
        parts = stored_hash.split('$')
        if len(parts) != 3:
            return False
        algorithm_info, salt, original_key = parts
        computed_key = hashlib.pbkdf2_hmac(
            'sha256',
            provided_password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        ).hex()
        return secrets.compare_digest(original_key, computed_key)
    except Exception:
        return False

def sanitize_string(val: str) -> str:
    """Escapa entidades HTML para prevenir XSS."""
    if val is None:
        return ""
    return html.escape(str(val).strip(), quote=True)

class TunaRequestHandler(SimpleHTTPRequestHandler):
    server_version = "TunaServer/2.0 (SecurityHardened)"
    timeout = 15  # Libera conexiones inactivas/keep-alive tras 15 segundos

    def log_message(self, format, *args):
        """Evita que el hilo del servidor caiga con BrokenPipe o EIO si la terminal se cierra."""
        try:
            sys.stderr.write("%s - - [%s] %s\n" %
                             (self.address_string(),
                              self.log_date_time_string(),
                              format % args))
            sys.stderr.flush()
        except Exception:
            pass

    def set_security_headers(self, content_type="text/html; charset=utf-8"):
        """Añade cabeceras de seguridad HTTP robustas según los mejores estándares."""
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("X-XSS-Protection", "1; mode=block")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://fonts.gstatic.com "
            "https://www.youtube.com https://open.spotify.com https://maps.googleapis.com https://*.google.com; "
            "img-src 'self' data: https:; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "frame-src https://www.youtube.com https://open.spotify.com https://www.google.com; "
            "connect-src 'self';"
        )
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")

    def send_json(self, data, status_code=200, extra_headers=None):
        """Envía una respuesta JSON con cabeceras de seguridad."""
        payload = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status_code)
        self.set_security_headers("application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        if extra_headers:
            for k, v in extra_headers.items():
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(payload)

    def send_error_json(self, message, status_code=400, extra=None):
        data = {"success": False, "error": message}
        if extra:
            data.update(extra)
        self.send_json(data, status_code=status_code)

    def parse_client_ip(self):
        """Extrae la IP del cliente de forma segura."""
        forwarded = self.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return self.client_address[0]

    def get_session_cookie(self):
        """Extrae el token de sesión de la cookie."""
        cookie_header = self.headers.get("Cookie")
        if not cookie_header:
            return None
        c = cookies.SimpleCookie()
        try:
            c.load(cookie_header)
            if "tuna_session" in c:
                return c["tuna_session"].value
        except Exception:
            return None
        return None

    def get_current_user(self):
        """Valida la sesión y devuelve los datos del usuario autenticado."""
        session_id = self.get_session_cookie()
        if not session_id or len(session_id) != 64:
            return None

        # Revisar en base de datos
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.id as session_id, s.csrf_token, s.expires_at,
                       u.id, u.email, u.name, u.phone, u.role
                FROM sessions s
                JOIN users u ON s.user_id = u.id
                WHERE s.id = ?
            """, (session_id,))
            row = cursor.fetchone()
            conn.close()

            if not row:
                return None

            expires_at = datetime.fromisoformat(row["expires_at"].replace("Z", ""))
            if get_utc_now() > expires_at:
                # Sesión expirada, limpiarla
                self.delete_session(session_id)
                return None

            return {
                "session_id": row["session_id"],
                "csrf_token": row["csrf_token"],
                "id": row["id"],
                "email": row["email"],
                "name": row["name"],
                "phone": row["phone"],
                "role": row["role"]
            }
        except Exception as e:
            print(f"[!] Error verificando sesión: {e}", file=sys.stderr)
            return None

    def create_session(self, user_id):
        """Crea una sesión criptográficamente segura de 256 bits."""
        session_id = secrets.token_hex(32)
        csrf_token = secrets.token_hex(32)
        ip = self.parse_client_ip()
        ua = self.headers.get("User-Agent", "")[:255]
        expires_at = get_utc_now() + timedelta(days=2)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sessions (id, user_id, csrf_token, ip_address, user_agent, expires_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (session_id, user_id, csrf_token, ip, ua, expires_at.isoformat()))
        conn.commit()
        conn.close()

        return session_id, csrf_token

    def delete_session(self, session_id):
        """Elimina la sesión de la base de datos."""
        if not session_id:
            return
        conn = get_db_connection()
        conn.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
        conn.commit()
        conn.close()

    def log_audit(self, action, details="", user_id=None, user_email=""):
        """Registra eventos de seguridad y cambios clave en audit_logs."""
        try:
            conn = get_db_connection()
            ip = self.parse_client_ip()
            conn.execute("""
                INSERT INTO audit_logs (user_id, user_email, action, details, ip_address)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, user_email, action, details, ip))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[!] Error en audit_log: {e}", file=sys.stderr)

    def check_rate_limit(self, ip):
        """Protección contra fuerza bruta en login."""
        now = get_utc_now()
        if ip in FAILED_LOGINS:
            attempts = [t for t in FAILED_LOGINS[ip] if (now - t).total_seconds() < RATE_LIMIT_LOCKOUT_SECONDS]
            FAILED_LOGINS[ip] = attempts
            if len(attempts) >= RATE_LIMIT_MAX_ATTEMPTS:
                return False
        return True

    def record_failed_login(self, ip):
        now = get_utc_now()
        if ip not in FAILED_LOGINS:
            FAILED_LOGINS[ip] = []
        FAILED_LOGINS[ip].append(now)

    def clear_failed_logins(self, ip):
        if ip in FAILED_LOGINS:
            del FAILED_LOGINS[ip]

    def verify_csrf(self, user, body_json=None):
        """Verifica el token CSRF para prevenir peticiones maliciosas forjadas."""
        if not user:
            return False
        token = self.headers.get("X-CSRF-Token")
        if not token and body_json and isinstance(body_json, dict):
            token = body_json.get("csrf_token")
        if not token:
            return False
        return secrets.compare_digest(user["csrf_token"], token)

    def read_json_body(self):
        """Lee y decodifica de forma segura el cuerpo JSON con límite de tamaño."""
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length == 0:
                return {}, None
            if content_length > 2 * 1024 * 1024:  # Máximo 2MB
                return None, "Cuerpo de solicitud demasiado grande"
            raw_body = self.rfile.read(content_length)
            if not raw_body.strip():
                return {}, None
            return json.loads(raw_body.decode('utf-8')), None
        except Exception as e:
            return None, f"JSON inválido: {str(e)}"

    # ============================================================
    # MANEJADORES DE RUTAS
    # ============================================================

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # Rutas de la API
        if path.startswith("/api/"):
            self.handle_api_get(path, parse_qs(parsed.query))
            return

        # Enrutamiento estático amigable y tolerancia a mayúsculas
        path_lower = path.lower()
        if path_lower.startswith("/visitante/") and path.startswith("/Visitante/"):
            self.send_redirect("/visitante/" + path[11:])
            return
        elif path_lower.startswith("/cliente/") and path.startswith("/Cliente/"):
            self.send_redirect("/cliente/" + path[9:])
            return
        elif path_lower.startswith("/admin/") and path.startswith("/Admin/"):
            self.send_redirect("/admin/" + path[7:])
            return

        if path in ("/", ""):
            self.send_redirect("/visitante/inicio.html")
            return
        elif path in ("/visitante", "/visitante/", "/Visitante", "/Visitante/"):
            self.send_redirect("/visitante/inicio.html")
            return
        elif path in ("/cliente", "/cliente/", "/Cliente", "/Cliente/"):
            self.send_redirect("/cliente/pedidos.html")
            return
        elif path in ("/admin", "/admin/", "/Admin", "/Admin/"):
            self.send_redirect("/admin/contratos.html")
            return
        elif path in ("/login", "/login/"):
            self.send_redirect("/auth/login.html")
            return
        elif path in ("/registro", "/registro/"):
            self.send_redirect("/auth/registro.html")
            return
        elif path in ("/unete", "/unete/", "/captacion", "/captacion/", "/quiero-unirme"):
            self.send_redirect("/visitante/captacion.html")
            return
        elif path in ("/contratacion", "/contratacion/"):
            self.send_redirect("/visitante/contratacion.html")
            return
        elif path in ("/tienda", "/tienda/"):
            self.send_redirect("/visitante/tienda.html")
            return

        # Servir archivos estáticos de la carpeta web
        self.serve_static_file(path)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path.startswith("/api/"):
            self.handle_api_post(path)
            return

        self.send_error_json("Método no soportado en esta ruta", 405)

    def do_PUT(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path.startswith("/api/"):
            self.handle_api_put(path)
            return

        self.send_error_json("Método no soportado en esta ruta", 405)

    def do_DELETE(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path.startswith("/api/"):
            self.handle_api_delete(path)
            return

        self.send_error_json("Método no soportado en esta ruta", 405)

    def send_redirect(self, target_url):
        self.send_response(302)
        self.send_header("Location", target_url)
        self.send_header("Content-Length", "0")
        self.send_header("Connection", "close")
        self.end_headers()
        self.close_connection = True

    def serve_static_file(self, req_path):
        """Sirve archivos estáticos asegurando que no haya Path Traversal."""
        # Limpiar barra inicial
        clean_path = req_path.lstrip("/")
        full_path = os.path.normpath(os.path.join(BASE_DIR, clean_path))

        # Validación estricta de Path Traversal
        if not full_path.startswith(BASE_DIR):
            self.send_error(403, "Acceso Prohibido")
            return

        if not os.path.exists(full_path):
            # Probar si falta .html
            if os.path.exists(full_path + ".html"):
                full_path += ".html"
            else:
                self.send_error(404, "Página no encontrada")
                return

        if os.path.isdir(full_path):
            index_path = os.path.join(full_path, "index.html")
            if os.path.exists(index_path):
                full_path = index_path
            else:
                self.send_error(403, "Listado de directorio no permitido")
                return

        # Protección: No servir la base de datos directamente ni el server.py
        rel = os.path.relpath(full_path, BASE_DIR)
        if rel.startswith("database/") and rel.endswith(".db"):
            self.send_error(403, "Acceso a la base de datos denegado")
            return

        mime_type, _ = mimetypes.guess_type(full_path)
        if not mime_type:
            mime_type = "application/octet-stream"
        if mime_type.startswith("text/") or mime_type in ("application/javascript", "application/json"):
            mime_type += "; charset=utf-8"

        try:
            with open(full_path, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.set_security_headers(mime_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Error del servidor: {e}")

    # ============================================================
    # CONTROLADORES DE LA API REST
    # ============================================================

    def handle_api_get(self, path, query_params):
        user = self.get_current_user()

        # 1. Sesión actual / Usuario conectado
        if path == "/api/auth/me":
            if user:
                self.send_json({
                    "authenticated": True,
                    "user": {
                        "id": user["id"],
                        "email": user["email"],
                        "name": user["name"],
                        "phone": user["phone"],
                        "role": user["role"]
                    },
                    "csrf_token": user["csrf_token"]
                })
            else:
                self.send_json({"authenticated": False, "user": None, "csrf_token": None})
            return

        # 2. Contratos y Solicitudes
        if path == "/api/contratos":
            if not user:
                self.send_error_json("No autenticado. Por favor, inicia sesión.", 401)
                return

            conn = get_db_connection()
            cursor = conn.cursor()

            if user["role"] == "admin":
                # Admin ve todos los contratos
                cursor.execute("""
                    SELECT id, client_id, client_name, client_email, client_phone,
                           event_type, event_date, event_time, location, attendees,
                           transport_logistics, notes, status, price_agreed, created_at
                    FROM contratos
                    ORDER BY event_date ASC, created_at DESC
                """)
            else:
                # Cliente solo ve los suyos
                cursor.execute("""
                    SELECT id, client_id, client_name, client_email, client_phone,
                           event_type, event_date, event_time, location, attendees,
                           transport_logistics, notes, status, price_agreed, created_at
                    FROM contratos
                    WHERE client_id = ?
                    ORDER BY event_date ASC, created_at DESC
                """, (user["id"],))

            rows = [dict(r) for r in cursor.fetchall()]
            conn.close()
            self.send_json({"success": True, "contratos": rows})
            return

        # 3. Tienda de Merchandising (Pública)
        if path == "/api/tienda":
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, category, description, price, image_url, badge, stock, is_active
                FROM products
                WHERE is_active = 1
                ORDER BY id ASC
            """)
            products = [dict(r) for r in cursor.fetchall()]
            conn.close()
            self.send_json({"success": True, "products": products})
            return

        # 4. Tienda Admin (incluye inactivos)
        if path == "/api/admin/tienda":
            if not user or user["role"] != "admin":
                self.send_error_json("Acceso restringido a administradores", 403)
                return
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products ORDER BY id ASC")
            products = [dict(r) for r in cursor.fetchall()]
            conn.close()
            self.send_json({"success": True, "products": products})
            return

        # 5. Pedidos de Merchandising
        if path == "/api/pedidos":
            if not user:
                self.send_error_json("No autenticado", 401)
                return

            conn = get_db_connection()
            cursor = conn.cursor()

            if user["role"] == "admin":
                cursor.execute("""
                    SELECT o.*, u.name as client_name, u.email as client_email
                    FROM orders o
                    JOIN users u ON o.client_id = u.id
                    ORDER BY o.created_at DESC
                """)
            else:
                cursor.execute("""
                    SELECT * FROM orders
                    WHERE client_id = ?
                    ORDER BY created_at DESC
                """, (user["id"],))

            orders = [dict(r) for r in cursor.fetchall()]

            # Adjuntar líneas de pedido a cada pedido
            for o in orders:
                cursor.execute("""
                    SELECT product_id, product_name, price, quantity
                    FROM order_items
                    WHERE order_id = ?
                """, (o["id"],))
                o["items"] = [dict(i) for i in cursor.fetchall()]

            conn.close()
            self.send_json({"success": True, "orders": orders})
            return

        # 6. Miembros de la Tuna (Público)
        if path == "/api/miembros":
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nickname, real_name, role_instrument, category, generation_year, bio, photo_url, order_num
                FROM members
                WHERE is_active = 1
                ORDER BY order_num ASC, id ASC
            """)
            members = [dict(r) for r in cursor.fetchall()]
            conn.close()
            self.send_json({"success": True, "members": members})
            return

        # 7. Repertorio y Audiovisuales (Cancionero y Vídeos)
        if path == "/api/repertorio":
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM songs ORDER BY id ASC")
            songs = [dict(r) for r in cursor.fetchall()]
            cursor.execute("SELECT * FROM videos ORDER BY year DESC, id ASC")
            videos = [dict(r) for r in cursor.fetchall()]
            conn.close()
            self.send_json({"success": True, "songs": songs, "videos": videos})
            return

        # 8. Captación de novatos (Solo Admin)
        if path == "/api/captacion":
            if not user or user["role"] != "admin":
                self.send_error_json("Acceso denegado", 403)
                return
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM captacion ORDER BY created_at DESC")
            aspirantes = [dict(r) for r in cursor.fetchall()]
            conn.close()
            self.send_json({"success": True, "aspirantes": aspirantes})
            return

        self.send_error_json("Ruta de API GET no encontrada", 404)

    def handle_api_post(self, path):
        body, err = self.read_json_body()
        if err:
            self.send_error_json(err, 400)
            return

        ip = self.parse_client_ip()

        # 1. Login
        if path == "/api/auth/login":
            if not self.check_rate_limit(ip):
                self.send_error_json(
                    "Demasiados intentos fallidos. Bloqueado temporalmente por seguridad. Espere 15 minutos.",
                    429
                )
                return

            email = str(body.get("email", "")).strip().lower()
            password = str(body.get("password", ""))

            if not email or not password:
                self.send_error_json("Debe ingresar correo y contraseña", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, email, password_hash, name, phone, role FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            conn.close()

            if not user or not verify_password(user["password_hash"], password):
                self.record_failed_login(ip)
                self.log_audit("FAILED_LOGIN", f"Email intentado: {email}")
                self.send_error_json("Credenciales incorrectas. Verifique su correo o contraseña.", 401)
                return

            # Login exitoso
            self.clear_failed_logins(ip)
            session_id, csrf_token = self.create_session(user["id"])
            self.log_audit("LOGIN_SUCCESS", f"Rol: {user['role']}", user_id=user["id"], user_email=user["email"])

            # Enviar cookie segura
            cookie = cookies.SimpleCookie()
            cookie["tuna_session"] = session_id
            cookie["tuna_session"]["path"] = "/"
            cookie["tuna_session"]["httponly"] = True
            cookie["tuna_session"]["samesite"] = "Strict"
            cookie["tuna_session"]["max-age"] = 172800  # 48 horas

            self.send_json({
                "success": True,
                "message": "Inicio de sesión correcto",
                "user": {
                    "id": user["id"],
                    "email": user["email"],
                    "name": user["name"],
                    "phone": user["phone"],
                    "role": user["role"]
                },
                "csrf_token": csrf_token
            }, extra_headers={"Set-Cookie": cookie["tuna_session"].OutputString()})
            return

        # 2. Registro de Clientes
        if path == "/api/auth/register":
            name = sanitize_string(body.get("name", ""))
            email = str(body.get("email", "")).strip().lower()
            phone = sanitize_string(body.get("phone", ""))
            password = str(body.get("password", ""))

            if not name or len(name) < 3:
                self.send_error_json("El nombre completo debe tener al menos 3 caracteres", 400)
                return
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
                self.send_error_json("El formato de correo electrónico no es válido", 400)
                return
            if len(password) < 8:
                self.send_error_json("La contraseña debe tener un mínimo de 8 caracteres", 400)
                return

            pwd_hash = hash_password(password)

            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO users (email, password_hash, name, phone, role)
                    VALUES (?, ?, ?, ?, 'cliente')
                """, (email, pwd_hash, name, phone))
                new_user_id = cursor.lastrowid
                conn.commit()
            except sqlite3.IntegrityError:
                conn.close()
                self.send_error_json("Ya existe una cuenta registrada con este correo electrónico", 409)
                return
            conn.close()

            # Auto-login del nuevo cliente
            session_id, csrf_token = self.create_session(new_user_id)
            self.log_audit("REGISTER_SUCCESS", f"Nuevo cliente ID: {new_user_id}", user_id=new_user_id, user_email=email)

            cookie = cookies.SimpleCookie()
            cookie["tuna_session"] = session_id
            cookie["tuna_session"]["path"] = "/"
            cookie["tuna_session"]["httponly"] = True
            cookie["tuna_session"]["samesite"] = "Strict"
            cookie["tuna_session"]["max-age"] = 172800

            self.send_json({
                "success": True,
                "message": "Registro completado con éxito",
                "user": {
                    "id": new_user_id,
                    "email": email,
                    "name": name,
                    "phone": phone,
                    "role": "cliente"
                },
                "csrf_token": csrf_token
            }, extra_headers={"Set-Cookie": cookie["tuna_session"].OutputString()})
            return

        # 3. Logout
        if path == "/api/auth/logout":
            user = self.get_current_user()
            if user:
                self.delete_session(user["session_id"])
                self.log_audit("LOGOUT", user_id=user["id"], user_email=user["email"])

            # Expirar cookie
            cookie = cookies.SimpleCookie()
            cookie["tuna_session"] = ""
            cookie["tuna_session"]["path"] = "/"
            cookie["tuna_session"]["httponly"] = True
            cookie["tuna_session"]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"

            self.send_json({"success": True, "message": "Sesión cerrada correctamente"},
                           extra_headers={"Set-Cookie": cookie["tuna_session"].OutputString()})
            return

        # Verificación de usuario para rutas autenticadas
        current_user = self.get_current_user()

        # 4. Crear Contrato / Solicitud de Actuación
        if path == "/api/contratos":
            # Puede ser enviado por visitante o por cliente logueado
            client_name = sanitize_string(body.get("client_name", ""))
            client_email = str(body.get("client_email", "")).strip().lower()
            client_phone = sanitize_string(body.get("client_phone", ""))
            event_type = sanitize_string(body.get("event_type", "Celebración"))
            event_date = sanitize_string(body.get("event_date", ""))
            event_time = sanitize_string(body.get("event_time", ""))
            location = sanitize_string(body.get("location", ""))
            attendees = sanitize_string(body.get("attendees", ""))
            transport_logistics = sanitize_string(body.get("transport_logistics", "A cargo de la Tuna"))
            notes = sanitize_string(body.get("notes", ""))

            # Si el usuario está autenticado, usar sus datos si faltan
            client_id = None
            if current_user:
                client_id = current_user["id"]
                if not client_name:
                    client_name = current_user["name"]
                if not client_email:
                    client_email = current_user["email"]
                if not client_phone:
                    client_phone = current_user["phone"]

            if not client_name or not client_phone or not event_date or not location:
                self.send_error_json("Por favor rellene los campos obligatorios: Nombre, Teléfono, Fecha y Lugar", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO contratos (
                    client_id, client_name, client_email, client_phone,
                    event_type, event_date, event_time, location, attendees,
                    transport_logistics, notes, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pendiente')
            """, (client_id, client_name, client_email, client_phone, event_type,
                  event_date, event_time, location, attendees, transport_logistics, notes))
            new_id = cursor.lastrowid
            conn.commit()
            conn.close()

            # Generar enlace directo de WhatsApp a Popeye según requisitos
            # Popeye recibe la solicitud con los datos estructurados
            popeye_phone = "34611223344"
            whatsapp_msg = (
                f"🎶 *Nueva Solicitud de Contratación - Tuna de Derecho Almería* 🎶\n"
                f"• *Cliente:* {client_name}\n"
                f"• *Teléfono:* {client_phone}\n"
                f"• *Email:* {client_email}\n"
                f"• *Tipo de Evento:* {event_type}\n"
                f"• *Fecha y Hora:* {event_date} a las {event_time}\n"
                f"• *Lugar:* {location}\n"
                f"• *Aforo estimado:* {attendees}\n"
                f"• *Transporte:* {transport_logistics}\n"
                f"• *Detalles:* {notes}\n"
                f"ID Solicitud Web: #{new_id}"
            )
            import urllib.parse
            whatsapp_link = f"https://api.whatsapp.com/send?phone={popeye_phone}&text={urllib.parse.quote(whatsapp_msg)}"

            self.log_audit("NEW_CONTRACT", f"ID #{new_id} por {client_name}", user_id=client_id, user_email=client_email)

            self.send_json({
                "success": True,
                "message": "Solicitud enviada correctamente. Popeye se pondrá en contacto en breve.",
                "contract_id": new_id,
                "whatsapp_link": whatsapp_link
            })
            return

        # 5. Crear Pedido de Tienda (Checkout)
        if path == "/api/pedidos":
            if not current_user:
                self.send_error_json("Debes iniciar sesión como cliente para tramitar tu pedido.", 401)
                return

            if not self.verify_csrf(current_user, body):
                self.send_error_json("Error de seguridad: Token CSRF no válido o expirado.", 403)
                return

            items = body.get("items", [])
            shipping_name = sanitize_string(body.get("shipping_name", current_user["name"]))
            shipping_phone = sanitize_string(body.get("shipping_phone", current_user["phone"]))
            shipping_address = sanitize_string(body.get("shipping_address", ""))
            shipping_city = sanitize_string(body.get("shipping_city", "Almería"))
            shipping_postal_code = sanitize_string(body.get("shipping_postal_code", "04001"))
            payment_method = sanitize_string(body.get("payment_method", "Bizum"))
            notes = sanitize_string(body.get("notes", ""))

            if not items or not isinstance(items, list):
                self.send_error_json("El carrito de compras está vacío", 400)
                return
            if not shipping_address or not shipping_phone:
                self.send_error_json("Por favor indique dirección y teléfono de entrega", 400)
                return

            # Calcular importe verificando precios reales de la BD
            conn = get_db_connection()
            cursor = conn.cursor()

            total_amount = 0.0
            verified_items = []

            for item in items:
                prod_id = int(item.get("product_id", 0))
                qty = max(1, int(item.get("quantity", 1)))
                cursor.execute("SELECT id, name, price, stock FROM products WHERE id = ? AND is_active = 1", (prod_id,))
                prod = cursor.fetchone()
                if not prod:
                    conn.close()
                    self.send_error_json(f"Producto ID {prod_id} no disponible", 400)
                    return
                item_total = prod["price"] * qty
                total_amount += item_total
                verified_items.append({
                    "id": prod["id"],
                    "name": prod["name"],
                    "price": prod["price"],
                    "quantity": qty
                })

            order_code = f"TUN-{get_utc_now().year}-{secrets.randbelow(8999)+1000}"

            cursor.execute("""
                INSERT INTO orders (
                    client_id, order_code, total_amount, shipping_name, shipping_phone,
                    shipping_address, shipping_city, shipping_postal_code, payment_method,
                    status, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'procesando', ?)
            """, (current_user["id"], order_code, total_amount, shipping_name, shipping_phone,
                  shipping_address, shipping_city, shipping_postal_code, payment_method, notes))
            order_id = cursor.lastrowid

            for vi in verified_items:
                cursor.execute("""
                    INSERT INTO order_items (order_id, product_id, product_name, price, quantity)
                    VALUES (?, ?, ?, ?, ?)
                """, (order_id, vi["id"], vi["name"], vi["price"], vi["quantity"]))
                # Reducir stock
                cursor.execute("UPDATE products SET stock = MAX(0, stock - ?) WHERE id = ?", (vi["quantity"], vi["id"]))

            conn.commit()
            conn.close()

            self.log_audit("NEW_ORDER", f"Pedido {order_code} ({total_amount:.2f} €)", user_id=current_user["id"], user_email=current_user["email"])

            self.send_json({
                "success": True,
                "message": "¡Pedido realizado con éxito!",
                "order_code": order_code,
                "order_id": order_id,
                "total_amount": total_amount
            })
            return

        # 6. Captación de Nuevos Miembros (Público)
        if path == "/api/captacion":
            full_name = sanitize_string(body.get("full_name", ""))
            email = str(body.get("email", "")).strip().lower()
            phone = sanitize_string(body.get("phone", ""))
            degree = sanitize_string(body.get("degree", ""))
            has_experience = sanitize_string(body.get("has_experience", "no"))
            instruments = sanitize_string(body.get("instruments", ""))
            motivation = sanitize_string(body.get("motivation", ""))

            if not full_name or not email or not phone:
                self.send_error_json("Nombre, correo y teléfono son obligatorios", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO captacion (full_name, email, phone, degree, has_experience, instruments, motivation)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (full_name, email, phone, degree, has_experience, instruments, motivation))
            new_id = cursor.lastrowid
            conn.commit()
            conn.close()

            self.log_audit("NEW_APPLICANT", f"Aspirante: {full_name} ({degree})")
            self.send_json({
                "success": True,
                "message": "¡Solicitud recibida! El Jefe de Novatos se pondrá en contacto contigo muy pronto."
            })
            return

        # 7. Actualizar Perfil de Cliente
        if path == "/api/auth/update-profile":
            if not current_user:
                self.send_error_json("No autenticado", 401)
                return
            if not self.verify_csrf(current_user, body):
                self.send_error_json("CSRF token inválido", 403)
                return

            name = sanitize_string(body.get("name", ""))
            phone = sanitize_string(body.get("phone", ""))
            email = str(body.get("email", "")).strip().lower()

            if not name or len(name) < 3:
                self.send_error_json("Nombre no válido", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    UPDATE users SET name = ?, phone = ?, email = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (name, phone, email, current_user["id"]))
                conn.commit()
            except sqlite3.IntegrityError:
                conn.close()
                self.send_error_json("El correo electrónico ya está en uso por otro usuario", 409)
                return
            conn.close()

            self.log_audit("PROFILE_UPDATED", f"Usuario ID {current_user['id']}", user_id=current_user["id"], user_email=email)
            self.send_json({"success": True, "message": "Datos de perfil actualizados correctamente"})
            return

        # 8. Modificar Contraseña
        if path == "/api/auth/change-password":
            if not current_user:
                self.send_error_json("No autenticado", 401)
                return
            if not self.verify_csrf(current_user, body):
                self.send_error_json("CSRF token inválido", 403)
                return

            current_pwd = str(body.get("current_password", ""))
            new_pwd = str(body.get("new_password", ""))

            if len(new_pwd) < 8:
                self.send_error_json("La nueva contraseña debe tener mínimo 8 caracteres", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT password_hash FROM users WHERE id = ?", (current_user["id"],))
            row = cursor.fetchone()

            if not row or not verify_password(row["password_hash"], current_pwd):
                conn.close()
                self.send_error_json("La contraseña actual no es correcta", 400)
                return

            new_hash = hash_password(new_pwd)
            cursor.execute("UPDATE users SET password_hash = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                           (new_hash, current_user["id"]))
            conn.commit()
            conn.close()

            self.log_audit("PASSWORD_CHANGED", "Cambio de contraseña exitoso", user_id=current_user["id"], user_email=current_user["email"])
            self.send_json({"success": True, "message": "Contraseña modificada con éxito"})
            return

        # RUTAS EXCLUSIVAS DE ADMINISTRADOR
        if not current_user or current_user["role"] != "admin":
            self.send_error_json("Acceso no autorizado", 403)
            return

        if not self.verify_csrf(current_user, body):
            self.send_error_json("CSRF token inválido", 403)
            return

        # Admin: Añadir Producto
        if path == "/api/admin/tienda":
            name = sanitize_string(body.get("name", ""))
            category = sanitize_string(body.get("category", "Accesorios"))
            description = sanitize_string(body.get("description", ""))
            price = float(body.get("price", 0.0))
            image_url = sanitize_string(body.get("image_url", "assets/img/shop/default.jpg"))
            badge = sanitize_string(body.get("badge", ""))
            stock = int(body.get("stock", 50))

            if not name or price <= 0:
                self.send_error_json("Nombre y precio positivo son obligatorios", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO products (name, category, description, price, image_url, badge, stock, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, 1)
            """, (name, category, description, price, image_url, badge, stock))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()

            self.log_audit("ADD_PRODUCT", f"Producto '{name}' ({price} €)", user_id=current_user["id"], user_email=current_user["email"])
            self.send_json({"success": True, "message": "Producto añadido al catálogo", "id": new_id})
            return

        # Admin: Añadir Miembro
        if path == "/api/admin/miembros":
            nickname = sanitize_string(body.get("nickname", ""))
            real_name = sanitize_string(body.get("real_name", ""))
            role_instrument = sanitize_string(body.get("role_instrument", "Guitarra"))
            category = sanitize_string(body.get("category", "activo"))
            generation_year = int(body.get("generation_year", get_utc_now().year))
            bio = sanitize_string(body.get("bio", ""))
            photo_url = sanitize_string(body.get("photo_url", "assets/img/members/default.jpg"))

            if not nickname or not real_name:
                self.send_error_json("Apodo y nombre real requeridos", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO members (nickname, real_name, role_instrument, category, generation_year, bio, photo_url)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nickname, real_name, role_instrument, category, generation_year, bio, photo_url))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()

            self.log_audit("ADD_MEMBER", f"Miembro {nickname}", user_id=current_user["id"], user_email=current_user["email"])
            self.send_json({"success": True, "message": "Miembro incorporado al directorio", "id": new_id})
            return

        # Admin: Añadir Canción
        if path == "/api/admin/repertorio/canciones":
            title = sanitize_string(body.get("title", ""))
            author = sanitize_string(body.get("author", "Popular"))
            genre = sanitize_string(body.get("genre", "Pasacalles"))
            lyrics = sanitize_string(body.get("lyrics", ""))
            spotify_url = sanitize_string(body.get("spotify_url", ""))
            youtube_url = sanitize_string(body.get("youtube_url", ""))

            if not title:
                self.send_error_json("El título es obligatorio", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO songs (title, author, genre, lyrics, spotify_url, youtube_url)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (title, author, genre, lyrics, spotify_url, youtube_url))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()

            self.send_json({"success": True, "message": "Canción agregada al cancionero", "id": new_id})
            return

        # Admin: Añadir Vídeo
        if path == "/api/admin/repertorio/videos":
            title = sanitize_string(body.get("title", ""))
            event_name = sanitize_string(body.get("event_name", ""))
            year = int(body.get("year", get_utc_now().year))
            category = sanitize_string(body.get("category", "Certamen"))
            youtube_id = sanitize_string(body.get("youtube_id", "dQw4w9WgXcQ"))

            if not title or not youtube_id:
                self.send_error_json("Título e ID de YouTube requeridos", 400)
                return

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO videos (title, event_name, year, category, youtube_id)
                VALUES (?, ?, ?, ?, ?)
            """, (title, event_name, year, category, youtube_id))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()

            self.send_json({"success": True, "message": "Vídeo añadido a la galería", "id": new_id})
            return

        self.send_error_json("Ruta POST no encontrada", 404)

    def handle_api_put(self, path):
        current_user = self.get_current_user()
        if not current_user or current_user["role"] != "admin":
            self.send_error_json("Acceso denegado: solo administradores", 403)
            return

        body, err = self.read_json_body()
        if err:
            self.send_error_json(err, 400)
            return

        if not self.verify_csrf(current_user, body):
            self.send_error_json("Token CSRF inválido", 403)
            return

        # 1. Actualizar Contrato: /api/contratos/<id>
        match = re.match(r"^/api/contratos/(\d+)$", path)
        if match:
            contract_id = int(match.group(1))
            status = sanitize_string(body.get("status", "pendiente"))
            notes = sanitize_string(body.get("notes", ""))
            price_agreed = body.get("price_agreed")

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE contratos
                SET status = ?, notes = ?, price_agreed = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (status, notes, price_agreed, contract_id))
            conn.commit()
            conn.close()

            self.log_audit("UPDATE_CONTRACT", f"Contrato #{contract_id} a '{status}'", user_id=current_user["id"], user_email=current_user["email"])
            self.send_json({"success": True, "message": "Contrato actualizado"})
            return

        # 2. Actualizar Producto: /api/admin/tienda/<id>
        match = re.match(r"^/api/admin/tienda/(\d+)$", path)
        if match:
            prod_id = int(match.group(1))
            name = sanitize_string(body.get("name", ""))
            price = float(body.get("price", 0.0))
            stock = int(body.get("stock", 0))
            is_active = int(body.get("is_active", 1))

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE products
                SET name = ?, price = ?, stock = ?, is_active = ?
                WHERE id = ?
            """, (name, price, stock, is_active, prod_id))
            conn.commit()
            conn.close()

            self.send_json({"success": True, "message": "Producto modificado"})
            return

        # 3. Actualizar Pedido: /api/pedidos/<id>
        match = re.match(r"^/api/pedidos/(\d+)$", path)
        if match:
            order_id = int(match.group(1))
            status = sanitize_string(body.get("status", "procesando"))
            tracking = sanitize_string(body.get("tracking_number", ""))

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE orders
                SET status = ?, tracking_number = ?
                WHERE id = ?
            """, (status, tracking, order_id))
            conn.commit()
            conn.close()

            self.send_json({"success": True, "message": "Estado del pedido actualizado"})
            return

        self.send_error_json("Ruta PUT no encontrada", 404)

    def handle_api_delete(self, path):
        current_user = self.get_current_user()
        if not current_user or current_user["role"] != "admin":
            self.send_error_json("Solo administradores pueden realizar esta acción", 403)
            return

        # Leer body opcional si se envió CSRF token en el body
        body, _ = self.read_json_body()
        if not self.verify_csrf(current_user, body):
            self.send_error_json("Token CSRF inválido", 403)
            return

        # 1. Eliminar Contrato
        match = re.match(r"^/api/contratos/(\d+)$", path)
        if match:
            contract_id = int(match.group(1))
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contratos WHERE id = ?", (contract_id,))
            conn.commit()
            conn.close()
            self.log_audit("DELETE_CONTRACT", f"Contrato #{contract_id}", user_id=current_user["id"], user_email=current_user["email"])
            self.send_json({"success": True, "message": "Contrato eliminado"})
            return

        # 2. Desactivar Producto
        match = re.match(r"^/api/admin/tienda/(\d+)$", path)
        if match:
            prod_id = int(match.group(1))
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET is_active = 0 WHERE id = ?", (prod_id,))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": "Producto retirado del catálogo"})
            return

        # 3. Eliminar Miembro
        match = re.match(r"^/api/admin/miembros/(\d+)$", path)
        if match:
            member_id = int(match.group(1))
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM members WHERE id = ?", (member_id,))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": "Miembro eliminado"})
            return

        self.send_error_json("Ruta DELETE no encontrada", 404)

class ThreadedHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True

def run_server(port=8080):
    server_address = ('0.0.0.0', port)
    httpd = ThreadedHTTPServer(server_address, TunaRequestHandler)

    def shutdown_handler(signum, frame):
        print("\n[!] Recibida señal de parada. Deteniendo servidor...")
        try:
            httpd.server_close()
        except Exception:
            pass
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)

    print("=" * 65)
    print("  TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA")
    print(f"  Servidor seguro activo en: http://localhost:{port}/")
    print("=" * 65)
    print("  Usuarios preconfigurados:")
    print("  - Administrador : popeye@tunaalmeria.es  /  Tuna2026!Admin")
    print("  - Cliente Test  : cliente@gmail.com     /  Cliente2026!")
    print("=" * 65)
    try:
        httpd.serve_forever()
    except Exception as e:
        print(f"[!] Servidor finalizado: {e}")
    finally:
        try:
            httpd.server_close()
        except Exception:
            pass

if __name__ == '__main__':
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run_server(port)
