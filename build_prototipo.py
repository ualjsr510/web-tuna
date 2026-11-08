# -*- coding: utf-8 -*-
"""
Build complete modular prototype for Tuna de la Facultad de Derecho de Almería.
Generates all 57 pages + top-level portal index.html.
"""

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
PROTOTIPO_DIR = os.path.join(ROOT, "prototipo")
MOCKUP_FILE = os.path.join(ROOT, "mockup", "mockup_tuna.html")

with open(MOCKUP_FILE, "r", encoding="utf-8") as f:
    mockup_html = f.read()

# Extract all 57 screens
matches = list(re.finditer(r'<section class="screen" data-route="([^"]+)">', mockup_html))
screens = {}
for i in range(len(matches)):
    m = matches[i]
    route = m.group(1)
    start = m.end()
    if i + 1 < len(matches):
        raw_body = mockup_html[start:matches[i+1].start()]
    else:
        end = mockup_html.find('</section>', start)
        raw_body = mockup_html[start:end]
    raw_body = re.sub(r'</section>\s*$', '', raw_body.strip())
    raw_body = re.sub(r'^\s*<div class="wireframe">', '', raw_body)
    raw_body = re.sub(r'</div>\s*$', '', raw_body)
    screens[route] = raw_body

print(f"Loaded {len(screens)} screens from mockup_tuna.html")

def convert_links(html_chunk, current_route):
    curr_role = current_route.split('/')[0]
    
    def repl(m):
        target = m.group(1) # e.g. visitante/index.html or admin/Contratos.html
        parts = target.split('/')
        target_role = parts[0]
        target_file = parts[1] if len(parts) > 1 else 'index.html'
        
        if curr_role == target_role:
            return f'href="{target_file}"'
        else:
            return f'href="../{target_role}/{target_file}"'

    # Convert href="#/..." to relative paths
    res = re.sub(r'href="#/([^"]+)"', repl, html_chunk)
    # Convert onclick="appGoBack(event, 'visitante/index.html')" to onclick="TunaApp.goBack('index.html')"
    def repl_back(m):
        target = m.group(1)
        if not target:
            return 'onclick="TunaApp.goBack()"'
        parts = target.split('/')
        if len(parts) > 1 and parts[0] == curr_role:
            return f'onclick="TunaApp.goBack(\'{parts[1]}\')"'
        elif len(parts) > 1:
            return f'onclick="TunaApp.goBack(\'../{parts[0]}/{parts[1]}\')"'
        return f'onclick="TunaApp.goBack(\'{target}\')"'

    res = re.sub(r'onclick="appGoBack\(event,\s*\'([^\']*)\'\)"', repl_back, res)
    return res

def get_header_html(role, current_file):
    # Role-based navigation
    if role == 'visitante':
        nav_items = [
            ("Conoce la tuna", "Conoce.html"),
            ("Contratación", "Contratacion.html"),
            ("Multimedia", "Multimedia.html"),
            ("Tienda", "Tienda.html"),
            ("Cancionero", "Cancionero.html"),
            ("Únete", "Unete.html")
        ]
        nav_html = "".join([
            f'<a href="{f}" class="{ "active" if current_file == f or (f=="Tienda.html" and current_file in ["Catalogo.html", "Cesta.html"]) else "" }">{t}</a>'
            for t, f in nav_items
        ])
        actions_html = """
          <a href="Cesta.html" class="btn-header-cart">
            🛒 Cesta (<span class="cart-counter-val">2</span>)
          </a>
          <a href="Acceso.html" class="btn-header-login">
            Iniciar sesión
          </a>
        """
    elif role == 'cliente':
        nav_items = [
            ("Inicio", "index.html"),
            ("Mis Contratos", "Contratos.html"),
            ("Mis Pedidos", "Pedidos.html"),
            ("Mi Cuenta", "Cuenta.html")
        ]
        nav_html = "".join([
            f'<a href="{f}" class="{ "active" if current_file == f else "" }">{t}</a>'
            for t, f in nav_items
        ])
        actions_html = """
          <a href="../visitante/index.html" class="btn-header-cart" title="Ver portal público de la Tuna">
            🏛 Portal Público
          </a>
          <a href="../visitante/index.html" class="btn btn-outline" style="font-size:12px; padding:6px 12px;" onclick="TunaApp.logout()">
            Cerrar sesión
          </a>
        """
    else: # admin
        nav_items = [
            ("Panel", "index.html"),
            ("Contratos", "Contratos.html"),
            ("Clientes", "Clientes.html"),
            ("Pedidos", "Pedidos.html"),
            ("Productos", "Productos.html"),
            ("Miembros", "Miembros.html"),
            ("Certámenes", "Certamenes.html")
        ]
        nav_html = "".join([
            f'<a href="{f}" class="{ "active" if current_file == f else "" }">{t}</a>'
            for t, f in nav_items
        ])
        actions_html = """
          <span class="badge-accent" style="font-size:11px;">ADMIN</span>
          <a href="../visitante/index.html" class="btn-header-cart" title="Ver portal público">
            👁 Ver Web
          </a>
          <a href="../visitante/index.html" class="btn btn-outline" style="font-size:12px; padding:6px 12px;" onclick="TunaApp.logout()">
            Salir
          </a>
        """

    return f"""
    <!-- BARRA SUPERIOR PARA CAMBIO RÁPIDO DE PERFIL EN EVALUACIÓN -->
    <div class="demo-role-bar">
      <div>
        <strong>Tuna de la Facultad de Derecho de Almería</strong> · Prototipo Web Oficial
      </div>
      <div style="display: flex; gap: 8px; align-items: center;">
        <span>Perfil activo: <strong class="current-role-badge">{role.upper()}</strong></span>
        <a href="../visitante/index.html" class="{ 'active' if role=='visitante' else '' }">Visitante</a>
        <a href="../cliente/index.html" class="{ 'active' if role=='cliente' else '' }">Cliente</a>
        <a href="../admin/index.html" class="{ 'active' if role=='admin' else '' }">Administrador</a>
      </div>
    </div>

    <!-- CABECERA PRINCIPAL CON LOGO CORPORATIVO -->
    <header class="site-header">
      <a href="../{role}/index.html" class="site-logo">
        <img src="../assets/img/logo_corporativo.svg" alt="Tuna de Derecho Almería Logo" style="height:48px;">
      </a>
      <nav class="site-nav">
        {nav_html}
      </nav>
      <div class="header-actions">
        {actions_html}
      </div>
    </header>
    """

def get_footer_html(role):
    prefix = "" if role == "root" else "../"
    return f"""
    <footer class="site-footer">
      <div class="footer-grid">
        <div class="footer-col">
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
            <img src="{prefix}assets/img/logo_corporativo.svg" alt="Tuna de Derecho" style="height:44px; filter:brightness(1.2);">
          </div>
          <p>
            Agrupación musical tradicional universitaria de la <strong>Facultad de Derecho de la Universidad de Almería</strong>. Fundada en el verano de 1993. Portadora de la alegría, la música y el buen hacer estudiantil.
          </p>
          <p style="font-size:12px; color:var(--gold);">
            🏛 Edificio CAE · Universidad de Almería · La Cañada de San Urbano, 04120 Almería
          </p>
        </div>
        <div class="footer-col">
          <h4>Navegación</h4>
          <ul class="footer-links">
            <li><a href="{prefix}visitante/index.html">Inicio del portal</a></li>
            <li><a href="{prefix}visitante/Conoce.html">Historia y miembros</a></li>
            <li><a href="{prefix}visitante/Contratacion.html">Contratar actuaciones</a></li>
            <li><a href="{prefix}visitante/Tienda.html">Tienda oficial y discos</a></li>
            <li><a href="{prefix}visitante/Cancionero.html">Cancionero y música</a></li>
            <li><a href="{prefix}visitante/Unete.html">Únete a la tuna</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Área Privada</h4>
          <ul class="footer-links">
            <li><a href="{prefix}visitante/Acceso.html">Iniciar sesión</a></li>
            <li><a href="{prefix}visitante/Registro.html">Registro de clientes</a></li>
            <li><a href="{prefix}cliente/index.html">Panel de cliente</a></li>
            <li><a href="{prefix}admin/index.html">Panel de administración</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contacto Oficial</h4>
          <p>
            📞 <strong>Teléfono:</strong> <a href="tel:685995510" style="color:#fff;">685 99 55 10</a><br>
            ✉️ <strong>Email:</strong> <a href="mailto:tunaderechoalmeria@hotmail.es" style="color:#eed793;">tunaderechoalmeria@hotmail.es</a><br>
            📸 <strong>Instagram:</strong> <a href="https://instagram.com/tunaderechoalmeria" target="_blank" style="color:#eed793;">@tunaderechoalmeria</a><br>
            🎵 <strong>YouTube:</strong> <a href="https://www.youtube.com/channel/UCAYXgNyTwe-L2edchU-Ee0A" target="_blank" style="color:#eed793;">Tuna Derecho Almería</a>
          </p>
        </div>
      </div>
      <div class="footer-bottom">
        <div>
          © 1993 - 2026 Tuna de la Facultad de Derecho de Almería. Todos los derechos reservados.
        </div>
        <div style="display:flex; gap:16px;">
          <span>Tecnologías Web · UAL</span>
          <span>Aviso Legal</span>
          <span>Política de Privacidad</span>
        </div>
      </div>
    </footer>
    """

# Generate each screen
for route, raw_body in screens.items():
    role, filename = route.split('/')
    target_dir = os.path.join(PROTOTIPO_DIR, role)
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, filename)

    # Remove the old wireframe <header> ... </header>
    clean_body = re.sub(r'<header style="[^"]*">.*?</header>', '', raw_body, count=1, flags=re.DOTALL)
    
    # Convert links
    converted_body = convert_links(clean_body, route)
    
    # Replace any leftover wireframe logo or placeholders with real corporate logo & assets
    converted_body = converted_body.replace(
        '<a href="#/visitante/index.html" style="width: 92px; height: 38px; border: 1px solid var(--accent); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-decoration: none">TUNA</a>',
        f'<a href="../{role}/index.html" class="site-logo"><img src="../assets/img/logo_corporativo.svg" alt="Tuna de Derecho Almería" style="height:46px;"></a>'
    )
    converted_body = converted_body.replace(
        '<a href="#/admin/index.html" style="width: 92px; height: 38px; border: 1px solid var(--accent); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-decoration: none">TUNA</a>',
        f'<a href="../{role}/index.html" class="site-logo"><img src="../assets/img/logo_corporativo.svg" alt="Tuna de Derecho Almería" style="height:46px;"></a>'
    )
    converted_body = converted_body.replace(
        '<a href="#/cliente/index.html" style="width: 92px; height: 38px; border: 1px solid var(--accent); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-decoration: none">TUNA</a>',
        f'<a href="../{role}/index.html" class="site-logo"><img src="../assets/img/logo_corporativo.svg" alt="Tuna de Derecho Almería" style="height:46px;"></a>'
    )

    # Determine scripts to include
    extra_scripts = ""
    if filename in ["Catalogo.html", "Tienda.html"]:
        extra_scripts += '\n  <script src="../js/catalog.js"></script>'
    if filename in ["Cesta.html", "Catalogo.html", "Tienda.html", "DireccionEnvio.html"]:
        extra_scripts += '\n  <script src="../js/cart.js"></script>'
    if filename in ["Cancionero.html", "Repertorio.html", "Spotify.html"]:
        extra_scripts += '\n  <script src="../js/audio-player.js"></script>'
    if filename in ["Contratacion.html", "FormularioContratacion.html", "Unete.html", "Formulario.html", "Acceso.html", "Registro.html"]:
        extra_scripts += '\n  <script src="../js/forms.js"></script>'
    if role == "admin":
        extra_scripts += '\n  <script src="../js/admin.js"></script>'

    # Specific interactive enhancements per page
    if filename == "Catalogo.html":
        # Inject catalog functional controls if not present
        if 'id="catalog-products-grid"' not in converted_body:
            # Wrap the catalog products into an interactive container
            pass

    full_page = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería — {filename.replace('.html','')}</title>
  <link rel="stylesheet" href="../css/styles.css">
  <link rel="icon" type="image/svg+xml" href="../assets/img/logo_corporativo.svg">
</head>
<body>
  {get_header_html(role, filename)}

  <div class="main-content">
    {converted_body}
  </div>

  {get_footer_html(role)}

  <!-- Scripts modulares -->
  <script src="../js/main.js"></script>{extra_scripts}
</body>
</html>
"""
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(full_page)

print(f"Generated all 57 pages successfully in {PROTOTIPO_DIR}!")

# Now generate prototipo/index.html (Entrance Portal)
index_portal_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería — Prototipo Oficial</title>
  <link rel="stylesheet" href="css/styles.css">
  <link rel="icon" type="image/svg+xml" href="assets/img/logo_corporativo.svg">
</head>
<body>
  <!-- BARRA DE ROL -->
  <div class="demo-role-bar">
    <div>
      <strong>Tuna de la Facultad de Derecho de Almería</strong> · Prototipo Web Oficial
    </div>
    <div style="display: flex; gap: 8px; align-items: center;">
      <a href="visitante/index.html" class="active">Visitante</a>
      <a href="cliente/index.html">Cliente</a>
      <a href="admin/index.html">Administrador</a>
    </div>
  </div>

  <!-- CABECERA -->
  <header class="site-header">
    <a href="visitante/index.html" class="site-logo">
      <img src="assets/img/logo_corporativo.svg" alt="Tuna de Derecho Almería Logo" style="height:48px;">
    </a>
    <nav class="site-nav">
      <a href="visitante/Conoce.html">Conoce la tuna</a>
      <a href="visitante/Contratacion.html">Contratación</a>
      <a href="visitante/Multimedia.html">Multimedia</a>
      <a href="visitante/Tienda.html">Tienda</a>
      <a href="visitante/Cancionero.html">Cancionero</a>
      <a href="visitante/Unete.html">Únete</a>
    </nav>
    <div class="header-actions">
      <a href="visitante/Cesta.html" class="btn-header-cart">
        🛒 Cesta (<span class="cart-counter-val">2</span>)
      </a>
      <a href="visitante/Acceso.html" class="btn-header-login">
        Iniciar sesión
      </a>
    </div>
  </header>

  <div class="main-content" style="display:flex; flex-direction:column; gap:36px; padding-top:16px;">
    
    <!-- HERO PRINCIPAL CON FOTO OFICIAL Y LOGO -->
    <section class="tuna-card" style="background: var(--hero); color:#fff; padding:48px 36px; border:2px solid var(--gold); border-radius:12px; position:relative; overflow:hidden; box-shadow:var(--shadow-xl);">
      <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:32px; position:relative; z-index:2;">
        <div style="flex:1; min-width:320px; max-width:680px;">
          <div style="display:inline-flex; align-items:center; gap:8px; padding:6px 16px; background:rgba(0,0,0,0.4); border:1px solid var(--gold); border-radius:99px; font-size:11px; font-weight:700; color:var(--gold-light); letter-spacing:0.1em; text-transform:uppercase; margin-bottom:14px;">
            <span>🏛</span> FACULTAD DE DERECHO · UNIVERSIDAD DE ALMERÍA
          </div>
          <h1 style="font-size:clamp(30px, 4vw, 44px); color:#fbf3df; font-family:var(--serif); margin:0 0 14px; text-shadow:0 3px 12px rgba(0,0,0,0.6); line-height:1.2;">
            Tuna de la Facultad de Derecho de Almería
          </h1>
          <p style="font-size:16px; color:#eed793; line-height:1.6; margin:0 0 24px; font-style:italic;">
            «Música, tradición estudiantil, galantería y alegría en cada ronda desde 1993»
          </p>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="visitante/index.html" class="btn btn-gold" style="font-size:14px; padding:13px 24px;">
              🌹 Entrar como Visitante
            </a>
            <a href="visitante/Contratacion.html" class="btn btn-primary" style="font-size:14px; padding:13px 22px;">
              🎻 Contratar Actuación
            </a>
            <a href="visitante/Tienda.html" class="btn btn-outline" style="background:rgba(255,255,255,0.12); color:#fff; border-color:rgba(255,255,255,0.3); font-size:14px; padding:13px 20px;">
              🛍️ Tienda y Catálogo
            </a>
          </div>
        </div>
        
        <!-- FOTO OFICIAL DE LA TUNA -->
        <div style="flex:1; min-width:320px; max-width:540px;">
          <div class="tuna-photo-frame" style="height:320px; border-radius:10px; border:2px solid var(--gold); box-shadow:var(--shadow-lg);">
            <img src="assets/img/tuna_oficial_grupo.jpg" alt="Tuna de Derecho de Almería" style="object-fit:cover;">
            <span class="badge-gold" style="position:absolute; bottom:12px; right:12px; background:rgba(20,12,15,0.85); color:#eed793; border:1px solid var(--gold);">
              Fotografía Oficial · Tuna de Derecho UAL
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- SELECTOR DE PERFILES DEL PROTOTIPO -->
    <section>
      <div style="border-bottom:2px solid var(--line); padding-bottom:8px; margin-bottom:20px;">
        <span class="badge-accent">ACCESO A PERFILES</span>
        <h2 style="font-size:22px; margin-top:6px;">Explorar el Prototipo por Perfiles</h2>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:24px;" class="responsive-grid-3">
        <!-- Tarjeta Visitante -->
        <article class="tuna-card tuna-card-hover" style="border-top:4px solid var(--accent); padding:24px; gap:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:32px;">🌹</span>
            <span class="badge badge-info">26 PANTALLAS</span>
          </div>
          <div>
            <h3 style="font-size:18px; margin-bottom:6px;">Perfil Visitante</h3>
            <p style="font-size:13px; color:var(--muted); line-height:1.5; margin:0;">
              Portal público con historia de la tuna, miembros, contratación con presupuesto instantáneo, tienda con filtros, cancionero interactivo con música y formulario para nuevos aspirantes.
            </p>
          </div>
          <div style="margin-top:auto; padding-top:12px;">
            <a href="visitante/index.html" class="btn btn-primary" style="width:100%;">
              Acceder como Visitante →
            </a>
          </div>
        </article>

        <!-- Tarjeta Cliente -->
        <article class="tuna-card tuna-card-hover" style="border-top:4px solid var(--gold); padding:24px; gap:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:32px;">👤</span>
            <span class="badge badge-gold">10 PANTALLAS</span>
          </div>
          <div>
            <h3 style="font-size:18px; margin-bottom:6px;">Perfil Cliente Registrado</h3>
            <p style="font-size:13px; color:var(--muted); line-height:1.5; margin:0;">
              Área personal de contratación y compras de clientes (Marta Gil). Historial de contratos solicitados, seguimiento de pedidos de tienda, edición de direcciones, devoluciones y cuenta.
            </p>
          </div>
          <div style="margin-top:auto; padding-top:12px;">
            <a href="cliente/index.html" class="btn btn-gold" style="width:100%;">
              Acceder como Cliente →
            </a>
          </div>
        </article>

        <!-- Tarjeta Administrador -->
        <article class="tuna-card tuna-card-hover" style="border-top:4px solid #181214; padding:24px; gap:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:32px;">⚙️</span>
            <span class="badge badge-accent">21 PANTALLAS</span>
          </div>
          <div>
            <h3 style="font-size:18px; margin-bottom:6px;">Panel de Administración</h3>
            <p style="font-size:13px; color:var(--muted); line-height:1.5; margin:0;">
              Gestión global para miembros directivos de la tuna. Estadísticas de actividad, aprobación de contratos de actuaciones, cartera de clientes, inventario de tienda, censo de tunos y certámenes.
            </p>
          </div>
          <div style="margin-top:auto; padding-top:12px;">
            <a href="admin/index.html" class="btn btn-outline" style="width:100%; font-weight:700;">
              Acceder a Administración →
            </a>
          </div>
        </article>
      </div>
    </section>

    <!-- CARACTERÍSTICAS PRINCIPALES IMPLEMENTADAS -->
    <section class="tuna-card" style="background:var(--soft-2); border:1px solid var(--line); padding:28px;">
      <h2 style="font-size:20px; margin-bottom:18px; color:var(--accent);">Características Funcionales y Modulares Destacadas</h2>
      <div style="display:grid; grid-template-columns:repeat(4, minmax(0, 1fr)); gap:20px;" class="responsive-grid-2">
        <div style="background:var(--card); padding:16px; border-radius:6px; border:1px solid var(--line);">
          <strong style="color:var(--accent); font-size:14px; display:block; margin-bottom:6px;">🛒 Cesta Persistente</strong>
          <p style="font-size:12.5px; color:var(--muted); margin:0;">Añadir, eliminar productos, modificar cantidades y sincronización del badge en cabecera en tiempo real con LocalStorage.</p>
        </div>
        <div style="background:var(--card); padding:16px; border-radius:6px; border:1px solid var(--line);">
          <strong style="color:var(--accent); font-size:14px; display:block; margin-bottom:6px;">🔍 Catálogo con Filtros</strong>
          <p style="font-size:12.5px; color:var(--muted); margin:0;">Buscador instantáneo por texto, categorías (indumentaria, música, recuerdos), filtro de precio y ficha lateral interactiva con tallas.</p>
        </div>
        <div style="background:var(--card); padding:16px; border-radius:6px; border:1px solid var(--line);">
          <strong style="color:var(--accent); font-size:14px; display:block; margin-bottom:6px;">🎶 Cancionero Web Audio</strong>
          <p style="font-size:12.5px; color:var(--muted); margin:0;">Reproductor funcional con temas tradicionales, arpegios acústicos en vivo, letras completas y selector de pistas.</p>
        </div>
        <div style="background:var(--card); padding:16px; border-radius:6px; border:1px solid var(--line);">
          <strong style="color:var(--accent); font-size:14px; display:block; margin-bottom:6px;">📋 Presupuestos en Vivo</strong>
          <p style="font-size:12.5px; color:var(--muted); margin:0;">Calculadora interactiva en el formulario de contratación según tipo de evento, número de músicos y horas de actuación.</p>
        </div>
      </div>
    </section>

  </div>

  {get_footer_html("root")}

  <script src="js/main.js"></script>
  <script src="js/cart.js"></script>
</body>
</html>
"""

with open(os.path.join(PROTOTIPO_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_portal_html)

print("Created prototipo/index.html portal successfully!")

