# Tuna de la Facultad de Derecho de Almería · Portal Web Oficial

> **Asignatura:** Tecnologías Web (4º Curso - Grado en Ingeniería Informática)  
> **Universidad de Almería (UAL)**  
> **Año Académico:** 2026/2027

---

## Descripción del Proyecto

Portal web corporativo oficial para la **Tuna de la Facultad de Derecho de la Universidad de Almería** (fundada en 1993). El sistema implementa un diseño modular, responsive, conectado a base de datos relacional y con separación de tres áreas principales:

1. **Portal Público (Visitante):** Portada con fotografía oficial, cancionero con reproductor de audio, historia, miembros, certámenes, contratación con cálculo de presupuesto interactivo, y catálogo de productos oficiales con cesta de compra.
2. **Embudo de Compra (Checkout en 5 Pasos):** Stepper visible a la derecha en todo momento con Identificación (`Paso 1`), Dirección de envío (`Paso 2`), Método de pago (`Paso 3`: Tarjeta, Bizum, Transferencia), Confirmación (`Paso 4`) y Recibo Oficial imprimible (`Paso 5`).
3. **Área Privada de Cliente:** Historial de contratos, historial de pedidos con detalle, gestión de datos personales y cambio de contraseña.
4. **Panel de Gestión de Administración:** Módulos de administración para contratos, pedidos, catálogo de productos, miembros y certámenes, con control de acceso por roles.

---

## Estructura del Repositorio

```text
├── index.html                 # Entrada principal con redirección al prototipo
├── prototipo/                 # Aplicación web completa y modular
│   ├── index.html             # Portada principal con diseño corporativo
│   ├── visitante/             # Vistas públicas (Tienda, Cancionero, Contratación...)
│   │   ├── AccesoPedido.html       # Paso 1: Identificación
│   │   ├── DireccionEnvio.html     # Paso 2: Dirección de entrega
│   │   ├── MetodoPago.html         # Paso 3: Selección de método de pago
│   │   ├── ConfirmacionPedido.html # Paso 4: Revisión y formalización
│   │   └── ReciboPedido.html       # Paso 5: Justificante de compra
│   ├── cliente/               # Vistas privadas del cliente
│   ├── admin/                 # Vistas privadas de administración
│   ├── assets/img/            # Fotografía oficial, imágenes de productos y logo SVG
│   ├── css/styles.css         # Sistema de diseño, layout checkout y variables de color
│   └── js/                    # Módulos JavaScript (db.js, cart.js, forms.js, main.js, admin.js)
├── database/                  # Base de datos relacional
│   ├── schema.sql             # Esquema DDL de 10 tablas relacionales
│   ├── seed_data.sql          # Datos de prueba (usuarios, productos, contratos, canciones)
│   └── tuna_almeria.db        # Base de datos SQLite compilada
├── mockup/                    # Mockups interactivos y diseño gráfico previo
├── wireframes_tuna/           # Wireframes iniciales en HTML
├── diagramas_tuna_png/        # Diagramas de flujo y arquitectura
└── arboles/                   # Árboles de navegación del sitio
```

---

## Base de Datos y Cuentas de Acceso

La aplicación cuenta con una capa ORM client-side (`prototipo/js/db.js`) conectada al esquema SQL de `database/schema.sql`:

- **Cliente de prueba:** `marta.gil@ual.es` · Clave: `cliente123`
- **Administrador:** `admin@derechoual.es` · Clave: `admin123`

---

## Ramas del Repositorio

- `main`: Código actual del proyecto con prototipo funcional, base de datos relacional y embudo de compra en 5 pasos.
- `version-antigua` / `version_antigua`: Código histórico previo del repositorio preservado íntegramente.

