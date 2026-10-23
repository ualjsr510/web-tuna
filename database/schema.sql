-- Base de Datos: Tuna de la Facultad de Derecho de Almería
-- Esquema relacional con integridad referencial, índices y validaciones

PRAGMA foreign_keys = ON;

-- 1. Usuarios (Administradores y Clientes)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL COLLATE NOCASE,
    password_hash TEXT NOT NULL,
    name TEXT NOT NULL,
    phone TEXT,
    role TEXT NOT NULL DEFAULT 'cliente' CHECK(role IN ('admin', 'cliente')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);

-- 2. Sesiones activas con tokens seguros y CSRF
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    csrf_token TEXT NOT NULL,
    ip_address TEXT,
    user_agent TEXT,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_expires ON sessions(expires_at);

-- 3. Contratos / Solicitudes de Actuación
CREATE TABLE IF NOT EXISTS contratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    client_name TEXT NOT NULL,
    client_email TEXT NOT NULL,
    client_phone TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_date TEXT NOT NULL,
    event_time TEXT NOT NULL,
    location TEXT NOT NULL,
    attendees TEXT,
    transport_logistics TEXT,
    notes TEXT,
    status TEXT NOT NULL DEFAULT 'pendiente' CHECK(status IN ('pendiente', 'confirmado', 'cancelado', 'finalizado')),
    price_agreed REAL DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_contratos_client ON contratos(client_id);
CREATE INDEX IF NOT EXISTS idx_contratos_date ON contratos(event_date);
CREATE INDEX IF NOT EXISTS idx_contratos_status ON contratos(status);

-- 4. Productos de Merchandising
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK(price >= 0),
    image_url TEXT NOT NULL,
    badge TEXT,
    stock INTEGER NOT NULL DEFAULT 50 CHECK(stock >= 0),
    is_active INTEGER NOT NULL DEFAULT 1 CHECK(is_active IN (0, 1)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_products_active ON products(is_active);

-- 5. Pedidos de Merchandising
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    order_code TEXT UNIQUE NOT NULL,
    total_amount REAL NOT NULL CHECK(total_amount >= 0),
    shipping_name TEXT NOT NULL,
    shipping_phone TEXT NOT NULL,
    shipping_address TEXT NOT NULL,
    shipping_city TEXT NOT NULL DEFAULT 'Almería',
    shipping_postal_code TEXT NOT NULL,
    payment_method TEXT NOT NULL DEFAULT 'Bizum / Transferencia',
    status TEXT NOT NULL DEFAULT 'procesando' CHECK(status IN ('procesando', 'enviado', 'entregado', 'cancelado')),
    tracking_number TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_orders_client ON orders(client_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);

-- 6. Líneas de Pedido
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id),
    product_name TEXT NOT NULL,
    price REAL NOT NULL CHECK(price >= 0),
    quantity INTEGER NOT NULL DEFAULT 1 CHECK(quantity > 0)
);

CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items(order_id);

-- 7. Directorio de Miembros
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT NOT NULL,
    real_name TEXT NOT NULL,
    role_instrument TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT 'activo' CHECK(category IN ('veterano', 'activo', 'novato')),
    generation_year INTEGER NOT NULL DEFAULT 2020,
    bio TEXT,
    photo_url TEXT NOT NULL,
    order_num INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1 CHECK(is_active IN (0, 1)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_members_category ON members(category);
CREATE INDEX IF NOT EXISTS idx_members_active ON members(is_active);

-- 8. Cancionero y Discografía
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT DEFAULT 'Popular / Tradicional',
    genre TEXT DEFAULT 'Pasacalles',
    album TEXT DEFAULT 'Disco Oficial Tuna de Derecho',
    duration TEXT DEFAULT '3:30',
    lyrics TEXT,
    spotify_url TEXT,
    youtube_url TEXT,
    audio_url TEXT,
    is_favorite INTEGER DEFAULT 0 CHECK(is_favorite IN (0, 1)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 9. Vídeos y Actuaciones
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    event_name TEXT NOT NULL,
    year INTEGER NOT NULL DEFAULT 2025,
    duration TEXT DEFAULT '4:00',
    category TEXT DEFAULT 'Certamen',
    youtube_id TEXT NOT NULL,
    thumbnail_url TEXT,
    views_text TEXT DEFAULT '1.2K visualizaciones',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. Solicitudes de Captación ("Únete a la Tuna")
CREATE TABLE IF NOT EXISTS captacion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    degree TEXT NOT NULL,
    has_experience TEXT NOT NULL DEFAULT 'no',
    instruments TEXT,
    motivation TEXT,
    status TEXT DEFAULT 'pendiente' CHECK(status IN ('pendiente', 'contactado', 'admitido', 'descartado')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 11. Auditoría de Seguridad (Audit Logs)
CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    user_email TEXT,
    action TEXT NOT NULL,
    details TEXT,
    ip_address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
