-- ============================================================================
-- BASE DE DATOS OFICIAL: TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
-- Esquema Relacional SQL (SQLite / MySQL Compatible)
-- ============================================================================

-- 1. Tabla de Usuarios (Cuentas de clientes y administradores)
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(20) NOT NULL DEFAULT 'cliente', -- 'cliente', 'admin'
    nombre VARCHAR(80) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(200),
    ciudad VARCHAR(80) DEFAULT 'Almería',
    codigo_postal VARCHAR(10) DEFAULT '04001',
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo INTEGER DEFAULT 1
);

-- 2. Tabla de Categorías de la Tienda
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(60) NOT NULL UNIQUE,
    slug VARCHAR(60) NOT NULL UNIQUE,
    descripcion TEXT
);

-- 3. Tabla de Productos del Catálogo
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo VARCHAR(30) UNIQUE,
    categoria_id INTEGER NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    imagen VARCHAR(255),
    tallas_disponibles VARCHAR(100), -- separadas por comas o pipes: 'S,M,L,XL'
    descripcion TEXT,
    activo INTEGER DEFAULT 1,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
);

-- 4. Tabla de Pedidos de la Tienda
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_pedido VARCHAR(30) NOT NULL UNIQUE,
    usuario_id INTEGER NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    subtotal DECIMAL(10,2) NOT NULL,
    gastos_envio DECIMAL(10,2) DEFAULT 0.00,
    total DECIMAL(10,2) NOT NULL,
    estado VARCHAR(30) NOT NULL DEFAULT 'En preparación', -- 'En preparación', 'Enviado', 'Entregado', 'Cancelado'
    direccion_envio VARCHAR(200) NOT NULL,
    ciudad VARCHAR(80) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL,
    telefono_contacto VARCHAR(20),
    metodo_pago VARCHAR(50) DEFAULT 'Tarjeta de crédito',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE RESTRICT
);

-- 5. Líneas de Detalle de Pedido
CREATE TABLE IF NOT EXISTS pedido_lineas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL DEFAULT 1,
    precio_unitario DECIMAL(10,2) NOT NULL,
    talla VARCHAR(30),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE RESTRICT
);

-- 6. Tabla de Contratos de Actuaciones y Rondas
CREATE TABLE IF NOT EXISTS contratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_contrato VARCHAR(30) NOT NULL UNIQUE,
    usuario_id INTEGER NOT NULL,
    tipo_evento VARCHAR(80) NOT NULL, -- 'Boda', 'Serenata', 'Certamen', 'Acto Académico', 'Evento Privado'
    fecha_evento DATE NOT NULL,
    hora_evento TIME,
    lugar VARCHAR(200) NOT NULL,
    num_asistentes INTEGER,
    duracion_horas INTEGER DEFAULT 1,
    num_tunos INTEGER DEFAULT 6,
    precio_total DECIMAL(10,2) NOT NULL,
    estado VARCHAR(40) NOT NULL DEFAULT 'Pendiente', -- 'Pendiente', 'Confirmado', 'Finalizado', 'Cancelado'
    observaciones TEXT,
    fecha_solicitud DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE RESTRICT
);

-- 7. Tabla de Miembros de la Tuna (Censo oficial)
CREATE TABLE IF NOT EXISTS miembros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mote VARCHAR(60) NOT NULL,
    nombre_completo VARCHAR(120) NOT NULL,
    instrumento VARCHAR(80) NOT NULL,
    rango VARCHAR(40) NOT NULL DEFAULT 'Tuno', -- 'Tuno Mayor', 'Tuno', 'Pardillo', 'Veterano'
    fecha_ingreso DATE,
    foto VARCHAR(255),
    biografia TEXT,
    activo INTEGER DEFAULT 1
);

-- 8. Tabla de Certámenes y Galardones Históricos
CREATE TABLE IF NOT EXISTS certamenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(150) NOT NULL,
    ciudad VARCHAR(80) NOT NULL,
    ano INTEGER NOT NULL,
    premio VARCHAR(120) NOT NULL,
    descripcion TEXT,
    cartel_foto VARCHAR(255)
);

-- 9. Tabla de Canciones del Cancionero
CREATE TABLE IF NOT EXISTS canciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(120) NOT NULL,
    genero VARCHAR(60) NOT NULL, -- 'Bolero', 'Pasodoble', 'Vals', 'Ronda', 'Popular'
    duracion VARCHAR(10) NOT NULL,
    letra TEXT,
    orden INTEGER DEFAULT 0
);

-- 10. Tabla de Aspirantes / Solicitudes para Unirse
CREATE TABLE IF NOT EXISTS aspirantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    titulacion VARCHAR(120),
    curso VARCHAR(20),
    instrumento VARCHAR(80),
    experiencia_musical TEXT,
    fecha_solicitud DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(30) DEFAULT 'Pendiente'
);

