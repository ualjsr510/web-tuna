-- ============================================================================
-- DATOS INICIALES (SEED DATA): TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
-- ============================================================================

-- 1. Cuentas de Usuarios
-- Contraseñas de prueba: 'cliente123' y 'admin123'
INSERT INTO usuarios (id, email, password_hash, rol, nombre, apellidos, telefono, direccion, ciudad, codigo_postal) VALUES
(1, 'marta.gil@ual.es', 'cliente123', 'cliente', 'Marta', 'Gil Navarro', '600 123 456', 'Calle de la Reina, 14, 2ºA', 'Almería', '04001'),
(2, 'admin@derechoual.es', 'admin123', 'admin', 'Maese', 'Tuno Mayor', '685 99 55 10', 'Edificio CAE, Campus Universidad de Almería', 'Almería', '04120'),
(3, 'colegio.abogados@almeria.es', 'cliente123', 'cliente', 'Ilustre Colegio', 'de la Abogacía de Almería', '950 234 567', 'Calle Álvarez de Castro, 27', 'Almería', '04002');

-- 2. Categorías de la Tienda
INSERT INTO categorias (id, nombre, slug, descripcion) VALUES
(1, 'Indumentaria', 'indumentaria', 'Capas de paño, sudaderas, camisetas y complementos de gala de la tuna'),
(2, 'Música', 'musica', 'Grabaciones discográficas en CD, vinilo y cancioneros impresos'),
(3, 'Instrumentos', 'instrumentos', 'Panderos afinados, laúdes, bandurrias y accesorios musicales'),
(4, 'Recuerdos', 'recuerdos', 'Parches bordados con hilo de oro, cintas de gala y recuerdos');

-- 3. Productos del Catálogo Oficial
INSERT INTO productos (id, codigo, categoria_id, nombre, precio, stock, imagen, tallas_disponibles, descripcion) VALUES
(1, 'IND-01', 1, 'Capa tradicional de paño', 25.00, 14, '../assets/img/prod_capa.jpg', 'S,M,L,XL', 'Capa negra tradicional confeccionada en paño de alta densidad con vivos y cuello en terciopelo rojo carmesí característico de la Facultad de Derecho. Incluye tiras de anclaje reforzadas.'),
(2, 'MUS-01', 2, 'CD XXV Aniversario', 12.00, 85, '../assets/img/prod_cd.jpg', 'Estándar,Edición Firmada', 'Álbum conmemorativo grabado en directo en el Teatro Cervantes de Almería. Incluye 16 temas emblemáticos como «Noche de Ronda», «Clavelitos» y «Almería Tierra Noble».'),
(3, 'IND-02', 1, 'Sudadera Derecho Almería', 28.00, 22, '../assets/img/prod_sudadera.jpg', 'S,M,L,XL,XXL', 'Sudadera de algodón 100% orgánico color granate con capucha y bolsillo canguro. Serigrafía oficial dorada de la Tuna de Derecho y la Universidad de Almería.'),
(4, 'INS-01', 3, 'Pandero decorado con cintas', 18.00, 8, '../assets/img/prod_pandero.jpg', 'Diámetro 25cm,Diámetro 30cm', 'Pandero artesanal de piel auténtica afinada con sonajas metálicas y juego de cintas multicolores de raso bordadas con versos tradicionales.'),
(5, 'REC-01', 4, 'Parche oficial bordado UAL', 6.00, 150, '../assets/img/prod_parche.jpg', 'Termoadhesivo (8cm)', 'Escudo oficial de la Tuna de Derecho bordado con hilo de oro y carmesí sobre fondo negro. Apto para coser o fijar con plancha en capas o mochilas.'),
(6, 'IND-03', 1, 'Camiseta de la tuna', 15.00, 40, '../assets/img/prod_camiseta.jpg', 'S,M,L,XL', 'Camiseta de manga corta 100% algodón prelavado con ilustración conmemorativa de la picaresca tunil almeriense y lema oficial.'),
(7, 'REC-02', 4, 'Cinta de colores', 4.00, 200, '../assets/img/prod_cintas.jpg', 'Longitud 1 metro,Longitud 1.5 metros', 'Cinta de raso de doble cara con orlas bordadas para prender en la capa. Disponible en colores representativos de ciudades y certámenes.'),
(8, 'MUS-02', 2, 'Cancionero impreso ilustrado', 12.00, 30, '../assets/img/prod_cancionero.jpg', 'Edición Tapa Blanda,Edición Coleccionista', 'Compendio musical de más de 60 páginas con partituras completas, acordes cifrados para guitarra y laúd, y letras históricas de rondas y pasodobles.');

-- 4. Pedidos Registrados
INSERT INTO pedidos (id, codigo_pedido, usuario_id, subtotal, gastos_envio, total, estado, direccion_envio, ciudad, codigo_postal, telefono_contacto) VALUES
(1, 'PED-2026-081', 1, 37.00, 4.50, 41.50, 'En preparación', 'Calle de la Reina, 14, 2ºA', 'Almería', '04001', '600 123 456'),
(2, 'PED-2026-042', 3, 96.00, 0.00, 96.00, 'Entregado', 'Calle Álvarez de Castro, 27', 'Almería', '04002', '950 234 567');

-- 5. Líneas de Pedido
INSERT INTO pedido_lineas (id, pedido_id, producto_id, cantidad, precio_unitario, talla) VALUES
(1, 1, 1, 1, 25.00, 'M'),
(2, 1, 2, 1, 12.00, 'Estándar'),
(3, 2, 2, 8, 12.00, 'Edición Firmada');

-- 6. Contratos de Actuaciones
INSERT INTO contratos (id, codigo_contrato, usuario_id, tipo_evento, fecha_evento, hora_evento, lugar, num_asistentes, duracion_horas, num_tunos, precio_total, estado, observaciones) VALUES
(1, 'CTR-2026-01', 1, 'Boda y Serenata', '2026-05-18', '21:00', 'Hotel Catedral Almería, Plaza de la Catedral', 120, 2, 8, 290.00, 'Confirmado', 'Recepción de invitados en cóctel y serenata a los novios con repertorio de boleros.'),
(2, 'CTR-2026-02', 3, 'Acto Académico San Raimundo', '2026-06-04', '19:30', 'Sede Ilustre Colegio de la Abogacía de Almería', 200, 2, 10, 350.00, 'Confirmado', 'Apertura y clausura solemne con Gaudeamus Igitur e himno universitario.'),
(3, 'CTR-2026-03', 1, 'Serenata Aniversario', '2026-06-21', '22:30', 'Casco Histórico Almería', 30, 1, 6, 180.00, 'Pendiente', 'Ronda bajo balcón para aniversario familiar.');

-- 7. Censo de Miembros de la Tuna
INSERT INTO miembros (id, mote, nombre_completo, instrumento, rango, fecha_ingreso, foto, biografia) VALUES
(1, 'Tuno Decano', 'Carlos Benítez', 'Guitarra', 'Tuno Mayor', '2014-10-01', '../assets/img/tuna_oficial_grupo.jpg', 'Fundador de la etapa contemporánea, coordina el repertorio instrumental y la dirección artística.'),
(2, 'Maese Solfa', 'Alejandro Morales', 'Laúd y Bandurria', 'Tuno', '2018-09-15', '../assets/img/tuna_oficial_certamen.jpg', 'Solista de cuerda y arreglista de los pasodobles tradicionales.'),
(3, 'Castañuela', 'Javier Ortiz', 'Pandereta y Percusión', 'Tuno', '2020-02-10', '../assets/img/tuna_oficial_ronda.jpg', 'Acróbata del pandero y animador de rondas de medianoche.'),
(4, 'Novicio', 'Pablo Ramos', 'Guitarra', 'Pardillo', '2025-10-10', '../assets/img/tuna_oficial_ensayo.jpg', 'Estudiante de 2º de Grado en Derecho, aspirante a vestir la beca roja en el próximo certamen.');

-- 8. Certámenes y Galardones Históricos
INSERT INTO certamenes (id, nombre, ciudad, ano, premio, descripcion) VALUES
(1, 'XXX Certamen Nacional de Tunas de Derecho', 'Granada', 2025, '1º Premio Mejor Tuna y Mejor Bandurria', 'Primer puesto absoluto entre 16 agrupaciones universitarias de toda España.'),
(2, 'Certamen Internacional Costa de Almería', 'Almería', 2024, 'Tuna Organizadora y Premio a la Tuna más Simpática', 'Encuentro anual en el Auditorio Maestro Padilla con más de 300 tunos participantes.'),
(3, 'XXIX Certamen de Tunas de Derecho', 'Salamanca', 2023, 'Premio Mejor Solista y Mejor Ronda', 'Destacada actuación en la Plaza Mayor de Salamanca.');

-- 9. Cancionero Oficial
INSERT INTO canciones (id, titulo, genero, duracion, letra, orden) VALUES
(1, 'Noche de Ronda en Almería', 'Bolero', '3:45', 'Noche de ronda, qué triste pasas...\nPor la Alcazaba baja la tuna cantando bajo la luna.', 1),
(2, 'Clavelitos Tradicionales', 'Pasodoble', '2:50', 'Mocita dame el clavel, dame el clavel de tu boca...\nClavelitos de mi corazón.', 2),
(3, 'Fonseca (Triste y Sola)', 'Himno', '3:15', 'Triste y sola, sola se queda Fonseca...\nLos tunos marchan a la ciudad.', 3),
(4, 'La Morena de mi Copla', 'Pasodoble', '3:30', 'Julio Romero de Torres pintó a la mujer morena...\nPor las calles de Almería resuena la serenata.', 4);

