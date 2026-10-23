# Tuna de la Facultad de Derecho de Almería - Portal Web Completo

Aplicación web integral, modular y segura desarrollada para la **Tuna de la Facultad de Derecho de la Universidad de Almería (UAL)**, cumpliendo con los requisitos de negocio, wireframes y flujos definidos para los perfiles de **Visitante**, **Cliente** y **Administrador**.

---

## 1. Características Principales

1. **Portal del Visitante (`/visitante/`)**:
   - **Inicio (`inicio.html`)**: Presentación corporativa con diseño de alto impacto visual, llamadas a la acción, canciones destacadas, presentación de integrantes y formulario de boletín.
   - **La Tuna (`la-tuna.html`)**: Reseña histórica desde 1995, indumentaria tradicional (beca roja, jubón, gregüescos, capa con cintas) y directorio interactivo de miembros clasificado por rangos (veteranos, activos, novatos).
   - **Cancionero (`cancionero.html`)**: Repertorio digital con letras completas, acordes y enlaces a Spotify.
   - **Vídeos (`videos.html`)**: Galería de actuaciones en certámenes nacionales, serenatas y pasacalles con reproductor interactivo.
   - **Únete / Captación (`captacion.html`)**: Mensaje de bienvenida enfocado en el relevo generacional (*"No hace falta saber música ni tocar instrumento"*), plano de ubicación del local de ensayo en el Edificio C (Derecho) de la UAL, horarios y formulario de inscripción directa conectado con la base de datos.
   - **Contratación (`contratacion.html`)**: Explicación de tarifas personalizadas (*no se publican precios fijos debido a la variabilidad de desplazamiento y duración*) y canalización directa a Popeye por WhatsApp.
   - **Tienda (`tienda.html`)**: Catálogo de productos oficiales (sudaderas, camisetas, discos, becas, cintas de capa) con carrito de compras en tiempo real y pasarela de tramitación de pedidos.

2. **Portal del Cliente (`/cliente/`)**:
   - **Contratación (`contratacion.html`)**: Formulario para cotizar actuaciones (fecha, hora, lugar, aforo, transporte, tipo de evento) con cálculo estimativo y guardado en base de datos.
   - **Mis Pedidos (`pedidos.html`)**: Panel unificado donde el cliente consulta el estado de sus solicitudes de actuación y compras de merchandising.
   - **Datos Personales (`datos.html`)**: Consulta y modificación de datos de contacto con persistencia en SQLite.
   - **Seguridad (`gestionar-cuenta.html`)**: Medidor de fortaleza de contraseña y cambio de clave cifrada.

3. **Panel de Administración (`/admin/`)**:
   - **Contratos (`contratos.html`)**: Gestión y filtrado de solicitudes, aprobación/rechazo, asignación de precios acordados, notas internas y enlace rápido a WhatsApp con el cliente.
   - **Miembros (`miembros.html`)**: Altas, bajas y edición de tunos en el directorio oficial.
   - **Tienda (`tienda.html`)**: Control de precios, inventario/stock y alta de nuevos artículos.
   - **Repertorio (`repertorio.html`)**: Añadir canciones y vídeos a la web pública.

4. **Autenticación Segura (`/auth/`)**:
   - **Inicio de sesión (`login.html`)**: Acceso unificado para administradores y clientes con protección contra fuerza bruta.
   - **Registro (`registro.html`)**: Alta de nuevos clientes con validación estricta de formatos.

---

## 2. Base de Datos Relacional (`database/tuna.db`)

El sistema cuenta con una base de datos SQLite relacional gobernada por el esquema `database/schema.sql`:

- `users`: Cuentas con roles (`admin`, `cliente`), correo único, teléfono y contraseñas cifradas.
- `sessions`: Sesiones activas con tokens aleatorios de 256 bits y token CSRF sincronizado.
- `contratos`: Registro completo de solicitudes de actuación (lugar, fecha, tipo de evento, aforo, logística, notas, estado, precio acordado).
- `products`: Catálogo de merchandising (nombre, categoría, precio, stock, estado activo).
- `orders`: Pedidos de tienda realizados por clientes.
- `order_items`: Líneas de detalle de cada pedido.
- `members`: Integrantes de la agrupación (apodo, nombre real, instrumento, categoría, año de promoción).
- `songs`: Cancionero con autor, género, letra, enlace a Spotify y YouTube.
- `videos`: Actuaciones en certámenes con identificador de YouTube.
- `captacion`: Aspirantes a entrar en la Tuna (estudios, teléfono, experiencia musical, motivación).
- `audit_logs`: Registro de seguridad para auditoría de acciones sensibles.

---

## 3. Arquitectura de Seguridad Implementada

Para asegurar la robustez y protección contra ataques cibernéticos habituales:

1. **Almacenamiento Criptográfico de Contraseñas**:
   - Algoritmo **PBKDF2-HMAC-SHA256** con 100.000 iteraciones y salt criptográfico individual de 16 bytes.
   - Comparación en tiempo constante (`secrets.compare_digest`) para prevenir ataques de temporización (*timing attacks*).

2. **Gestión de Sesiones Segura**:
   - Tokens de sesión de 64 caracteres hexadecimales generados con `secrets.token_hex(32)`.
   - Cookies con directivas `HttpOnly` (inmunes al robo por Javascript en el navegador) y `SameSite=Strict`.

3. **Protección Anti-CSRF (Cross-Site Request Forgery)**:
   - Patrón *Synchronizer Token*. Cada sesión tiene un token CSRF único validado en todas las peticiones `POST`, `PUT` y `DELETE`.

4. **Prevención de Inyecciones SQL**:
   - El 100% de las consultas utilizan sentencias preparadas y parámetros vinculados (`?`), neutralizando cualquier intento de inyección de código SQL.

5. **Mitigación de XSS (Cross-Site Scripting) y Cabeceras de Seguridad**:
   - Sanitización de entradas con escape de entidades HTML (`html.escape`).
   - Cabeceras HTTP activas:
     - `Content-Security-Policy`: Restringe fuentes de scripts, marcos (Spotify, YouTube) y estilos.
     - `X-Content-Type-Options: nosniff`
     - `X-Frame-Options: SAMEORIGIN`
     - `X-XSS-Protection: 1; mode=block`
     - `Referrer-Policy: strict-origin-when-cross-origin`

6. **Protección contra Fuerza Bruta (Rate Limiting)**:
   - Bloqueo temporal por IP tras 5 intentos fallidos consecutivos de inicio de sesión durante 15 minutos.

7. **Control de Acceso Basado en Roles (RBAC)**:
   - Los endpoints de administración (`/api/admin/*`) verifican que el usuario posea el rol `admin`.
   - Las rutas de cliente verifican la propiedad de los recursos (un cliente solo puede ver sus propios pedidos y contratos).

---

## 4. Usuarios y Credenciales Preconfiguradas

| Perfil | Correo Electrónico | Contraseña | Rol |
| :--- | :--- | :--- | :--- |
| **Administrador (Popeye)** | `popeye@tunaalmeria.es` | `Tuna2026!Admin` | `admin` |
| **Cliente de Prueba (Juan)** | `cliente@gmail.com` | `Cliente2026!` | `cliente` |

*También es posible crear nuevos clientes en cualquier momento a través del formulario `/auth/registro.html`.*

---

## 5. Instrucciones de Ejecución

Para iniciar el servidor web y la base de datos:

```bash
# Opción 1: Mediante el script automático
./run.sh

# Opción 2: Ejecutando directamente con Python en el puerto deseado
python3 server.py 8080
```

Abre en tu navegador favorito:
👉 **[http://localhost:8080/](http://localhost:8080/)**
