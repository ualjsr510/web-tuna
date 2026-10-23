#!/usr/bin/env python3
"""
Script de inicialización y poblado de la base de datos de la Tuna de Derecho de Almería.
Genera contraseñas con PBKDF2-HMAC-SHA256 (estándar criptográfico seguro).
"""

import os
import sqlite3
import hashlib
import secrets
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "tuna.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

def hash_password(password: str) -> str:
    """Genera un hash seguro con salt aleatorio de 16 bytes y 100,000 iteraciones PBKDF2."""
    salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    ).hex()
    return f"pbkdf2:sha256:100000${salt}${key}"

def init_database():
    print(f"[*] Inicializando base de datos en: {DB_PATH}")
    
    # Si existe una base previa y queremos reiniciar limpiamente
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
            print("[+] Base de datos previa eliminada.")
        except Exception as e:
            print(f"[!] Aviso al eliminar base previa: {e}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("PRAGMA journal_mode = WAL;")

    # 1. Cargar esquema DDL
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    print("[+] Esquema SQL ejecutado con éxito.")

    # 2. Insertar usuarios iniciales
    admin_hash = hash_password("Tuna2026!Admin")
    client_hash = hash_password("Cliente2026!")

    users_data = [
        ("popeye@tunaalmeria.es", admin_hash, "Popeye (Administrador Oficial)", "+34 611 223 344", "admin"),
        ("cliente@gmail.com", client_hash, "Juan Pérez Gómez", "+34 622 334 455", "cliente"),
        ("maria.boda@hotmail.com", client_hash, "María Rodríguez López", "+34 633 445 566", "cliente")
    ]

    cursor.executemany("""
        INSERT INTO users (email, password_hash, name, phone, role)
        VALUES (?, ?, ?, ?, ?)
    """, users_data)
    print(f"[+] {len(users_data)} usuarios insertados.")

    # 3. Insertar Miembros de la Tuna
    members_data = [
        ("Popeye", "José Manuel Navarro", "Guitarra y Solista (Director)", "veterano", 2014,
         "Fundador del ciclo moderno y responsable de la dirección musical y contrataciones.", "assets/img/members/popeye.jpg", 1, 1),
        ("Percus", "Antonio Alarcón", "Pandereta y Percusión", "activo", 2019,
         "Maestro panderetero, malabares y responsable de archivos audiovisuales de la agrupación.", "assets/img/members/percus.jpg", 2, 1),
        ("Dolly", "Francisco Javier Ruiz", "Bandurria y Coros", "veterano", 2016,
         "Virtuoso de los plectros y encargado de tutorizar a los nuevos aspirantes y novatos.", "assets/img/members/dolly.jpg", 3, 1),
        ("El Abuelo", "Don Carlos Benítez", "Laúd Español", "veterano", 2010,
         "Medalla de Oro de la Tuna. Custodio del libreto histórico y tradiciones académicas.", "assets/img/members/abuelo.jpg", 4, 1),
        ("Espinete", "David Morales", "Bandurria Solista", "activo", 2021,
         "Primera bandurria en certámenes y arreglista de temas clásicos y pasodobles.", "assets/img/members/espinete.jpg", 5, 1),
        ("Chispas", "Alejandro Torres", "Bandera y Baile de Capa", "activo", 2022,
         "Abanderado oficial, acrobacias con estandarte y coreografías en certámenes nacionales.", "assets/img/members/chispas.jpg", 6, 1),
        ("El Notas", "Sergio Carmona", "Guitarra Española", "activo", 2023,
         "Ritmo armónico incansable y corista en las serenatas nocturnas.", "assets/img/members/notas.jpg", 7, 1),
        ("El Chispa", "Ignacio Soler", "Novato Aspirante", "novato", 2026,
         "Estudiante de 1º de Derecho, aprendiendo bandurria y tradición tunera desde cero.", "assets/img/members/chispa.jpg", 8, 1)
    ]

    cursor.executemany("""
        INSERT INTO members (nickname, real_name, role_instrument, category, generation_year, bio, photo_url, order_num, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, members_data)
    print(f"[+] {len(members_data)} miembros creados.")

    # 4. Insertar Productos de Tienda
    products_data = [
        ("Camiseta Oficial Tuna de Derecho", "Ropa", "Camiseta 100% algodón orgánico color granate con escudo oficial serigrafiado.", 18.00, "assets/img/shop/camiseta.jpg", "Nuevo", 45, 1),
        ("CD Oficial 'Noche de Ronda y Pasacalles'", "Música", "Álbum conmemorativo grabado en directo con 14 canciones tradicionales remasterizadas.", 12.00, "assets/img/shop/disco.jpg", "Más Vendido", 80, 1),
        ("Beca Oficial de Derecho de Almería", "Tradición", "Beca reglamentaria en paño rojo carmesí con escudo bordado de la Facultad.", 35.00, "assets/img/shop/beca.jpg", "Oficial", 20, 1),
        ("Parche Conmemorativo Bordado", "Accesorios", "Emblema termoadhesivo o para coser en capa, chaqueta o mochila con hilo dorado.", 6.50, "assets/img/shop/parche.jpg", "Top", 150, 1),
        ("Juego de Cintas de Capa Bordadas", "Tradición", "Pack de 3 cintas de raso personalizadas con dedicatorias y lemas universitarios.", 15.00, "assets/img/shop/cintas.jpg", "Edición Especial", 35, 1),
        ("Sudadera Universitaria Granate", "Ropa", "Sudadera con capucha y bolsillo canguro, escudo bordado de la Tuna y UAL.", 32.00, "assets/img/shop/sudadera.jpg", "Popular", 28, 1)
    ]

    cursor.executemany("""
        INSERT INTO products (name, category, description, price, image_url, badge, stock, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, products_data)
    print(f"[+] {len(products_data)} productos en catálogo.")

    # 5. Insertar Repertorio Musical (Cancionero)
    songs_data = [
        ("Clavelitos", "Genaro Monreal", "Pasacalles", "Disco Oficial Tuna de Derecho", "3:15",
         "Mocita dame el clavel, dame el clavel de tu boca...\nPa eso no hay que tener tanta vergüenza ni poca.\nYo te daré un cascabel, te lo prometo mocita,\nsi tú me das ese clavel que llevas en tu boquita.",
         "https://open.spotify.com/track/clavelitos", "https://youtube.com/watch?v=clavelitos", "", 1),
        ("Fonseca", "Popular / Tradicional", "Himno Tunero", "Disco Oficial Tuna de Derecho", "3:45",
         "Adiós, villa de Carracedo, adiós para no volver...\nQue me voy para la Habana, adiós mi linda mujer.\nNo te acuerdas cuando te decía a la sombra de un verde laurel...",
         "https://open.spotify.com/track/fonseca", "https://youtube.com/watch?v=fonseca", "", 1),
        ("La Morena de mi Copla", "Carlos Castellano", "Pasodoble", "Disco Oficial Tuna de Derecho", "3:30",
         "Julio Romero de Torres pintó a la mujer morena...\nCon ojos de misterio y el alma llena de pena.\nPuso en sus manos de bronce la guitarra cantora...",
         "https://open.spotify.com/track/morena", "https://youtube.com/watch?v=morena", "", 1),
        ("Horas de Ronda", "Tradicional", "Serenata", "Disco Oficial Tuna de Derecho", "3:50",
         "Horas de ronda, de la noche y del silencio...\nCuando la luna alumbra el firmamento.\nCantan los tunos con dulce melodía,\npara decirte que te quiero vida mía.",
         "https://open.spotify.com/track/horas", "https://youtube.com/watch?v=horas", "", 0),
        ("Almería, Tierra Noble", "Popular Almeriense", "Jota / Homenaje", "Disco Oficial Tuna de Derecho", "4:10",
         "Almería de mi vida, tierra noble y marinera...\nBajo el sol de la Alcazaba florece la primavera.\nCanta la Tuna cantares con orgullo y emoción...",
         "https://open.spotify.com/track/almeria", "https://youtube.com/watch?v=almeria", "", 1),
        ("Carrascosa", "Jaime Texidor", "Pasacalles", "Disco Oficial Tuna de Derecho", "2:55",
         "Instrumental vibrante de bandurrias y laúdes en pasacalles por el centro de la ciudad.",
         "https://open.spotify.com/track/carrascosa", "https://youtube.com/watch?v=carrascosa", "", 0)
    ]

    cursor.executemany("""
        INSERT INTO songs (title, author, genre, album, duration, lyrics, spotify_url, youtube_url, audio_url, is_favorite)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, songs_data)
    print(f"[+] {len(songs_data)} canciones catalogadas.")

    # 6. Insertar Vídeos y Actuaciones
    videos_data = [
        ("Primer Premio Certamen Nacional de Tunas de Derecho", "Certamen Nacional de Alicante", 2025, "12:40", "Certamen", "dQw4w9WgXcQ", "assets/img/videos/certamen_alicante.jpg", "14.2K visualizaciones"),
        ("Serenata de Gala bajo la Alcazaba de Almería", "Noche de las Velas Almería", 2025, "06:15", "Serenata", "dQw4w9WgXcQ", "assets/img/videos/serenata_alcazaba.jpg", "8.9K visualizaciones"),
        ("Pasacalles de Feria del Mediodía Almería", "Feria de Almería", 2025, "04:50", "Pasacalles", "dQw4w9WgXcQ", "assets/img/videos/feria_almeria.jpg", "5.1K visualizaciones"),
        ("Ronda Romántica de Bodas - Almería Centro", "Boda Privada Catedral", 2024, "05:20", "Boda", "dQw4w9WgXcQ", "assets/img/videos/boda_catedral.jpg", "9.7K visualizaciones")
    ]

    cursor.executemany("""
        INSERT INTO videos (title, event_name, year, duration, category, youtube_id, thumbnail_url, views_text)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, videos_data)
    print(f"[+] {len(videos_data)} vídeos catalogados.")

    # 7. Insertar Contratos / Solicitudes
    contratos_data = [
        (2, "Juan Pérez Gómez", "cliente@gmail.com", "+34 622 334 455", "Boda", "2026-11-14", "18:30",
         "Castillo de Santa Ana, Roquetas de Mar (Almería)", "120 personas", "A cargo de la Tuna",
         "Queremos una ronda sorpresa al salir de la iglesia y luego 3 pasodobles en el cóctel.", "confirmado", 350.00),
        (3, "María Rodríguez López", "maria.boda@hotmail.com", "+34 633 445 566", "Serenata", "2026-11-20", "21:00",
         "Plaza de la Catedral, Almería Capital", "25 personas", "No necesario",
         "Cumpleaños sorpresa para mi madre. Le encantan Clavelitos y Horas de Ronda.", "pendiente", None),
        (None, "Carlos Martínez Ruiz", "carlos.m@empresa.com", "+34 644 556 677", "Graduación", "2026-12-05", "19:00",
         "Paraninfo de la Universidad de Almería (UAL)", "300 personas", "En el campus UAL",
         "Actuación de clausura en el acto de graduación de Derecho.", "confirmado", 450.00),
        (None, "Laura Sánchez Vega", "laura.boda@gmail.com", "+34 655 667 788", "Puerta de Iglesia", "2026-12-19", "13:00",
         "Iglesia de San Pedro, Almería", "80 personas", "A cargo de la Tuna",
         "Ronda a la salida de la ceremonia.", "pendiente", None)
    ]

    cursor.executemany("""
        INSERT INTO contratos (client_id, client_name, client_email, client_phone, event_type, event_date, event_time,
                              location, attendees, transport_logistics, notes, status, price_agreed)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, contratos_data)
    print(f"[+] {len(contratos_data)} contratos iniciales.")

    # 8. Insertar Pedidos de prueba
    cursor.execute("""
        INSERT INTO orders (client_id, order_code, total_amount, shipping_name, shipping_phone,
                           shipping_address, shipping_city, shipping_postal_code, payment_method, status, tracking_number, notes)
        VALUES (2, 'TUN-2026-8941', 30.00, 'Juan Pérez Gómez', '+34 622 334 455',
                'Paseo de Almería, 42, 3º B', 'Almería', '04001', 'Bizum', 'enviado', 'ES-CORREOS-98124', 'Dejar en conserjería si no estoy')
    """)
    order_id = cursor.lastrowid
    cursor.execute("""
        INSERT INTO order_items (order_id, product_id, product_name, price, quantity)
        VALUES (?, 1, 'Camiseta Oficial Tuna de Derecho', 18.00, 1),
               (?, 2, 'CD Oficial ''Noche de Ronda y Pasacalles''', 12.00, 1)
    """, (order_id, order_id))

    cursor.execute("""
        INSERT INTO orders (client_id, order_code, total_amount, shipping_name, shipping_phone,
                           shipping_address, shipping_city, shipping_postal_code, payment_method, status, tracking_number, notes)
        VALUES (2, 'TUN-2026-9022', 15.00, 'Juan Pérez Gómez', '+34 622 334 455',
                'Paseo de Almería, 42, 3º B', 'Almería', '04001', 'Transferencia Bancaria', 'procesando', NULL, 'Pedido de regalo')
    """)
    order_id_2 = cursor.lastrowid
    cursor.execute("""
        INSERT INTO order_items (order_id, product_id, product_name, price, quantity)
        VALUES (?, 5, 'Juego de Cintas de Capa Bordadas', 15.00, 1)
    """, (order_id_2,))
    print("[+] Pedidos de prueba generados.")

    # 9. Solicitud de captación de prueba
    cursor.execute("""
        INSERT INTO captacion (full_name, email, phone, degree, has_experience, instruments, motivation, status)
        VALUES ('Gonzalo Ruiz Medina', 'gonzalo.derecho@ual.es', '+34 666 777 888', 'Grado en Derecho (UAL)', 'no',
                'Ninguno, pero con muchas ganas de aprender bandurria', 'Me gusta mucho el ambiente de camaradería, los viajes y la tradición universitaria.', 'pendiente')
    """)

    conn.commit()
    conn.close()
    print("[✓] Base de datos creada y sembrada con éxito en:", DB_PATH)

if __name__ == '__main__':
    init_database()
