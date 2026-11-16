-- =====================================================================
--  Tuna de la Facultad de Derecho de Almería · Base de datos MySQL 8
--  (8.0.16 o superior · InnoDB · utf8mb4)
--
--  Modela todo lo que usa el prototipo (carpeta prototipo/):
--    · Cuentas: Acceso, Registro, RecuperarContrasena, cliente/Cuenta*
--    · La tuna: Miembros, Historia, Unete, Formulario, LocalEnsayo
--    · Contratación: Contratacion, FormularioContratacion,
--      cliente/Contratos, admin/Contratos
--    · Tienda: Catalogo, Cesta, AccesoPedido → DireccionEnvio → MetodoPago
--      → ConfirmacionPedido → ReciboPedido, cliente/Pedido*, admin/Pedidos
--    · Cancionero y multimedia: Repertorio, Spotify, Fotos, Videos,
--      Certamenes
--    · Portada: noticias, próximas actuaciones, ofertas, contacto
--    · Panel de administración: estadísticas (vistas v_admin_*)
--
--  Los estados se guardan con el mismo texto que muestra el prototipo
--  ('Pendiente', 'En preparación', 'Devolución solicitada'...), y los
--  códigos de contrato y pedido tienen su formato (CTR-2026-01, PED-2026-081).
--
--  Uso:  mysql -u root -p < database/mysql/tuna.sql
--  ¡Ojo! Borra y vuelve a crear la base de datos «tuna».
-- =====================================================================

DROP DATABASE IF EXISTS tuna;
CREATE DATABASE tuna CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE tuna;
SET NAMES utf8mb4 COLLATE utf8mb4_spanish_ci;

-- =====================================================================
-- 1. CUENTAS
-- =====================================================================

-- Clientes y administradores. Registro.html pide nombre, apellidos, correo,
-- teléfono y contraseña; la dirección se guarda al hacer el primer pedido.
CREATE TABLE usuarios (
  id                     INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  email                  VARCHAR(255) NOT NULL,
  password_hash          VARCHAR(255) NOT NULL,                -- bcrypt (password_hash de PHP, bcryptjs...)
  rol                    ENUM('cliente','admin') NOT NULL DEFAULT 'cliente',
  nombre                 VARCHAR(80)  NOT NULL,
  apellidos              VARCHAR(120) NOT NULL DEFAULT '',
  telefono               VARCHAR(20)  NULL,                    -- "600 123 456" o "+34 600123456"
  direccion              VARCHAR(200) NULL,
  ciudad                 VARCHAR(100) NULL,
  codigo_postal          CHAR(5)      NULL,
  provincia              VARCHAR(100) NULL,
  activo                 BOOLEAN  NOT NULL DEFAULT TRUE,
  privacidad_aceptada_en DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_registro         DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ultimo_acceso          DATETIME NULL,
  UNIQUE KEY uq_usuarios_email (email),                        -- "Ya existe una cuenta registrada con este correo"
  KEY ix_usuarios_rol (rol, fecha_registro),
  CONSTRAINT ck_usuarios_email  CHECK (email LIKE '%_@_%._%'),
  CONSTRAINT ck_usuarios_nombre CHECK (CHAR_LENGTH(TRIM(nombre)) >= 2),
  CONSTRAINT ck_usuarios_tel    CHECK (telefono IS NULL OR REGEXP_LIKE(REPLACE(telefono, ' ', ''), '^(\\+34)?[0-9]{9}$')),
  CONSTRAINT ck_usuarios_cp     CHECK (codigo_postal IS NULL OR REGEXP_LIKE(codigo_postal, '^[0-9]{5}$'))
) ENGINE=InnoDB;

-- RecuperarContrasena.html: enlace de un solo uso enviado por correo.
CREATE TABLE tokens_recuperacion (
  id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id  INT UNSIGNED NOT NULL,
  token_hash  CHAR(64) NOT NULL,                               -- SHA-256 del token; el token en claro solo va en el correo
  expira_en   DATETIME NOT NULL,
  usado_en    DATETIME NULL,
  creado_en   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_token (token_hash),
  CONSTRAINT fk_token_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- =====================================================================
-- 2. LA TUNA Y ÚNETE
-- =====================================================================

CREATE TABLE instrumentos (
  id      TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre  VARCHAR(50) NOT NULL,
  orden   SMALLINT NOT NULL DEFAULT 0,
  UNIQUE KEY uq_instrumento (nombre)
) ENGINE=InnoDB;

-- Miembros.html (lista y ficha) y admin/Miembro*.html
CREATE TABLE miembros (
  id             INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre         VARCHAR(100) NOT NULL,
  instrumento_id TINYINT UNSIGNED NOT NULL,
  anio_ingreso   YEAR NULL,                                    -- "En la tuna desde"
  foto_url       VARCHAR(255) NULL,
  biografia      TEXT NULL,
  activo         BOOLEAN NOT NULL DEFAULT TRUE,
  orden          SMALLINT NOT NULL DEFAULT 0,
  KEY ix_miembro_instr (instrumento_id),
  FULLTEXT KEY ft_miembro (nombre),                            -- buscador de admin/MiembrosGestion
  CONSTRAINT fk_miembro_instr FOREIGN KEY (instrumento_id) REFERENCES instrumentos(id),
  CONSTRAINT ck_miembro_anio  CHECK (anio_ingreso IS NULL OR anio_ingreso >= 1993)
) ENGINE=InnoDB;

-- Formulario.html (Únete): no hace falta cuenta.
CREATE TABLE solicitudes_ingreso (
  id                  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre              VARCHAR(150) NOT NULL,
  email               VARCHAR(255) NOT NULL,
  telefono            VARCHAR(20)  NULL,
  instrumento_id      TINYINT UNSIGNED NULL,
  experiencia         TEXT NULL,
  privacidad_aceptada BOOLEAN NOT NULL,
  estado              ENUM('Nueva','Contactada','Aceptada','Descartada') NOT NULL DEFAULT 'Nueva',
  creado_en           DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY ix_ingreso_estado (estado),
  CONSTRAINT fk_ingreso_instr FOREIGN KEY (instrumento_id) REFERENCES instrumentos(id) ON DELETE SET NULL,
  CONSTRAINT ck_ingreso_email CHECK (email LIKE '%_@_%._%'),
  CONSTRAINT ck_ingreso_priv  CHECK (privacidad_aceptada = TRUE)
) ENGINE=InnoDB;

-- LocalEnsayo.html (y punto de recogida de pedidos en DireccionEnvio.html)
CREATE TABLE locales_ensayo (
  id         TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre     VARCHAR(100) NOT NULL,
  direccion  VARCHAR(150) NOT NULL,
  ciudad     VARCHAR(100) NOT NULL,
  edificio   VARCHAR(100) NULL,
  latitud    DECIMAL(9,6) NULL,
  longitud   DECIMAL(9,6) NULL,
  activo     BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE horarios_ensayo (
  id          SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  local_id    TINYINT UNSIGNED NOT NULL,
  dia_semana  TINYINT UNSIGNED NOT NULL,                       -- 1 = lunes … 7 = domingo
  hora_inicio TIME NOT NULL,
  hora_fin    TIME NOT NULL,
  CONSTRAINT fk_horario_local FOREIGN KEY (local_id) REFERENCES locales_ensayo(id) ON DELETE CASCADE,
  CONSTRAINT ck_horario_dia   CHECK (dia_semana BETWEEN 1 AND 7),
  CONSTRAINT ck_horario_hora  CHECK (hora_fin > hora_inicio)
) ENGINE=InnoDB;

-- =====================================================================
-- 3. CONTRATACIÓN
-- =====================================================================

-- Desplegable "Tipo de evento" de FormularioContratacion.html, con la tarifa
-- base de TunaForms.calculateQuote().
CREATE TABLE tipos_evento (
  id           TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  slug         VARCHAR(30)  NOT NULL,
  nombre       VARCHAR(100) NOT NULL,
  tarifa_base  DECIMAL(8,2) NOT NULL,
  orden        SMALLINT NOT NULL DEFAULT 0,
  UNIQUE KEY uq_tipo_evento_slug (slug)
) ENGINE=InnoDB;

-- Tarjetas informativas de Contratacion.html
CREATE TABLE servicios (
  id          TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre      VARCHAR(100) NOT NULL,
  descripcion VARCHAR(300) NOT NULL,
  activo      BOOLEAN NOT NULL DEFAULT TRUE,
  orden       SMALLINT NOT NULL DEFAULT 0
) ENGINE=InnoDB;

-- Solicitudes de actuación (TunaDB.contracts). Se guarda una copia del
-- contacto, como hace el prototipo (clientName, email, phone).
CREATE TABLE contratos (
  id                    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  codigo                VARCHAR(20)  NOT NULL DEFAULT '',      -- CTR-2026-01 (lo genera el trigger si llega vacío)
  usuario_id            INT UNSIGNED NULL,                     -- NULL si se borra la cuenta
  tipo_evento_id        TINYINT UNSIGNED NOT NULL,
  evento                VARCHAR(100) NOT NULL DEFAULT '',      -- lo que se muestra como "Evento" (service); por defecto, el tipo
  contacto_nombre       VARCHAR(200) NOT NULL DEFAULT '',      -- vacío → se copia de la cuenta
  contacto_email        VARCHAR(255) NOT NULL DEFAULT '',
  contacto_telefono     VARCHAR(20)  NULL,
  fecha                 DATE NOT NULL,
  hora                  TIME NULL,
  lugar                 VARCHAR(200) NOT NULL,
  asistentes            SMALLINT UNSIGNED NULL,
  horas                 TINYINT UNSIGNED NOT NULL DEFAULT 1,
  musicos               TINYINT UNSIGNED NOT NULL DEFAULT 6,
  desplazamiento        BOOLEAN NOT NULL DEFAULT FALSE,        -- fuera de Almería capital (+50 €)
  presupuesto           DECIMAL(8,2) NULL,                     -- NULL = "A convenir"
  observaciones         VARCHAR(1000) NOT NULL DEFAULT '',
  estado                ENUM('Pendiente','Confirmado','Rechazado','Realizado') NOT NULL DEFAULT 'Pendiente',
  condiciones_aceptadas BOOLEAN NOT NULL DEFAULT TRUE,
  creado_en             DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  actualizado_en        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY uq_contrato_codigo (codigo),
  KEY ix_contrato_usuario (usuario_id, fecha),
  KEY ix_contrato_estado (estado),
  KEY ix_contrato_creado (creado_en),
  CONSTRAINT fk_contrato_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL,
  CONSTRAINT fk_contrato_tipo    FOREIGN KEY (tipo_evento_id) REFERENCES tipos_evento(id),
  CONSTRAINT ck_contrato_asist   CHECK (asistentes IS NULL OR asistentes BETWEEN 1 AND 5000),
  CONSTRAINT ck_contrato_horas   CHECK (horas BETWEEN 1 AND 8),
  CONSTRAINT ck_contrato_musicos CHECK (musicos BETWEEN 1 AND 40),
  CONSTRAINT ck_contrato_presup  CHECK (presupuesto IS NULL OR presupuesto >= 0),
  CONSTRAINT ck_contrato_cond    CHECK (condiciones_aceptadas = TRUE)
) ENGINE=InnoDB;

-- Portada: "Próximas actuaciones y rondas en directo". Puede venir de un
-- contrato confirmado o ser una ronda/certamen propio.
CREATE TABLE actuaciones (
  id          SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  titulo      VARCHAR(150) NOT NULL,
  lugar       VARCHAR(150) NOT NULL,
  fecha       DATE NOT NULL,
  hora        TIME NULL,
  contrato_id INT UNSIGNED NULL,
  publica     BOOLEAN NOT NULL DEFAULT TRUE,
  KEY ix_actuacion_fecha (fecha),
  CONSTRAINT fk_actuacion_contrato FOREIGN KEY (contrato_id) REFERENCES contratos(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- =====================================================================
-- 4. TIENDA
-- =====================================================================

CREATE TABLE categorias_producto (
  id          TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  slug        VARCHAR(30) NOT NULL,                            -- data-cat del catálogo
  nombre      VARCHAR(60) NOT NULL,
  descripcion VARCHAR(150) NULL,
  orden       SMALLINT NOT NULL DEFAULT 0,
  UNIQUE KEY uq_catprod_slug (slug)
) ENGINE=InnoDB;

CREATE TABLE productos (
  id                INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  codigo            VARCHAR(20)  NOT NULL,                     -- id de la web: prod-1, prod-oferta-1...
  nombre            VARCHAR(150) NOT NULL,
  descripcion       VARCHAR(600) NOT NULL,
  categoria_id      TINYINT UNSIGNED NOT NULL,
  precio            DECIMAL(8,2) NOT NULL,
  precio_anterior   DECIMAL(8,2) NULL,                         -- tachado en las ofertas de la portada
  imagen_url        VARCHAR(255) NULL,
  etiqueta          VARCHAR(20)  NULL,                         -- TOP VENTAS, NUEVO, POPULAR...
  valoracion        DECIMAL(2,1) NULL,                         -- ★ 4.9
  num_valoraciones  INT UNSIGNED NOT NULL DEFAULT 0,           -- (42)
  en_catalogo       BOOLEAN NOT NULL DEFAULT TRUE,             -- FALSE: solo se vende desde la portada (packs)
  destacado_portada BOOLEAN NOT NULL DEFAULT FALSE,            -- "Promociones y descuentos especiales"
  orden             SMALLINT NOT NULL DEFAULT 0,
  activo            BOOLEAN NOT NULL DEFAULT TRUE,
  creado_en         DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_producto_codigo (codigo),
  KEY ix_producto_cat (categoria_id),
  FULLTEXT KEY ft_producto (nombre, descripcion),              -- buscador del catálogo
  CONSTRAINT fk_producto_cat     FOREIGN KEY (categoria_id) REFERENCES categorias_producto(id),
  CONSTRAINT ck_producto_precio  CHECK (precio >= 0),
  CONSTRAINT ck_producto_oferta  CHECK (precio_anterior IS NULL OR precio_anterior > precio),
  CONSTRAINT ck_producto_valor   CHECK (valoracion IS NULL OR valoracion BETWEEN 0 AND 5)
) ENGINE=InnoDB;

-- "Talla / Formato" de cada producto (S, M, CD Físico, 25 cm...) con su stock.
-- Todo producto tiene al menos una opción.
CREATE TABLE producto_opciones (
  id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  producto_id INT UNSIGNED NOT NULL,
  nombre      VARCHAR(40) NOT NULL,
  stock       INT UNSIGNED NULL,                               -- NULL = sin límite (descargas digitales, a medida)
  orden       SMALLINT NOT NULL DEFAULT 0,
  UNIQUE KEY uq_opcion (producto_id, nombre),
  CONSTRAINT fk_opcion_producto FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Pedido del embudo de 5 pasos. Admite compra sin cuenta (AccesoPedido →
-- "compra rápida"), por eso se copian los datos de contacto y de envío.
-- Nunca se guardan datos de tarjeta: solo el método y la referencia de la pasarela.
CREATE TABLE pedidos (
  id                 INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  codigo             VARCHAR(20)  NOT NULL DEFAULT '',         -- PED-2026-081 (lo genera el trigger si llega vacío)
  usuario_id         INT UNSIGNED NULL,                        -- NULL = compra como invitado
  cliente_nombre     VARCHAR(200) NOT NULL,
  cliente_email      VARCHAR(255) NOT NULL,
  cliente_telefono   VARCHAR(20)  NOT NULL,
  -- Paso 2: dirección y entrega (cliente/PedidoEditar.html la puede cambiar)
  envio_destinatario VARCHAR(200) NOT NULL,
  envio_telefono     VARCHAR(20)  NOT NULL,
  envio_direccion    VARCHAR(200) NOT NULL,
  envio_cp           CHAR(5)      NOT NULL,
  envio_ciudad       VARCHAR(100) NOT NULL,
  envio_provincia    VARCHAR(100) NOT NULL,
  modalidad_entrega  ENUM('domicilio','recogida') NOT NULL DEFAULT 'domicilio',
  notas_entrega      VARCHAR(500) NULL,
  -- Paso 3: pago
  metodo_pago        ENUM('Tarjeta','Bizum','Transferencia') NOT NULL,
  referencia_pago    VARCHAR(100) NULL,
  -- Importes (envío: 4,50 €; gratis por encima de 40 € o con recogida)
  subtotal           DECIMAL(10,2) NOT NULL,
  gastos_envio       DECIMAL(10,2) NOT NULL DEFAULT 0,
  total              DECIMAL(10,2) AS (subtotal + gastos_envio) STORED,
  estado             ENUM('Pendiente','En preparación','Enviado','Entregado','Devolución solicitada','Devuelto')
                     NOT NULL DEFAULT 'En preparación',
  creado_en          DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  actualizado_en     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY uq_pedido_codigo (codigo),
  KEY ix_pedido_usuario (usuario_id, creado_en),
  KEY ix_pedido_estado (estado),
  KEY ix_pedido_creado (creado_en),
  CONSTRAINT fk_pedido_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL,
  CONSTRAINT ck_pedido_cp       CHECK (REGEXP_LIKE(envio_cp, '^[0-9]{5}$')),
  CONSTRAINT ck_pedido_email    CHECK (cliente_email LIKE '%_@_%._%'),
  CONSTRAINT ck_pedido_importes CHECK (subtotal >= 0 AND gastos_envio >= 0),
  CONSTRAINT ck_pedido_recogida CHECK (modalidad_entrega = 'domicilio' OR gastos_envio = 0)
) ENGINE=InnoDB;

-- Copia histórica de cada artículo (nombre, opción y precio del momento).
CREATE TABLE pedido_lineas (
  id              INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  pedido_id       INT UNSIGNED NOT NULL,
  producto_id     INT UNSIGNED NULL,                           -- NULL si el producto se borra
  opcion_id       INT UNSIGNED NULL,
  nombre_producto VARCHAR(150) NOT NULL,
  opcion          VARCHAR(40)  NOT NULL DEFAULT '',            -- "Opción/Talla" del recibo
  precio_unitario DECIMAL(8,2) NOT NULL,
  cantidad        SMALLINT UNSIGNED NOT NULL,
  importe         DECIMAL(10,2) AS (precio_unitario * cantidad) STORED,
  KEY ix_pl_pedido (pedido_id),
  CONSTRAINT fk_pl_pedido   FOREIGN KEY (pedido_id)   REFERENCES pedidos(id) ON DELETE CASCADE,
  CONSTRAINT fk_pl_producto FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE SET NULL,
  CONSTRAINT fk_pl_opcion   FOREIGN KEY (opcion_id)   REFERENCES producto_opciones(id) ON DELETE SET NULL,
  CONSTRAINT ck_pl_cantidad CHECK (cantidad BETWEEN 1 AND 99),
  CONSTRAINT ck_pl_precio   CHECK (precio_unitario >= 0)
) ENGINE=InnoDB;

-- cliente/PedidoDevolucion.html (solo pedidos entregados; una por pedido)
CREATE TABLE devoluciones (
  id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  pedido_id   INT UNSIGNED NOT NULL,
  motivo      ENUM('Talla incorrecta','Producto defectuoso','Producto equivocado','Otro motivo') NOT NULL,
  comentarios VARCHAR(1000) NOT NULL DEFAULT '',
  creado_en   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_devolucion_pedido (pedido_id),
  CONSTRAINT fk_dev_pedido FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE devolucion_lineas (
  devolucion_id   INT UNSIGNED NOT NULL,
  pedido_linea_id INT UNSIGNED NOT NULL,
  PRIMARY KEY (devolucion_id, pedido_linea_id),
  CONSTRAINT fk_dl_devolucion FOREIGN KEY (devolucion_id)   REFERENCES devoluciones(id) ON DELETE CASCADE,
  CONSTRAINT fk_dl_linea      FOREIGN KEY (pedido_linea_id) REFERENCES pedido_lineas(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- =====================================================================
-- 5. CANCIONERO Y MULTIMEDIA
-- =====================================================================

-- Filtro "Todos los géneros" de Repertorio.html
CREATE TABLE generos (
  id     TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  UNIQUE KEY uq_genero (nombre)
) ENGINE=InnoDB;

CREATE TABLE albumes (
  id          SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  titulo      VARCHAR(150) NOT NULL,
  anio        YEAR NULL,
  portada_url VARCHAR(255) NULL,
  spotify_url VARCHAR(255) NULL,
  UNIQUE KEY uq_album (titulo)
) ENGINE=InnoDB;

-- Repertorio.html (tabla Canción · Autor · Género), reproductor del
-- Cancionero (título, álbum, duración, letra) y Spotify.html.
CREATE TABLE canciones (
  id             INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  titulo         VARCHAR(150) NOT NULL,
  autor          VARCHAR(150) NOT NULL DEFAULT 'Tradicional',
  genero_id      TINYINT UNSIGNED NOT NULL,
  album_id       SMALLINT UNSIGNED NULL,
  duracion_seg   SMALLINT UNSIGNED NULL,
  letra          TEXT NULL,
  audio_url      VARCHAR(255) NULL,
  spotify_url    VARCHAR(255) NULL,
  en_reproductor BOOLEAN NOT NULL DEFAULT FALSE,               -- aparece en la lista del reproductor
  orden          SMALLINT NOT NULL DEFAULT 0,
  KEY ix_cancion_genero (genero_id),
  KEY ix_cancion_album (album_id),
  FULLTEXT KEY ft_cancion (titulo, autor, letra),              -- "Busca por título o palabra clave"
  CONSTRAINT fk_cancion_genero FOREIGN KEY (genero_id) REFERENCES generos(id),
  CONSTRAINT fk_cancion_album  FOREIGN KEY (album_id)  REFERENCES albumes(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Certamenes.html y admin/Certamen*.html (nombre, fecha, lugar, cartel, premios)
CREATE TABLE certamenes (
  id         SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre     VARCHAR(150) NOT NULL,
  fecha      DATE NOT NULL,
  lugar      VARCHAR(100) NOT NULL,
  premios    VARCHAR(500) NULL,
  cartel_url VARCHAR(255) NULL,
  UNIQUE KEY uq_certamen (nombre, fecha),
  KEY ix_certamen_fecha (fecha)
) ENGINE=InnoDB;

-- Fotos.html, Videos.html y galerías de cada certamen
CREATE TABLE multimedia (
  id            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  tipo          ENUM('foto','video') NOT NULL,
  titulo        VARCHAR(150) NOT NULL,
  descripcion   VARCHAR(500) NULL,
  archivo_url   VARCHAR(255) NOT NULL,
  miniatura_url VARCHAR(255) NULL,
  duracion_seg  SMALLINT UNSIGNED NULL,                        -- solo vídeos
  fecha         DATE NOT NULL,
  certamen_id   SMALLINT UNSIGNED NULL,
  oficial       BOOLEAN NOT NULL DEFAULT FALSE,                -- sello "OFICIAL"
  destacado     BOOLEAN NOT NULL DEFAULT FALSE,                -- vídeo principal / mejores momentos
  publicado     BOOLEAN NOT NULL DEFAULT TRUE,
  KEY ix_mm_tipo_fecha (tipo, fecha),
  KEY ix_mm_certamen (certamen_id),
  CONSTRAINT fk_mm_certamen  FOREIGN KEY (certamen_id) REFERENCES certamenes(id) ON DELETE SET NULL,
  CONSTRAINT ck_mm_duracion  CHECK (tipo = 'video' OR duracion_seg IS NULL)
) ENGINE=InnoDB;

-- =====================================================================
-- 6. SITIO: portada, historia y configuración
-- =====================================================================

-- Portada: "Noticias y novedades de la tuna"
CREATE TABLE noticias (
  id         SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  categoria  ENUM('Certámenes','Captación','Discografía','Actuaciones','General') NOT NULL DEFAULT 'General',
  titulo     VARCHAR(150) NOT NULL,
  resumen    VARCHAR(500) NOT NULL,
  enlace     VARCHAR(255) NULL,
  enlace_texto VARCHAR(60) NULL,
  fecha      DATE NOT NULL,
  publicada  BOOLEAN NOT NULL DEFAULT TRUE,
  KEY ix_noticia_fecha (fecha)
) ENGINE=InnoDB;

-- Historia.html: línea de tiempo
CREATE TABLE hitos_historia (
  id     SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  anio   YEAR NOT NULL,
  titulo VARCHAR(150) NOT NULL,
  KEY ix_hito_anio (anio)
) ENGINE=InnoDB;

-- Datos sueltos: teléfono, redes, IBAN, envío, tarifas del presupuesto...
CREATE TABLE configuracion (
  clave VARCHAR(50) PRIMARY KEY,
  valor TEXT NOT NULL
) ENGINE=InnoDB;

-- =====================================================================
-- LÓGICA: funciones, triggers, procedimientos
-- =====================================================================
DELIMITER //

-- Valor numérico de la tabla configuracion
CREATE FUNCTION fn_config_num(p_clave VARCHAR(50)) RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN
  RETURN (SELECT CAST(valor AS DECIMAL(10,2)) FROM configuracion WHERE clave = p_clave);
END//

-- Gastos de envío de cart.js: gratis con recogida o si el subtotal supera 40 €
CREATE FUNCTION fn_gastos_envio(p_subtotal DECIMAL(10,2), p_modalidad VARCHAR(10)) RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN
  IF p_modalidad = 'recogida' OR p_subtotal > fn_config_num('envio_gratis_desde') THEN
    RETURN 0;
  END IF;
  RETURN fn_config_num('envio_tarifa');
END//

-- Presupuesto de TunaForms.calculateQuote():
-- tarifa base + 70 €/hora extra + 25 €/músico por encima de 4 + 50 € de desplazamiento
CREATE FUNCTION fn_presupuesto(p_tipo_evento_id TINYINT UNSIGNED, p_horas TINYINT UNSIGNED,
                               p_musicos TINYINT UNSIGNED, p_desplazamiento BOOLEAN) RETURNS DECIMAL(8,2)
READS SQL DATA
BEGIN
  DECLARE v_base DECIMAL(8,2) DEFAULT NULL;
  SET v_base = (SELECT tarifa_base FROM tipos_evento WHERE id = p_tipo_evento_id);
  IF v_base IS NULL THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de evento no válido';
  END IF;
  RETURN v_base
       + (GREATEST(p_horas, 1) - 1) * fn_config_num('presupuesto_hora_extra')
       + GREATEST(CAST(p_musicos AS SIGNED) - fn_config_num('presupuesto_musicos_incluidos'), 0) * fn_config_num('presupuesto_musico_extra')
       + IF(p_desplazamiento, fn_config_num('presupuesto_desplazamiento'), 0);
END//

-- Siguiente código con formato PREFIJO-AÑO-NN (CTR-2026-05, PED-2026-082)
CREATE FUNCTION fn_siguiente_codigo(p_ultimo INT UNSIGNED, p_prefijo VARCHAR(5), p_anio INT, p_cifras TINYINT)
RETURNS VARCHAR(20) DETERMINISTIC
BEGIN
  DECLARE n INT UNSIGNED DEFAULT IFNULL(p_ultimo, 0) + 1;
  RETURN CONCAT(p_prefijo, '-', p_anio, '-', LPAD(n, GREATEST(p_cifras, CHAR_LENGTH(n)), '0'));
END//

-- ---------------------------------------------------------------- contratos
CREATE TRIGGER trg_contratos_bi BEFORE INSERT ON contratos
FOR EACH ROW
BEGIN
  DECLARE v_anio INT DEFAULT YEAR(IF(NEW.creado_en IS NULL OR NEW.creado_en < '2000-01-01', NOW(), NEW.creado_en));

  IF NEW.codigo IS NULL OR NEW.codigo = '' THEN
    SET NEW.codigo = fn_siguiente_codigo(
          (SELECT MAX(CAST(SUBSTRING_INDEX(codigo, '-', -1) AS UNSIGNED)) FROM contratos
            WHERE codigo LIKE CONCAT('CTR-', v_anio, '-%')),
          'CTR', v_anio, 2);
  END IF;

  IF NEW.evento IS NULL OR NEW.evento = '' THEN
    SET NEW.evento = (SELECT nombre FROM tipos_evento WHERE id = NEW.tipo_evento_id);
  END IF;

  -- Copia del contacto desde la cuenta si no se envía
  IF NEW.usuario_id IS NOT NULL THEN
    IF NEW.contacto_nombre IS NULL OR NEW.contacto_nombre = '' THEN
      SET NEW.contacto_nombre = (SELECT TRIM(CONCAT(nombre, ' ', apellidos)) FROM usuarios WHERE id = NEW.usuario_id);
    END IF;
    IF NEW.contacto_email IS NULL OR NEW.contacto_email = '' THEN
      SET NEW.contacto_email = (SELECT email FROM usuarios WHERE id = NEW.usuario_id);
    END IF;
    IF NEW.contacto_telefono IS NULL THEN
      SET NEW.contacto_telefono = (SELECT telefono FROM usuarios WHERE id = NEW.usuario_id);
    END IF;
  END IF;
  IF IFNULL(NEW.contacto_nombre, '') = '' OR IFNULL(NEW.contacto_email, '') = '' THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Faltan el nombre o el correo de contacto del contrato';
  END IF;
END//

-- ------------------------------------------------------------------ pedidos
CREATE TRIGGER trg_pedidos_bi BEFORE INSERT ON pedidos
FOR EACH ROW
BEGIN
  DECLARE v_anio INT DEFAULT YEAR(IF(NEW.creado_en IS NULL OR NEW.creado_en < '2000-01-01', NOW(), NEW.creado_en));

  IF NEW.codigo IS NULL OR NEW.codigo = '' THEN
    SET NEW.codigo = fn_siguiente_codigo(
          (SELECT MAX(CAST(SUBSTRING_INDEX(codigo, '-', -1) AS UNSIGNED)) FROM pedidos
            WHERE codigo LIKE CONCAT('PED-', v_anio, '-%')),
          'PED', v_anio, 3);
  END IF;
END//

-- cliente/PedidoEditar.html: la dirección solo se cambia en 'Pendiente' o 'En preparación'
CREATE TRIGGER trg_pedidos_bu BEFORE UPDATE ON pedidos
FOR EACH ROW
BEGIN
  IF OLD.estado NOT IN ('Pendiente','En preparación') AND NOT (
         NEW.envio_destinatario <=> OLD.envio_destinatario AND NEW.envio_telefono <=> OLD.envio_telefono
     AND NEW.envio_direccion <=> OLD.envio_direccion       AND NEW.envio_cp <=> OLD.envio_cp
     AND NEW.envio_ciudad <=> OLD.envio_ciudad             AND NEW.envio_provincia <=> OLD.envio_provincia) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El pedido ya no se puede editar';
  END IF;
END//

-- Al marcar un pedido como 'Devuelto' se repone el stock de las líneas
-- devueltas (o de todas, si el administrador lo marca sin solicitud).
CREATE TRIGGER trg_pedidos_au AFTER UPDATE ON pedidos
FOR EACH ROW
BEGIN
  IF NEW.estado = 'Devuelto' AND OLD.estado <> 'Devuelto' THEN
    UPDATE producto_opciones o
       SET o.stock = o.stock + (
             SELECT SUM(l.cantidad) FROM pedido_lineas l
              WHERE l.pedido_id = NEW.id AND l.opcion_id = o.id
                AND (NOT EXISTS (SELECT 1 FROM devoluciones d WHERE d.pedido_id = NEW.id)
                     OR l.id IN (SELECT dl.pedido_linea_id FROM devolucion_lineas dl
                                   JOIN devoluciones d ON d.id = dl.devolucion_id
                                  WHERE d.pedido_id = NEW.id)))
     WHERE o.stock IS NOT NULL
       AND o.id IN (SELECT l2.opcion_id FROM pedido_lineas l2
                     WHERE l2.pedido_id = NEW.id AND l2.opcion_id IS NOT NULL
                       AND (NOT EXISTS (SELECT 1 FROM devoluciones d2 WHERE d2.pedido_id = NEW.id)
                            OR l2.id IN (SELECT dl2.pedido_linea_id FROM devolucion_lineas dl2
                                           JOIN devoluciones d3 ON d3.id = dl2.devolucion_id
                                          WHERE d3.pedido_id = NEW.id)));
  END IF;
END//

-- ------------------------------------------------------------ pedido_lineas
-- Comprueba y descuenta el stock de la opción elegida.
CREATE TRIGGER trg_pl_stock BEFORE INSERT ON pedido_lineas
FOR EACH ROW
BEGIN
  DECLARE v_stock INT DEFAULT NULL;
  DECLARE v_msg VARCHAR(255);
  IF NEW.opcion_id IS NOT NULL THEN
    SET v_stock = (SELECT IFNULL(stock, -1) FROM producto_opciones WHERE id = NEW.opcion_id FOR UPDATE);
    IF v_stock <> -1 THEN                                       -- -1 = stock ilimitado
      IF v_stock < NEW.cantidad THEN
        SET v_msg = CONCAT('Stock insuficiente de «', NEW.nombre_producto, '» (', NEW.opcion, '): quedan ', v_stock);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = v_msg;
      END IF;
      UPDATE producto_opciones SET stock = stock - NEW.cantidad WHERE id = NEW.opcion_id;
    END IF;
  END IF;
END//

-- ------------------------------------------------------------- devoluciones
CREATE TRIGGER trg_devoluciones_bi BEFORE INSERT ON devoluciones
FOR EACH ROW
BEGIN
  IF (SELECT estado FROM pedidos WHERE id = NEW.pedido_id) <> 'Entregado' THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Solo se pueden devolver pedidos entregados';
  END IF;
END//

CREATE TRIGGER trg_devoluciones_ai AFTER INSERT ON devoluciones
FOR EACH ROW
BEGIN
  UPDATE pedidos SET estado = 'Devolución solicitada' WHERE id = NEW.pedido_id;
END//

CREATE TRIGGER trg_devolucion_lineas_bi BEFORE INSERT ON devolucion_lineas
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pedido_lineas l JOIN devoluciones d ON d.pedido_id = l.pedido_id
                  WHERE l.id = NEW.pedido_linea_id AND d.id = NEW.devolucion_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La línea no pertenece al pedido de la devolución';
  END IF;
END//

-- ---------------------------------------------------------------------------
-- Formaliza un pedido (paso 4, TunaCart.submitCheckoutOrder) en una sola
-- transacción. Los precios salen de la base de datos, no del navegador.
--   p_usuario_id : NULL para compra como invitado (entonces p_cliente_* son obligatorios)
--   p_lineas     : la cesta, p. ej. '[{"producto":"prod-1","opcion":"M","cantidad":2}]'
--   p_metodo_pago: 'Tarjeta' | 'Bizum' | 'Transferencia'
-- Las transferencias quedan 'Pendiente' hasta verificar el ingreso.
-- ---------------------------------------------------------------------------
CREATE PROCEDURE sp_crear_pedido(
  IN  p_usuario_id       INT UNSIGNED,
  IN  p_cliente_nombre   VARCHAR(200),
  IN  p_cliente_email    VARCHAR(255),
  IN  p_cliente_telefono VARCHAR(20),
  IN  p_destinatario     VARCHAR(200),
  IN  p_envio_telefono   VARCHAR(20),
  IN  p_direccion        VARCHAR(200),
  IN  p_cp               CHAR(5),
  IN  p_ciudad           VARCHAR(100),
  IN  p_provincia        VARCHAR(100),
  IN  p_modalidad        VARCHAR(10),
  IN  p_notas            VARCHAR(500),
  IN  p_metodo_pago      VARCHAR(15),
  IN  p_lineas           JSON,
  OUT p_pedido_id        INT UNSIGNED,
  OUT p_codigo           VARCHAR(20))
BEGIN
  DECLARE v_nombre VARCHAR(200); DECLARE v_email VARCHAR(255); DECLARE v_tel VARCHAR(20);
  DECLARE v_pedidas INT; DECLARE v_validas INT; DECLARE v_sub DECIMAL(10,2);
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    DROP TEMPORARY TABLE IF EXISTS tmp_lineas;
    RESIGNAL;
  END;

  -- Datos de contacto: los de la cuenta, o los de la compra rápida
  SET v_nombre = p_cliente_nombre, v_email = p_cliente_email, v_tel = p_cliente_telefono;
  IF p_usuario_id IS NOT NULL THEN
    IF NOT EXISTS (SELECT 1 FROM usuarios WHERE id = p_usuario_id AND activo) THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Usuario no válido';
    END IF;
    SET v_nombre = IFNULL(v_nombre, (SELECT TRIM(CONCAT(nombre, ' ', apellidos)) FROM usuarios WHERE id = p_usuario_id)),
        v_email  = IFNULL(v_email,  (SELECT email    FROM usuarios WHERE id = p_usuario_id)),
        v_tel    = IFNULL(v_tel,    (SELECT telefono FROM usuarios WHERE id = p_usuario_id));
  END IF;
  IF v_nombre IS NULL OR v_email IS NULL OR v_tel IS NULL THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Faltan el nombre, el correo o el teléfono de contacto';
  END IF;

  -- La cesta se copia a una tabla temporal: el trigger trg_pl_stock actualiza
  -- producto_opciones y MySQL no deja hacerlo si la sentencia que lo dispara
  -- lee esa misma tabla (error 1442).
  DROP TEMPORARY TABLE IF EXISTS tmp_lineas;
  CREATE TEMPORARY TABLE tmp_lineas (
    producto_id INT UNSIGNED, opcion_id INT UNSIGNED, nombre VARCHAR(150),
    opcion VARCHAR(40), precio DECIMAL(8,2), cantidad INT);

  INSERT INTO tmp_lineas
  SELECT p.id, o.id, p.nombre, o.nombre, p.precio, j.cantidad
    FROM JSON_TABLE(p_lineas, '$[*]' COLUMNS (
           producto VARCHAR(20) PATH '$.producto',
           opcion   VARCHAR(40) PATH '$.opcion',
           cantidad INT         PATH '$.cantidad')) j
    JOIN productos p         ON p.codigo = j.producto COLLATE utf8mb4_spanish_ci AND p.activo
    JOIN producto_opciones o ON o.producto_id = p.id AND o.nombre = j.opcion COLLATE utf8mb4_spanish_ci;

  SET v_pedidas = IFNULL(JSON_LENGTH(p_lineas), 0);
  SET v_validas = (SELECT COUNT(*) FROM tmp_lineas),
      v_sub     = (SELECT SUM(precio * cantidad) FROM tmp_lineas);
  IF v_pedidas = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La cesta está vacía';
  END IF;
  IF v_validas <> v_pedidas THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Algún producto u opción de la cesta ya no está disponible';
  END IF;

  START TRANSACTION;
  INSERT INTO pedidos (usuario_id, cliente_nombre, cliente_email, cliente_telefono,
                       envio_destinatario, envio_telefono, envio_direccion, envio_cp, envio_ciudad, envio_provincia,
                       modalidad_entrega, notas_entrega, metodo_pago, subtotal, gastos_envio, estado)
  VALUES (p_usuario_id, v_nombre, v_email, v_tel,
          p_destinatario, p_envio_telefono, p_direccion, p_cp, p_ciudad, p_provincia,
          p_modalidad, NULLIF(p_notas, ''), p_metodo_pago, v_sub, fn_gastos_envio(v_sub, p_modalidad),
          IF(p_metodo_pago = 'Transferencia', 'Pendiente', 'En preparación'));
  SET p_pedido_id = LAST_INSERT_ID();

  -- trg_pl_stock comprueba y descuenta el stock de cada línea
  INSERT INTO pedido_lineas (pedido_id, producto_id, opcion_id, nombre_producto, opcion, precio_unitario, cantidad)
  SELECT p_pedido_id, producto_id, opcion_id, nombre, opcion, precio, cantidad FROM tmp_lineas;

  -- Se guarda la dirección en la cuenta para el siguiente pedido
  IF p_usuario_id IS NOT NULL THEN
    UPDATE usuarios SET direccion = p_direccion, ciudad = p_ciudad, codigo_postal = p_cp, provincia = p_provincia
     WHERE id = p_usuario_id AND direccion IS NULL;
  END IF;

  SET p_codigo = (SELECT codigo FROM pedidos WHERE id = p_pedido_id);
  COMMIT;
  DROP TEMPORARY TABLE tmp_lineas;
END//

-- cliente/PedidoDevolucion.html: p_lineas = '[12, 13]' (ids de pedido_lineas)
CREATE PROCEDURE sp_solicitar_devolucion(
  IN p_usuario_id INT UNSIGNED, IN p_codigo_pedido VARCHAR(20),
  IN p_motivo VARCHAR(30), IN p_comentarios VARCHAR(1000), IN p_lineas JSON)
BEGIN
  DECLARE v_pedido INT UNSIGNED DEFAULT NULL;
  DECLARE v_dev INT UNSIGNED;
  DECLARE EXIT HANDLER FOR SQLEXCEPTION BEGIN ROLLBACK; RESIGNAL; END;

  SET v_pedido = (SELECT id FROM pedidos WHERE codigo = p_codigo_pedido AND usuario_id = p_usuario_id);
  IF v_pedido IS NULL THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Este pedido no existe o no pertenece a tu cuenta.';
  END IF;
  IF IFNULL(JSON_LENGTH(p_lineas), 0) = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Selecciona al menos un producto y el motivo.';
  END IF;

  START TRANSACTION;
  INSERT INTO devoluciones (pedido_id, motivo, comentarios) VALUES (v_pedido, p_motivo, IFNULL(p_comentarios, ''));
  SET v_dev = LAST_INSERT_ID();
  INSERT INTO devolucion_lineas (devolucion_id, pedido_linea_id)
  SELECT DISTINCT v_dev, j.linea FROM JSON_TABLE(p_lineas, '$[*]' COLUMNS (linea INT UNSIGNED PATH '$')) j;
  COMMIT;
END//

DELIMITER ;

-- =====================================================================
-- VISTAS (lo que pinta cada pantalla)
-- =====================================================================

-- Catalogo.html: data-cat, data-price, data-stock y las opciones "S|M|L|XL"
-- que recibe selectCatalogProduct().
CREATE VIEW v_catalogo AS
SELECT p.id, p.codigo, p.nombre, p.descripcion, c.slug AS categoria, c.nombre AS categoria_nombre,
       p.precio, p.precio_anterior,
       IF(p.precio_anterior IS NULL, NULL, ROUND(100 - p.precio * 100 / p.precio_anterior)) AS descuento_pct,
       p.imagen_url, p.etiqueta, p.valoracion, p.num_valoraciones,
       p.en_catalogo, p.destacado_portada, p.orden,
       GROUP_CONCAT(o.nombre ORDER BY o.orden, o.id SEPARATOR '|') AS opciones,
       IF(SUM(o.stock IS NULL) > 0, NULL, SUM(o.stock))              AS stock_total,  -- NULL = sin límite
       (SUM(o.stock IS NULL) > 0 OR SUM(o.stock) > 0)                AS en_stock
  FROM productos p
  JOIN categorias_producto c ON c.id = p.categoria_id
  LEFT JOIN producto_opciones o ON o.producto_id = p.id
 WHERE p.activo
 GROUP BY p.id, c.id;

-- Listados de pedidos (cliente/Pedidos, admin/Pedidos): la dirección en una
-- sola línea, como la guarda el prototipo ("calle, 04001 Ciudad")
CREATE VIEW v_pedidos AS
SELECT pe.id, pe.codigo, pe.usuario_id,
       IFNULL(TRIM(CONCAT(u.nombre, ' ', u.apellidos)), pe.cliente_nombre) AS cliente,
       pe.cliente_email, DATE(pe.creado_en) AS fecha,
       CONCAT(pe.envio_direccion, ', ', pe.envio_cp, ' ', pe.envio_ciudad) AS direccion,
       pe.modalidad_entrega, pe.metodo_pago, pe.subtotal, pe.gastos_envio, pe.total, pe.estado,
       (SELECT SUM(l.cantidad) FROM pedido_lineas l WHERE l.pedido_id = pe.id) AS num_articulos
  FROM pedidos pe
  LEFT JOIN usuarios u ON u.id = pe.usuario_id;

-- Listados de contratos (cliente/Contratos, admin/Contratos)
CREATE VIEW v_contratos AS
SELECT co.id, co.codigo, co.usuario_id,
       IFNULL(TRIM(CONCAT(u.nombre, ' ', u.apellidos)), co.contacto_nombre) AS cliente,
       co.evento, t.nombre AS tipo_evento, co.fecha, co.hora, co.lugar, co.asistentes,
       co.horas, co.musicos, co.observaciones,
       IFNULL(CONCAT(FORMAT(co.presupuesto, 2, 'es_ES'), ' €'), 'A convenir') AS presupuesto_texto,
       co.presupuesto, co.estado, co.creado_en
  FROM contratos co
  JOIN tipos_evento t ON t.id = co.tipo_evento_id
  LEFT JOIN usuarios u ON u.id = co.usuario_id;

-- admin/Clientes.html: cartera con número de contratos y pedidos
CREATE VIEW v_clientes AS
SELECT u.id, TRIM(CONCAT(u.nombre, ' ', u.apellidos)) AS nombre_completo, u.email, u.telefono,
       DATE(u.fecha_registro) AS cliente_desde,
       (SELECT COUNT(*) FROM contratos c WHERE c.usuario_id = u.id) AS num_contratos,
       (SELECT COUNT(*) FROM pedidos p   WHERE p.usuario_id = u.id) AS num_pedidos
  FROM usuarios u
 WHERE u.rol = 'cliente' AND u.activo;

-- admin/index.html: tarjetas de resumen
CREATE VIEW v_admin_resumen AS
SELECT
  (SELECT COUNT(*) FROM contratos WHERE estado = 'Pendiente')                         AS contratos_pendientes,
  (SELECT COUNT(*) FROM pedidos   WHERE estado IN ('Pendiente','En preparación'))      AS pedidos_pendientes,
  (SELECT IFNULL(SUM(total), 0) FROM pedidos
    WHERE estado <> 'Devuelto' AND creado_en >= DATE_FORMAT(CURDATE(), '%Y-%m-01'))   AS ventas_tienda_mes,
  (SELECT IFNULL(SUM(presupuesto), 0) FROM contratos
    WHERE estado IN ('Confirmado','Realizado')
      AND fecha >= DATE_FORMAT(CURDATE(), '%Y-%m-01')
      AND fecha <  DATE_FORMAT(CURDATE(), '%Y-%m-01') + INTERVAL 1 MONTH)            AS ingresos_contratos_mes,
  (SELECT COUNT(*) FROM usuarios
    WHERE rol = 'cliente' AND fecha_registro >= DATE_FORMAT(CURDATE(), '%Y-%m-01'))   AS clientes_nuevos_mes;

-- admin/index.html: gráficas de los últimos 12 meses
CREATE VIEW v_admin_contratos_mes AS
SELECT DATE_FORMAT(creado_en, '%Y-%m') AS mes, COUNT(*) AS contratos
  FROM contratos
 WHERE creado_en >= DATE_FORMAT(CURDATE(), '%Y-%m-01') - INTERVAL 11 MONTH
 GROUP BY DATE_FORMAT(creado_en, '%Y-%m');

CREATE VIEW v_admin_ventas_mes AS
SELECT DATE_FORMAT(creado_en, '%Y-%m') AS mes, COUNT(*) AS pedidos, SUM(total) AS ventas
  FROM pedidos
 WHERE estado <> 'Devuelto'
   AND creado_en >= DATE_FORMAT(CURDATE(), '%Y-%m-01') - INTERVAL 11 MONTH
 GROUP BY DATE_FORMAT(creado_en, '%Y-%m');

-- Miembros.html y admin/MiembrosGestion.html
CREATE VIEW v_miembros AS
SELECT m.id, m.nombre, i.nombre AS instrumento, m.anio_ingreso, m.foto_url, m.biografia, m.orden
  FROM miembros m JOIN instrumentos i ON i.id = m.instrumento_id
 WHERE m.activo;

-- Repertorio.html y reproductor del Cancionero
CREATE VIEW v_repertorio AS
SELECT c.id, c.titulo, c.autor, g.nombre AS genero, a.titulo AS album,
       c.duracion_seg, CONCAT(c.duracion_seg DIV 60, ':', LPAD(c.duracion_seg MOD 60, 2, '0')) AS duracion,
       c.letra, c.audio_url, c.spotify_url, c.en_reproductor, c.orden
  FROM canciones c
  JOIN generos g ON g.id = c.genero_id
  LEFT JOIN albumes a ON a.id = c.album_id;

-- =====================================================================
-- DATOS INICIALES (los mismos que muestra el prototipo)
-- =====================================================================

INSERT INTO configuracion (clave, valor) VALUES
 ('nombre_tuna',                  'Tuna de la Facultad de Derecho de Almería'),
 ('anio_fundacion',               '1993'),
 ('galardones',                   '18'),
 ('telefono',                     '685 99 55 10'),
 ('whatsapp_url',                 'https://wa.me/34685995510'),
 ('instagram_url',                'https://instagram.com/tunaderechoalmeria'),
 ('spotify_usuario',              '@tunaderechoalmeria'),
 ('spotify_oyentes_mensuales',    '12400'),
 ('bizum_telefono',               '685 99 55 10'),
 ('iban',                         'ES91 2100 0418 4502 0001 2345'),
 ('envio_tarifa',                 '4.50'),
 ('envio_gratis_desde',           '40.00'),
 ('presupuesto_hora_extra',       '70'),
 ('presupuesto_musicos_incluidos','4'),
 ('presupuesto_musico_extra',     '25'),
 ('presupuesto_desplazamiento',   '50'),
 ('historia_texto',               'La Tuna de la Facultad de Derecho de Almería fue fundada en el verano de 1993 por un entusiasta grupo de estudiantes de la recién creada Universidad de Almería, con el anhelo de llevar por bandera la tradición musical, la galantería y el espíritu festivo universitario.');

-- ------------------------------------------------------------------ cuentas
-- Contraseñas de prueba (hash bcrypt real): clientes «cliente123», admin «admin123»
INSERT INTO usuarios (id, email, password_hash, rol, nombre, apellidos, telefono, direccion, ciudad, codigo_postal, provincia, fecha_registro, privacidad_aceptada_en) VALUES
 (1,'marta.gil@ual.es',      '$2y$10$nSb4k93gxy.gOqmtp4GKKuW3XqogOOzF3V2bePJ5Q3MUvNtaneSqG','cliente','Marta','Gil Navarro',    '600 123 456','Calle de la Reina, 14, 2ºA', 'Almería','04001','Almería','2026-01-15','2026-01-15'),
 (2,'admin@derechoual.es',   '$2y$10$DiTokHFiq3f1k9j52pbLnO3.OFs0SKVTgcxtFutLlO7b81n0hAaJu','admin',  'Maese','Tuno Mayor',     '685 99 55 10','Edificio CAE, Campus UAL',   'Almería','04120','Almería','2024-09-01','2024-09-01'),
 (3,'carlos.ruiz@ual.es',    '$2y$10$nSb4k93gxy.gOqmtp4GKKuW3XqogOOzF3V2bePJ5Q3MUvNtaneSqG','cliente','Carlos','Ruiz Sánchez',   '600 234 567','Avenida de la Estación, 8',  'Almería','04005','Almería','2026-02-03','2026-02-03'),
 (4,'lucia.fernandez@ual.es','$2y$10$nSb4k93gxy.gOqmtp4GKKuW3XqogOOzF3V2bePJ5Q3MUvNtaneSqG','cliente','Lucía','Fernández Mora', '600 345 678','Calle Murcia, 21',           'Almería','04004','Almería','2026-03-20','2026-03-20');

-- ----------------------------------------------------------------- la tuna
INSERT INTO instrumentos (id, nombre, orden) VALUES
 (1,'Guitarra',1),(2,'Bandurria',2),(3,'Laúd',3),(4,'Pandero',4),(5,'Acordeón',5),(6,'Voz',6),(7,'Otro',7);

INSERT INTO miembros (nombre, instrumento_id, anio_ingreso, foto_url, biografia, orden) VALUES
 ('Álvaro Ramos', 1, 2019, '../assets/img/galeria_barco_almeria.jpg',
  'Toca desde los 12 años y se unió a la tuna en su primer curso de universidad.', 1),
 ('Daniel Cortés',2, 2021, '../assets/img/galeria_catedral_nocturna.jpg',   NULL, 2),
 ('Irene Vega',   3, 2022, '../assets/img/galeria_estandarte_valencia.jpg', NULL, 3),
 ('Hugo Santos',  4, 2023, '../assets/img/galeria_grupo_plaza.jpg',         NULL, 4),
 ('Nuria Lara',   5, 2024, '../assets/img/galeria_puente_nocturno.jpg',     NULL, 5),
 ('Diego Marín',  6, 2020, '../assets/img/galeria_ronda_nocturna.jpg',      NULL, 6);

INSERT INTO solicitudes_ingreso (nombre, email, telefono, instrumento_id, experiencia, privacidad_aceptada, creado_en) VALUES
 ('Pablo Úbeda Martín','pablo.ubeda@ual.es','611 222 333',1,'Cinco años de guitarra en el conservatorio.',TRUE,'2026-10-02 18:30');

INSERT INTO locales_ensayo (id, nombre, direccion, ciudad, edificio) VALUES
 (1,'Local de ensayo','Calle del Ensayo 5','Almería','Edificio CAE · Universidad de Almería');
INSERT INTO horarios_ensayo (local_id, dia_semana, hora_inicio, hora_fin) VALUES
 (1,2,'20:00','22:00'),   -- martes
 (1,4,'19:00','21:00');   -- jueves

INSERT INTO hitos_historia (anio, titulo) VALUES
 (1993,'Fundación de la tuna'),
 (2004,'Primer certamen nacional'),
 (2012,'Gira internacional'),
 (2019,'Nuevo local de ensayo');

-- ------------------------------------------------------------ contratación
INSERT INTO tipos_evento (id, slug, nombre, tarifa_base, orden) VALUES
 (1,'serenata', 'Serenata Romántica',           180.00,1),
 (2,'boda',     'Boda y Recepción',             220.00,2),
 (3,'privado',  'Evento Privado / Celebración', 180.00,3),
 (4,'certamen', 'Certamen o Festival',          300.00,4),
 (5,'academico','Acto Académico Institucional', 200.00,5);

INSERT INTO servicios (nombre, descripcion, orden) VALUES
 ('Ronda por tu barrio',    'Ronda por las calles de tu localidad con nuestro repertorio tradicional.',1),
 ('Actuación en eventos',   'Actuación completa para bodas, cumpleaños y celebraciones.',2),
 ('Serenata personalizada', 'Música en directo para eventos de empresa y fiestas privadas.',3);

INSERT INTO contratos (codigo, usuario_id, tipo_evento_id, evento, fecha, hora, lugar, asistentes, horas, musicos, observaciones, estado, creado_en) VALUES
 ('CTR-2026-01',1,2,'Boda y Serenata',     '2026-05-18','21:00','Hotel Catedral Almería',            120,2, 8,'Recepción en cóctel y serenata bajo balcón.','Realizado', '2026-01-20 10:15'),
 ('CTR-2026-02',1,1,'Serenata Aniversario','2027-03-20','22:30','Casco Histórico Almería',            30,1, 6,'Ronda sorpresa.',                            'Pendiente', '2026-10-05 17:40'),
 ('CTR-2026-03',3,3,'Cumpleaños',          '2027-01-16','20:00','Finca Los Olivos, Viator',           60,1, 6,'Entrada por sorpresa durante la cena.',      'Confirmado','2026-09-12 12:00'),
 ('CTR-2026-04',4,3,'Evento de empresa',   '2027-02-12','19:00','Auditorio Maestro Padilla, Almería',150,2,10,'',                                           'Pendiente', '2026-11-02 09:30');

INSERT INTO actuaciones (titulo, lugar, fecha, hora) VALUES
 ('Ronda en el Casco Histórico de Almería','Plaza de la Catedral',     '2026-11-14','21:30'),
 ('Boda Privada Palacio de Congresos',     'Cabo de Gata',             '2026-11-22','19:00'),
 ('Certamen Internacional de Tunas',       'Auditorio Maestro Padilla','2026-12-05','20:00');

-- ------------------------------------------------------------------ tienda
INSERT INTO categorias_producto (id, slug, nombre, descripcion, orden) VALUES
 (1,'indumentaria','Indumentaria & Capas', 'Capas, sudaderas, camisetas',1),
 (2,'musica',      'Música & Discos',      'CDs oficiales, cancioneros',2),
 (3,'instrumentos','Instrumentos & Cintas','Panderetas, cintas bordadas',3),
 (4,'recuerdos',   'Recuerdos & Souvenirs','Parches bordados, regalos',4);

INSERT INTO productos (id, codigo, nombre, descripcion, categoria_id, precio, precio_anterior, imagen_url, etiqueta, valoracion, num_valoraciones, en_catalogo, destacado_portada, orden) VALUES
 (1,'prod-1','Capa tradicional de paño',
  'Confeccionada en paño negro de máxima calidad con forro interior rojo púrpura de la Facultad de Derecho. Incluye tirantes de sujeción reforzados y espacio preparado para cintas.',
  1,25.00,32.00,'../assets/img/prod_capa.jpg','TOP VENTAS',4.9,42,TRUE,TRUE,1),
 (2,'prod-2','CD XXV Aniversario',
  'Grabación oficial conmemorativa del XXV Aniversario. 16 temas clásicos y piezas galardonadas en certámenes nacionales con libreto ilustrado de 20 páginas.',
  2,12.00,NULL,'../assets/img/prod_cd_vinilo.jpg','NUEVO',5.0,28,TRUE,FALSE,2),
 (3,'prod-3','Sudadera Derecho Almería',
  'Algodón orgánico 320g color granate institucional con el escudo bordado en hilo dorado y tipografía universitaria. Corte unisex con capucha ajustable.',
  1,28.00,35.00,'../assets/img/prod_sudadera.jpg','POPULAR',4.8,35,TRUE,TRUE,3),
 (4,'prod-4','Pandero decorado con cintas',
  'Pandereta de madera de haya con sonajas de latón y piel de cabra tensada a mano, decorada con cintas bicolores roja y amarilla de 80 cm.',
  3,18.00,NULL,'../assets/img/prod_pandero.jpg',NULL,4.7,19,TRUE,FALSE,4),
 (5,'prod-5','Parche oficial bordado UAL',
  'Emblema oficial de la Tuna de Derecho de Almería con hilo de oro y seda sobre fondo negro. Apto para coser en capa, jubón o mochila.',
  4,6.00,NULL,'../assets/img/prod_parche.jpg',NULL,4.9,53,TRUE,FALSE,5),
 (6,'prod-6','Camiseta de la tuna',
  'Camiseta 100% algodón suave de alta densidad con serigrafía del escudo de Derecho en el pecho y lema de la tuna en la espalda.',
  1,15.00,NULL,'../assets/img/prod_camiseta_escudo.jpg',NULL,4.6,22,TRUE,FALSE,6),
 (7,'prod-7','Cinta de colores',
  'Cinta de raso de 1 metro de longitud con orla dorada. Posibilidad de incluir dedicatoria personalizada bordada o estampada.',
  3,4.00,NULL,'../assets/img/prod_taza_cintas.jpg',NULL,4.9,64,TRUE,FALSE,7),
 (8,'prod-8','Cancionero impreso ilustrado',
  'Libro encuadernado de 140 páginas con acordes, tablaturas y letras de más de 80 canciones tradicionales de tuna, boleros y pasodobles.',
  2,12.00,NULL,'../assets/img/prod_cancionero.jpg',NULL,4.8,17,TRUE,FALSE,8),
 (9,'prod-oferta-1','Pack Conmemorativo XXV Aniversario',
  'Incluye CD doble en directo + cancionero completo encuadernado + insignia dorada de solapa de la Tuna.',
  2,22.50,30.00,'../assets/img/prod_cd_vinilo.jpg','OFERTA DESTACADA',NULL,0,FALSE,TRUE,0);

INSERT INTO producto_opciones (producto_id, nombre, stock, orden) VALUES
 (1,'S',4,1),(1,'M',6,2),(1,'L',5,3),(1,'XL',3,4),(1,'A medida',NULL,5),
 (2,'CD Físico',25,1),(2,'Edición Digipack',10,2),(2,'Descarga Digital FLAC',NULL,3),
 (3,'XS',2,1),(3,'S',5,2),(3,'M',8,3),(3,'L',8,4),(3,'XL',4,5),(3,'XXL',2,6),
 (4,'20 cm',5,1),(4,'25 cm (Estándar)',10,2),(4,'28 cm',4,3),
 (5,'8 cm redondo',40,1),(5,'10 cm escudo',30,2),
 (6,'S',6,1),(6,'M',10,2),(6,'L',10,3),(6,'XL',5,4),
 (7,'Rojo Derecho',50,1),(7,'Blanco Almería',50,2),(7,'Oro Gala',30,3),(7,'Multicolor',40,4),
 (8,'Edición Rústica',20,1),(8,'Edición Tapa Dura',8,2),
 (9,'Edición Especial',15,1);

-- Pedidos de ejemplo (cliente/Pedidos.html). Las líneas descuentan stock (trigger).
INSERT INTO pedidos (id, codigo, usuario_id, cliente_nombre, cliente_email, cliente_telefono,
                     envio_destinatario, envio_telefono, envio_direccion, envio_cp, envio_ciudad, envio_provincia,
                     modalidad_entrega, metodo_pago, subtotal, gastos_envio, estado, creado_en) VALUES
 (1,'PED-2026-081',1,'Marta Gil Navarro','marta.gil@ual.es','600 123 456',
  'Marta Gil Navarro','600 123 456','Calle de la Reina, 14, 2ºA','04001','Almería','Almería',
  'domicilio','Tarjeta',37.00,4.50,'En preparación','2026-04-10 11:20'),
 (2,'PED-2026-074',3,'Carlos Ruiz Sánchez','carlos.ruiz@ual.es','600 234 567',
  'Carlos Ruiz Sánchez','600 234 567','Avenida de la Estación, 8','04005','Almería','Almería',
  'domicilio','Bizum',28.00,4.50,'Enviado','2026-10-22 19:05'),
 (3,'PED-2026-052',4,'Lucía Fernández Mora','lucia.fernandez@ual.es','600 345 678',
  'Lucía Fernández Mora','600 345 678','Calle Murcia, 21','04004','Almería','Almería',
  'recogida','Transferencia',25.00,0.00,'Entregado','2026-09-02 13:45');

-- opcion_id según el orden de inserción de producto_opciones: 1 = Capa S,
-- 2 = Capa M, 6 = CD Físico, 12 = Sudadera L
INSERT INTO pedido_lineas (pedido_id, producto_id, opcion_id, nombre_producto, opcion, precio_unitario, cantidad) VALUES
 (1, 1,  2, 'Capa tradicional de paño', 'M',         25.00, 1),
 (1, 2,  6, 'CD XXV Aniversario',       'CD Físico', 12.00, 1),
 (2, 3, 12, 'Sudadera Derecho Almería', 'L',         28.00, 1),
 (3, 1,  1, 'Capa tradicional de paño', 'S',         25.00, 1);

-- -------------------------------------------------- cancionero y multimedia
INSERT INTO generos (id, nombre) VALUES (1,'Tradicional'),(2,'Pasodoble'),(3,'Balada'),(4,'Popular');

INSERT INTO albumes (id, titulo, spotify_url) VALUES
 (1,'Álbum Oficial XXV Aniversario','https://open.spotify.com/'),
 (2,'Clásicos de la Universidad',NULL),
 (3,'Himnos de Ronda Estudiantil',NULL),
 (4,'Pasodobles de Oro',NULL);

INSERT INTO canciones (titulo, autor, genero_id, album_id, duracion_seg, en_reproductor, orden, spotify_url, letra) VALUES
 ('Noche de Ronda en Almería','Tuna de Derecho de Almería',3,1,225,TRUE,1,'https://open.spotify.com/',
  'Noche de ronda, qué triste pasas,\nqué triste cruzas por mi balcón.\nNoche de ronda, cómo me hieres,\ncómo lastimas mi corazón...\n\nPor la Alcazaba baja la tuna,\ncantan sus voces bajo la luna,\ny entre las rejas de la Judería,\ndeja un suspiro por Almería.'),
 ('Clavelitos Tradicionales','Tradicional',1,2,170,TRUE,2,NULL,
  'Mocita dame el clavel,\ndame el clavel de tu boca,\nque para eso no hay que tener\nmucha vergüenza ni poca...\n\nClavelitos, clavelitos,\nclavelitos de mi corazón,\nyo te traigo clavelitos\ncolorados igual que un tizón.'),
 ('Fonseca (Triste y Sola)','Tradicional',1,3,195,TRUE,3,NULL,
  'Triste y sola, sola se queda Fonseca,\ntriste y llorosa queda la Universidad,\ny los libros, los libros se quedan mudos,\nlos tunos marchan a la ciudad...\n\nAdiós villa de Almería,\nadiós colegio mayor,\nque ya repican campanas,\nanunciando el nuevo amor.'),
 ('La Morena de mi Copla','Popular',4,4,210,TRUE,4,NULL,
  'Julio Romero de Torres pintó a la mujer morena,\ncon ojos de misterio y el alma llena de pena.\nPor las calles de Almería resuena la serenata,\nque los tunos con salero le cantan a la muchacha.'),
 ('Ay, Carmela',  'Popular',    2,NULL,NULL,FALSE,5,NULL,NULL),
 ('Cielito lindo','Tradicional',3,NULL,NULL,FALSE,6,NULL,NULL),
 ('Mi Almería',   'Tradicional',1,NULL,NULL,FALSE,7,NULL,NULL),
 ('Soy minero',   'Popular',    2,NULL,NULL,FALSE,8,NULL,NULL);

INSERT INTO certamenes (id, nombre, fecha, lugar, premios) VALUES
 (1,'Certamen Nacional de Tunas',   '2025-03-12','Almería','Mejor pandero y mejor tuna del certamen'),
 (2,'Festival de Primavera',        '2024-04-20','Granada',NULL),
 (3,'Certamen Ciudad Universitaria','2023-05-13','Murcia', NULL),
 (4,'Encuentro Internacional',      '2022-12-03','Madrid', NULL);

INSERT INTO multimedia (tipo, titulo, descripcion, archivo_url, miniatura_url, duracion_seg, fecha, certamen_id, oficial, destacado) VALUES
 -- Fotos.html
 ('foto','Actuación en el certamen de este año',NULL,'../assets/img/tuna_oficial_certamen.jpg',NULL,NULL,'2025-03-12',1,TRUE,TRUE),
 ('foto','Ensayo en el local',               NULL,'../assets/img/tuna_oficial_ensayo.jpg',  NULL,NULL,'2025-10-14',NULL,TRUE,FALSE),
 ('foto','Actuación en un evento',           NULL,'../assets/img/tuna_oficial_evento.jpg',  NULL,NULL,'2025-06-21',NULL,TRUE,FALSE),
 ('foto','Foto de grupo',                    NULL,'../assets/img/tuna_oficial_grupo.jpg',   NULL,NULL,'2025-09-30',NULL,TRUE,TRUE),
 ('foto','Ronda nocturna',                   NULL,'../assets/img/tuna_oficial_ronda.jpg',   NULL,NULL,'2025-05-03',NULL,TRUE,FALSE),
 -- Galerías de Certamenes.html
 ('foto','Actuación en el escenario',NULL,'../assets/img/galeria_actuacion_escenario.jpg',NULL,NULL,'2025-03-12',1,FALSE,FALSE),
 ('foto','En el auditorio',          NULL,'../assets/img/galeria_auditorio.jpg',          NULL,NULL,'2025-03-12',1,FALSE,FALSE),
 ('foto','Estandarte de la tuna',    NULL,'../assets/img/galeria_estandarte_valencia.jpg',NULL,NULL,'2024-04-20',2,FALSE,FALSE),
 ('foto','Bajo los arcos',           NULL,'../assets/img/galeria_arcos.jpg',              NULL,NULL,'2023-05-13',3,FALSE,FALSE),
 ('foto','Grupo en el césped',       NULL,'../assets/img/galeria_grupo_cesped.jpg',       NULL,NULL,'2022-12-03',4,FALSE,FALSE),
 -- Videos.html
 ('video','Certamen Nacional de Tunas 2025 - Actuación Completa',NULL,'/media/videos/certamen-nacional-2025.mp4','../assets/img/galeria_actuacion_escenario.jpg',255,'2025-03-12',1,TRUE,TRUE),
 ('video','Ronda en la plaza mayor','Un momento de la ronda de primavera frente al ayuntamiento.','/media/videos/ronda-plaza-mayor.mp4','../assets/img/galeria_ronda_nocturna.jpg',222,'2026-03-12',NULL,FALSE,FALSE),
 ('video','Certamen de tunas',      NULL,'/media/videos/certamen-tunas.mp4',     '../assets/img/galeria_auditorio.jpg',     310,'2026-02-28',NULL,FALSE,FALSE),
 ('video','Serenata de boda',       NULL,'/media/videos/serenata-boda.mp4',      '../assets/img/galeria_arcos.jpg',         178,'2026-01-15',NULL,FALSE,FALSE),
 ('video','Concierto de Navidad',   NULL,'/media/videos/concierto-navidad.mp4',  '../assets/img/galeria_barco_almeria.jpg', 261,'2025-12-03',NULL,FALSE,FALSE);

-- ------------------------------------------------------------------ portada
INSERT INTO noticias (categoria, titulo, resumen, enlace, enlace_texto, fecha) VALUES
 ('Certámenes','¡Primer Premio a la Mejor Tuna en el Certamen Nacional!',
  'La Tuna de Derecho de Almería se alzó con los galardones a Mejor Tuna y Mejor Bandurria en una noche mágica.',
  'Certamenes.html','Leer crónica del certamen','2026-10-12'),
 ('Captación','Abierta la convocatoria para nuevos aspirantes',
  'Si estudias en la Universidad de Almería y te apasiona la música, ven a nuestros ensayos en el Edificio CAE.',
  'Formulario.html','Unirse a la tuna','2026-09-28'),
 ('Discografía','Álbum conmemorativo disponible en la tienda',
  'Nuevo recopilatorio con las canciones más queridas de nuestra tuna, grabado en directo con sonido remasterizado.',
  'Repertorio.html','Escuchar repertorio','2026-09-15');
