# -*- coding: utf-8 -*-
"""
Generador del Mockup para ADMINISTRADOR (admin.html)
Fiel a los 21 wireframes de Administrador:
- 0 Panel con estadísticas (index.html)
- 1 Gestionar contratos (Contratos.html, ContratoDetalle.html)
- 2 Gestionar cartera de clientes (Clientes.html, FichaCliente.html, ContratosCliente.html, PedidosCliente.html)
- 3 Gestionar pedidos de la tienda (Pedidos.html, PedidoDetalle.html)
- 4 Gestionar productos de la tienda (Productos.html, ProductoNuevo.html, ProductosGestion.html)
- 5 Gestionar lista de miembros (Miembros.html, MiembroNuevo.html, MiembrosGestion.html)
- 6 Gestionar cuenta (Cuenta.html, CuentaDatos.html, CuentaPassword.html)
- 7 Gestionar certámenes (Certamenes.html, CertamenNuevo.html, CertamenesGestion.html)
"""

def get_admin_html():
    return """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería · Panel de Administración</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {
      --rojo-tuna: #8B0000;
      --rojo-oscuro: #5C0000;
      --dorado: #D4AF37;
      --fondo-admin: #F4F4F5;
    }
    body {
      background-color: var(--fondo-admin);
      color: #1F2937;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .font-serif-tuna {
      font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
    }
    .badge-editorial {
      letter-spacing: 0.18em;
      text-transform: uppercase;
      font-size: 0.7rem;
      font-weight: 700;
    }
    .admin-menu-item.active {
      background-color: #8B0000;
      color: #FFFFFF;
      font-weight: 700;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .subview-pill.active {
      background-color: #8B0000;
      color: #FFFFFF;
      font-weight: 700;
    }
    .pulse-call {
      animation: pulse-ring 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    @keyframes pulse-ring {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.05); }
    }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased">

  <!-- ========================================================================= -->
  <!-- SELECTOR DE PERFILES EN CABECERA SUPERIOR (INTERCONEXIÓN DE LOS 3 MOCKUPS) -->
  <!-- ========================================================================= -->
  <div class="sticky top-0 z-50 bg-[#121212] border-b border-amber-500/40 text-white shadow-xl">
    <div class="max-w-7xl mx-auto px-4 py-2 flex flex-col md:flex-row items-center justify-between gap-2 text-xs">
      <div class="flex items-center gap-2.5">
        <span class="w-6 h-6 rounded bg-red-900 text-amber-300 font-serif-tuna font-black flex items-center justify-center border border-amber-500 text-xs">TD</span>
        <div>
          <span class="text-amber-400 font-bold tracking-wider uppercase text-[10px] block">MOCKUP 3 DE 3 · PERFIL ACTUAL: ADMINISTRADOR</span>
          <span class="text-slate-300 text-[11px]">Tuna de la Facultad de Derecho de Almería</span>
        </div>
      </div>

      <!-- Selector para cambiar de mockup -->
      <div class="flex items-center bg-[#1f1f1f] p-1 rounded-xl border border-slate-700">
        <a href="visitante.html" class="px-3.5 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white transition flex items-center gap-1.5">
          <span>🌐</span> Visitante <span class="text-[10px] opacity-75">(Público)</span>
        </a>
        <a href="cliente.html" class="px-3.5 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white transition flex items-center gap-1.5">
          <span>👤</span> Cliente <span class="text-[10px] opacity-75">(Registrado)</span>
        </a>
        <a href="admin.html" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#8B0000] border-b-2 border-[#D4AF37] shadow flex items-center gap-1.5">
          <span>⚙️</span> Administrador <span class="text-[10px] opacity-75">(Gestión)</span>
        </a>
      </div>

      <!-- Teléfono de urgencias admin -->
      <div class="hidden lg:flex items-center gap-3">
        <span class="px-3 py-1 bg-red-900 text-amber-300 rounded-full font-bold border border-amber-400 text-xs">
          Sesión: SuperAdmin
        </span>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- BARRA DE CONTACTO CORPORATIVA Y REDES SOCIALES (ULTRA-VISIBLE) -->
  <!-- ========================================================================= -->
  <div class="bg-[#5C0000] text-white border-b-2 border-[#D4AF37] py-2.5 px-4 text-xs shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex flex-wrap items-center gap-4 sm:gap-6">
        <span class="font-black text-sm text-amber-300 flex items-center gap-2">
          <span>🔒</span> LÍNEA DIRECTA TUNA: +34 600 123 456 · +34 612 345 678
        </span>
        <span class="text-slate-200">✉️ tuna.derecho.almeria@gmail.com</span>
      </div>

      <div class="flex items-center gap-2">
        <span class="badge-editorial text-amber-300 hidden md:inline">Canales Oficiales:</span>
        <a href="https://instagram.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-pink-700 transition text-[11px] font-bold text-white">Instagram</a>
        <a href="https://tiktok.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-black transition text-[11px] font-bold text-white">TikTok</a>
        <a href="https://facebook.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-blue-700 transition text-[11px] font-bold text-white">Facebook</a>
        <a href="https://spotify.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-green-700 transition text-[11px] font-bold text-white">Spotify</a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- HEADER FIEL AL WIREFRAME DE ADMIN (LOGO TUNA + PANEL DE ADMINISTRACIÓN) -->
  <!-- ========================================================================= -->
  <header class="bg-white border-b border-stone-300 sticky top-12 z-40 shadow-sm py-3 px-6 flex items-center justify-between text-xs">
    <div class="flex items-center gap-4">
      <a href="#adm-0" onclick="switchAdminView('adm-0')" class="w-10 h-10 rounded bg-[#8B0000] text-amber-300 font-serif-tuna font-bold text-base flex items-center justify-center border border-[#D4AF37] shadow">
        TD
      </a>
      <div>
        <span class="font-serif-tuna font-bold text-base text-[#5C0000] block leading-none">PANEL DE ADMINISTRACIÓN</span>
        <span class="text-stone-500 text-[11px]">Tuna de la Facultad de Derecho de Almería</span>
      </div>
    </div>

    <div class="flex items-center gap-4">
      <div class="text-right hidden sm:block">
        <span class="font-bold text-stone-900 block">Tuno Mayor Javier Fernández</span>
        <span class="text-stone-400 text-[10px]">Administrador Principal</span>
      </div>
      <a href="visitante.html" class="px-3 py-1.5 border border-stone-300 rounded font-bold text-stone-700 hover:bg-stone-50 transition">
        Cerrar sesión
      </a>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- BARRA DE ACCESO DIRECTO A LAS 21 PANTALLAS WIREFRAME DE ADMIN -->
  <!-- ========================================================================= -->
  <div class="bg-stone-100 border-b border-stone-300 py-2 px-4 text-xs overflow-x-auto whitespace-nowrap shadow-inner">
    <div class="max-w-7xl mx-auto flex items-center gap-1.5">
      <span class="font-bold text-stone-500 uppercase tracking-wider text-[10px] mr-1">Pantallas Wireframe Admin:</span>
      <button onclick="switchAdminView('adm-0')" class="subview-pill active px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">0. Panel Estadísticas</button>
      <button onclick="switchAdminView('adm-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">1. Contratos</button>
      <button onclick="switchAdminView('adm-1-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">1.1 Detalle Contrato</button>
      <button onclick="switchAdminView('adm-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2. Cartera Clientes</button>
      <button onclick="switchAdminView('adm-2-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2.1 Ficha Cliente</button>
      <button onclick="switchAdminView('adm-3')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3. Pedidos Tienda</button>
      <button onclick="switchAdminView('adm-3-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3.1 Detalle Pedido</button>
      <button onclick="switchAdminView('adm-4')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">4. Productos</button>
      <button onclick="switchAdminView('adm-4-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">4.1 Añadir Producto</button>
      <button onclick="switchAdminView('adm-4-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">4.2 Modificar/Eliminar</button>
      <button onclick="switchAdminView('adm-5')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">5. Lista Miembros</button>
      <button onclick="switchAdminView('adm-5-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">5.1 Modificar Miembro</button>
      <button onclick="switchAdminView('adm-5-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">5.2 Añadir Miembro</button>
      <button onclick="switchAdminView('adm-6')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">6. Cuenta Admin</button>
      <button onclick="switchAdminView('adm-6-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">6.1 Info Personal</button>
      <button onclick="switchAdminView('adm-6-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">6.2 Password</button>
      <button onclick="switchAdminView('adm-7')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">7. Certámenes</button>
      <button onclick="switchAdminView('adm-7-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">7.1 Modificar Certamen</button>
      <button onclick="switchAdminView('adm-7-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">7.2 Crear Certamen</button>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- LAYOUT PRINCIPAL ADMIN: SIDEBAR LATERAL IZQUIERDO (232px) + CONTENIDO MAIN -->
  <!-- ========================================================================= -->
  <div class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 grid lg:grid-cols-12 gap-6">

    <!-- SIDEBAR FIEL AL WIREFRAME (admin/index.html aside) -->
    <aside class="lg:col-span-3 space-y-2 text-xs">
      <div class="bg-white rounded-xl border border-stone-200 p-3 shadow-sm space-y-1">
        <div class="text-[10px] font-bold text-stone-400 uppercase px-3 py-1">Módulos Administrativos</div>
        
        <button onclick="switchAdminView('adm-0')" id="side-0" class="admin-menu-item active w-full text-left px-3 py-2 rounded-lg font-bold flex items-center gap-2">
          <span>📊</span> Panel de estadísticas
        </button>
        <button onclick="switchAdminView('adm-1')" id="side-1" class="admin-menu-item w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
          <span>📜</span> 1 Contratos
        </button>
        <button onclick="switchAdminView('adm-2')" id="side-2" class="admin-menu-item w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
          <span>👥</span> 2 Cartera de clientes
        </button>
        <button onclick="switchAdminView('adm-3')" id="side-3" class="admin-menu-item w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
          <span>📦</span> 3 Pedidos de la tienda
        </button>
        <button onclick="switchAdminView('adm-4')" id="side-4" class="admin-menu-item w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
          <span>🛍️</span> 4 Productos de la tienda
        </button>
        <button onclick="switchAdminView('adm-5')" id="side-5" class="admin-menu-item w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
          <span>🎸</span> 5 Lista de miembros
        </button>
        <button onclick="switchAdminView('adm-6')" id="side-6" class="admin-menu-item w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
          <span>🔑</span> 6 Cuenta
        </button>
        <button onclick="switchAdminView('adm-7')" id="side-7" class="admin-menu-item w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
          <span>🏆</span> 7 Certámenes
        </button>
      </div>

      <!-- Tarjeta de contacto interno -->
      <div class="bg-[#5C0000] text-white rounded-xl p-4 text-xs border border-amber-400/80 shadow">
        <span class="badge-editorial text-amber-300 block mb-1">TELÉFONOS DE CONTACTO</span>
        <div class="text-[11px] text-stone-200">Guardia de actuaciones:</div>
        <div class="font-bold text-white mt-1">📞 +34 600 123 456</div>
        <div class="font-bold text-white">📞 +34 612 345 678</div>
      </div>
    </aside>

    <!-- ÁREA DE CONTENIDO MAIN (Fiel a los wireframes) -->
    <main class="lg:col-span-9 space-y-6">

      <!-- ================= PANTALLA 0: PANEL CON ESTADÍSTICAS ================= -->
      <div id="adm-0" class="admin-subview space-y-6">
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Panel de administración</h1>
          <p class="text-xs text-stone-500 mt-1">Resumen y estadísticas de la tuna de Derecho de Almería</p>
        </div>

        <!-- 4 Cajas KPI del Wireframe -->
        <section class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs">
          <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
            <span class="text-stone-500 font-bold uppercase text-[10px]">Contratos pendientes</span>
            <div class="text-3xl font-black text-[#8B0000] mt-1">4</div>
          </div>
          <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
            <span class="text-stone-500 font-bold uppercase text-[10px]">Pedidos pendientes</span>
            <div class="text-3xl font-black text-stone-900 mt-1">7</div>
          </div>
          <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
            <span class="text-stone-500 font-bold uppercase text-[10px]">Ingresos del mes</span>
            <div class="text-3xl font-black text-emerald-700 mt-1">1.840 €</div>
          </div>
          <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
            <span class="text-stone-500 font-bold uppercase text-[10px]">Clientes nuevos</span>
            <div class="text-3xl font-black text-blue-800 mt-1">12</div>
          </div>
        </section>

        <!-- 2 Gráficos de barras del Wireframe -->
        <section class="grid md:grid-cols-2 gap-6 text-xs">
          <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm">
            <h2 class="font-serif-tuna font-bold text-base text-stone-900 mb-3">Contratos por mes</h2>
            <div class="flex items-end gap-1.5 h-36 border-b border-stone-900 pb-1 px-1">
              <div class="flex-1 bg-red-200 h-[40%] rounded-t" title="Ene: 4"></div>
              <div class="flex-1 bg-red-200 h-[55%] rounded-t" title="Feb: 6"></div>
              <div class="flex-1 bg-red-200 h-[35%] rounded-t" title="Mar: 3"></div>
              <div class="flex-1 bg-red-300 h-[70%] rounded-t" title="Abr: 8"></div>
              <div class="flex-1 bg-red-400 h-[60%] rounded-t" title="May: 7"></div>
              <div class="flex-1 bg-red-500 h-[80%] rounded-t" title="Jun: 9"></div>
              <div class="flex-1 bg-red-600 h-[95%] rounded-t" title="Jul: 12"></div>
              <div class="flex-1 bg-red-600 h-[90%] rounded-t" title="Ago: 11"></div>
              <div class="flex-1 bg-red-400 h-[75%] rounded-t" title="Sep: 8"></div>
              <div class="flex-1 bg-red-300 h-[50%] rounded-t" title="Oct: 5"></div>
              <div class="flex-1 bg-red-200 h-[40%] rounded-t" title="Nov: 4"></div>
              <div class="flex-1 bg-red-400 h-[65%] rounded-t" title="Dic: 7"></div>
            </div>
            <div class="flex justify-between text-[10px] text-stone-400 mt-2 font-mono">
              <span>Ene</span><span>Jun</span><span>Dic (Últimos 12 meses)</span>
            </div>
          </div>

          <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm">
            <h2 class="font-serif-tuna font-bold text-base text-stone-900 mb-3">Ventas de la tienda por mes</h2>
            <div class="flex items-end gap-1.5 h-36 border-b border-stone-900 pb-1 px-1">
              <div class="flex-1 bg-amber-200 h-[30%] rounded-t"></div>
              <div class="flex-1 bg-amber-200 h-[45%] rounded-t"></div>
              <div class="flex-1 bg-amber-200 h-[60%] rounded-t"></div>
              <div class="flex-1 bg-amber-300 h-[40%] rounded-t"></div>
              <div class="flex-1 bg-amber-300 h-[55%] rounded-t"></div>
              <div class="flex-1 bg-amber-400 h-[70%] rounded-t"></div>
              <div class="flex-1 bg-amber-500 h-[65%] rounded-t"></div>
              <div class="flex-1 bg-amber-300 h-[50%] rounded-t"></div>
              <div class="flex-1 bg-amber-400 h-[60%] rounded-t"></div>
              <div class="flex-1 bg-amber-500 h-[80%] rounded-t"></div>
              <div class="flex-1 bg-amber-500 h-[70%] rounded-t"></div>
              <div class="flex-1 bg-amber-600 h-[95%] rounded-t"></div>
            </div>
            <div class="flex justify-between text-[10px] text-stone-400 mt-2 font-mono">
              <span>Ene</span><span>Jun</span><span>Dic (Últimos 12 meses)</span>
            </div>
          </div>
        </section>

        <!-- 2 Tablas de Resumen Fieles al Wireframe -->
        <section class="grid md:grid-cols-2 gap-6 text-xs">
          <!-- Últimos contratos -->
          <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm space-y-3">
            <h2 class="font-serif-tuna font-bold text-base text-stone-900">Últimos contratos</h2>
            <table class="w-full text-left border border-stone-200 rounded overflow-hidden">
              <thead class="bg-stone-50 border-b border-stone-200 font-bold">
                <tr><th class="py-2 px-3">Nº</th><th class="py-2 px-3">Cliente</th><th class="py-2 px-3">Estado</th><th class="py-2 px-3 text-right"></th></tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                <tr><td class="py-2 px-3 font-bold">#CTR-042</td><td class="py-2 px-3">José Manuel Martínez</td><td class="py-2 px-3 text-green-700 font-bold">Aceptado</td><td class="py-2 px-3 text-right"><button onclick="switchAdminView('adm-1-1')" class="text-[#8B0000] font-bold">Ver</button></td></tr>
                <tr><td class="py-2 px-3 font-bold">#CTR-043</td><td class="py-2 px-3">Colegio de Abogados</td><td class="py-2 px-3 text-amber-700 font-bold">Pendiente</td><td class="py-2 px-3 text-right"><button onclick="switchAdminView('adm-1-1')" class="text-[#8B0000] font-bold">Ver</button></td></tr>
              </tbody>
            </table>
            <button onclick="switchAdminView('adm-1')" class="text-[#8B0000] font-bold block pt-1 hover:underline">Ver todos los contratos →</button>
          </div>

          <!-- Últimos pedidos -->
          <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm space-y-3">
            <h2 class="font-serif-tuna font-bold text-base text-stone-900">Últimos pedidos</h2>
            <table class="w-full text-left border border-stone-200 rounded overflow-hidden">
              <thead class="bg-stone-50 border-b border-stone-200 font-bold">
                <tr><th class="py-2 px-3">Nº</th><th class="py-2 px-3">Cliente</th><th class="py-2 px-3">Estado</th><th class="py-2 px-3 text-right"></th></tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                <tr><td class="py-2 px-3 font-bold">#PED-894</td><td class="py-2 px-3">José Manuel Martínez</td><td class="py-2 px-3 text-blue-700 font-bold">Enviado</td><td class="py-2 px-3 text-right"><button onclick="switchAdminView('adm-3-1')" class="text-[#8B0000] font-bold">Ver</button></td></tr>
                <tr><td class="py-2 px-3 font-bold">#PED-895</td><td class="py-2 px-3">Carmen Sánchez</td><td class="py-2 px-3 text-amber-700 font-bold">Preparando</td><td class="py-2 px-3 text-right"><button onclick="switchAdminView('adm-3-1')" class="text-[#8B0000] font-bold">Ver</button></td></tr>
              </tbody>
            </table>
            <button onclick="switchAdminView('adm-3')" class="text-[#8B0000] font-bold block pt-1 hover:underline">Ver todos los pedidos →</button>
          </div>
        </section>
      </div>

      <!-- ================= PANTALLA 1: GESTIONAR CONTRATOS ================= -->
      <div id="adm-1" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <span class="text-stone-900 font-semibold">1 Gestionar contratos</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Gestionar contratos</h1>
          <p class="text-xs text-stone-500 mt-1">Revisa las solicitudes de actuación y aprueba presupuestos</p>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm text-xs">
          <table class="w-full text-left">
            <thead class="bg-stone-50 border-b border-stone-200 text-stone-500 uppercase font-bold">
              <tr>
                <th class="py-3 px-4">Nº</th>
                <th class="py-3 px-4">Cliente</th>
                <th class="py-3 px-4">Evento</th>
                <th class="py-3 px-4">Fecha y Hora</th>
                <th class="py-3 px-4">Lugar</th>
                <th class="py-3 px-4">Estado</th>
                <th class="py-3 px-4 text-right">Detalle (1.1)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-stone-100">
              <tr>
                <td class="py-3 px-4 font-bold">#CTR-042</td>
                <td class="py-3 px-4 font-semibold text-stone-900"><a href="#adm-2-1" onclick="switchAdminView('adm-2-1')" class="underline">José Manuel Martínez</a></td>
                <td class="py-3 px-4">Boda Civil & Banquete</td>
                <td class="py-3 px-4">18/07/2026 21:00</td>
                <td class="py-3 px-4">Finca Almería Costa</td>
                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-green-100 text-green-800 font-bold">Aceptado</span></td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-1-1')" class="text-[#8B0000] font-bold hover:underline">Ver detalle</button></td>
              </tr>
              <tr>
                <td class="py-3 px-4 font-bold">#CTR-043</td>
                <td class="py-3 px-4 font-semibold text-stone-900">Colegio de Abogados</td>
                <td class="py-3 px-4">Gala Anual San Raimundo</td>
                <td class="py-3 px-4">24/09/2026 22:00</td>
                <td class="py-3 px-4">Teatro Cervantes</td>
                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-800 font-bold">Pendiente</span></td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-1-1')" class="text-[#8B0000] font-bold hover:underline">Ver detalle</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- ================= PANTALLA 1.1: VER CONTRATO EN DETALLE ================= -->
      <div id="adm-1-1" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <a href="#adm-1" onclick="switchAdminView('adm-1')" class="hover:text-stone-900">Gestionar contratos</a> › 
          <span class="text-stone-900 font-semibold">1.1 Ver contrato en detalle</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Contrato #CTR-042</h1>
          <p class="text-xs text-stone-500 mt-1">Datos de la solicitud y gestión de su estado</p>
        </div>

        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm text-xs space-y-6">
          <div class="grid md:grid-cols-2 gap-8">
            <div class="space-y-2.5 divide-y divide-stone-100">
              <div class="flex justify-between pt-1"><span class="text-stone-500">Cliente:</span><span><button onclick="switchAdminView('adm-2-1')" class="text-[#8B0000] font-bold underline">José Manuel Martínez</button></span></div>
              <div class="flex justify-between pt-2"><span class="text-stone-500">Evento:</span><span class="font-bold">Boda Civil & Banquete</span></div>
              <div class="flex justify-between pt-2"><span class="text-stone-500">Fecha y hora:</span><span>18/07/2026 21:00</span></div>
              <div class="flex justify-between pt-2"><span class="text-stone-500">Lugar:</span><span>Finca Almería Costa</span></div>
              <div class="flex justify-between pt-2"><span class="text-stone-500">Asistentes previstos:</span><span>120 personas</span></div>
              <div class="flex justify-between pt-2"><span class="text-stone-500">Observaciones:</span><span>Piden sorpresa a la novia con Clavelitos</span></div>
              <div class="flex justify-between pt-2"><span class="text-stone-500">Importe total:</span><span class="font-black text-[#8B0000] text-sm">450 €</span></div>
            </div>

            <div class="space-y-4 bg-stone-50 p-4 rounded-xl border border-stone-200">
              <label class="block">
                <span class="font-bold text-stone-700 block mb-1">Estado del contrato</span>
                <select id="adm-ctr-state" class="w-full h-9 px-3 border border-stone-300 rounded bg-white font-semibold">
                  <option>Pendiente</option>
                  <option selected>Aceptado</option>
                  <option>Rechazado</option>
                  <option>Realizado</option>
                </select>
              </label>

              <button type="button" onclick="document.getElementById('adm-box-confirm').classList.remove('hidden');" class="px-5 py-2.5 bg-stone-900 hover:bg-stone-800 text-white font-bold rounded uppercase">
                Guardar estado
              </button>

              <div id="adm-box-confirm" class="hidden p-3 bg-white border border-stone-300 rounded text-stone-800 flex items-center gap-2">
                <span class="px-2 py-0.5 bg-stone-200 text-stone-700 font-bold text-[10px] uppercase rounded">Confirmación</span>
                <span>«Estado actualizado con éxito»</span>
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-stone-200">
            <button onclick="switchAdminView('adm-1')" class="px-4 py-2 border border-stone-300 rounded font-bold text-stone-700 hover:bg-stone-50">
              ← Volver al listado de contratos
            </button>
          </div>
        </div>
      </div>

      <!-- ================= PANTALLA 2: GESTIONAR CARTERA DE CLIENTES ================= -->
      <div id="adm-2" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <span class="text-stone-900 font-semibold">2 Gestionar cartera de clientes</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Cartera de clientes</h1>
          <p class="text-xs text-stone-500 mt-1">Historial y fichas de clientes registrados</p>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm text-xs">
          <table class="w-full text-left">
            <thead class="bg-stone-50 border-b border-stone-200 text-stone-500 uppercase font-bold">
              <tr>
                <th class="py-3 px-4">Cliente</th>
                <th class="py-3 px-4">Correo</th>
                <th class="py-3 px-4">Teléfono</th>
                <th class="py-3 px-4">Ciudad</th>
                <th class="py-3 px-4 text-right">Ficha (2.1)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-stone-100">
              <tr>
                <td class="py-3 px-4 font-bold text-stone-900">José Manuel Martínez</td>
                <td class="py-3 px-4">cliente@almeria.es</td>
                <td class="py-3 px-4 font-mono">612 345 678</td>
                <td class="py-3 px-4">Almería</td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-2-1')" class="text-[#8B0000] font-bold hover:underline">Ver ficha</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- ================= PANTALLA 2.1: VER FICHA DE CLIENTE ================= -->
      <div id="adm-2-1" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <a href="#adm-2" onclick="switchAdminView('adm-2')" class="hover:text-stone-900">Cartera de clientes</a> › 
          <span class="text-stone-900 font-semibold">2.1 Ficha de cliente</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Ficha de cliente: José Manuel Martínez</h1>
          <p class="text-xs text-stone-500 mt-1">Datos personales y actividad asociada en la tuna</p>
        </div>

        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm text-xs space-y-6">
          <div class="grid sm:grid-cols-2 gap-4">
            <div><span class="text-stone-500 block">Correo:</span><strong class="text-sm">cliente@almeria.es</strong></div>
            <div><span class="text-stone-500 block">Teléfono:</span><strong class="text-sm">612 345 678</strong></div>
            <div><span class="text-stone-500 block">Dirección:</span><strong>Avda. del Mediterráneo 120, Almería</strong></div>
            <div><span class="text-stone-500 block">Fecha de alta:</span><strong>14/01/2025</strong></div>
          </div>

          <div class="pt-4 border-t border-stone-200 flex flex-wrap gap-4">
            <button onclick="switchAdminView('adm-1')" class="px-4 py-2 bg-stone-900 text-white rounded font-bold">
              2.1.1 Ver contratos del cliente (1 activo)
            </button>
            <button onclick="switchAdminView('adm-3')" class="px-4 py-2 bg-[#8B0000] text-amber-200 rounded font-bold">
              2.1.2 Ver pedidos del cliente (1 en tienda)
            </button>
          </div>
        </div>
      </div>

      <!-- ================= PANTALLA 3: GESTIONAR PEDIDOS DE LA TIENDA ================= -->
      <div id="adm-3" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <span class="text-stone-900 font-semibold">3 Pedidos de la tienda</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Gestionar pedidos de la tienda</h1>
          <p class="text-xs text-stone-500 mt-1">Supervisión de compras de merchandising y envíos</p>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm text-xs">
          <table class="w-full text-left">
            <thead class="bg-stone-50 border-b border-stone-200 text-stone-500 uppercase font-bold">
              <tr>
                <th class="py-3 px-4">Nº Pedido</th>
                <th class="py-3 px-4">Cliente</th>
                <th class="py-3 px-4">Fecha</th>
                <th class="py-3 px-4">Total</th>
                <th class="py-3 px-4">Estado</th>
                <th class="py-3 px-4 text-right">Detalle (3.1)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-stone-100">
              <tr>
                <td class="py-3 px-4 font-bold">#PED-894</td>
                <td class="py-3 px-4 font-semibold text-stone-900">José Manuel Martínez</td>
                <td class="py-3 px-4">02/03/2026</td>
                <td class="py-3 px-4 font-bold">34,50 €</td>
                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold">Enviado</span></td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-3-1')" class="text-[#8B0000] font-bold hover:underline">Ver detalle</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- ================= PANTALLA 3.1: VER PEDIDO EN DETALLE ================= -->
      <div id="adm-3-1" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <a href="#adm-3" onclick="switchAdminView('adm-3')" class="hover:text-stone-900">Pedidos de la tienda</a> › 
          <span class="text-stone-900 font-semibold">3.1 Ver pedido en detalle</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Pedido #PED-894</h1>
          <p class="text-xs text-stone-500 mt-1">Gestión del estado de envío y seguimiento</p>
        </div>

        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm text-xs space-y-4 max-w-2xl">
          <div class="space-y-2">
            <div class="flex justify-between"><span class="text-stone-500">Cliente:</span><span class="font-bold">José Manuel Martínez</span></div>
            <div class="flex justify-between"><span class="text-stone-500">Destino:</span><span>Avda. del Mediterráneo 120, Almería</span></div>
            <div class="flex justify-between"><span class="text-stone-500">Artículos:</span><span>1x Sudadera Roja (L), 1x Parche Beca Oro</span></div>
            <div class="flex justify-between"><span class="text-stone-500">Total:</span><span class="font-black text-[#8B0000] text-sm">34,50 €</span></div>
          </div>

          <div class="pt-3 border-t border-stone-200 space-y-3 bg-stone-50 p-4 rounded-xl">
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Estado del envío</label>
              <select class="w-full h-8 px-2 border border-stone-300 rounded bg-white">
                <option>Preparando</option>
                <option selected>Enviado</option>
                <option>Entregado</option>
              </select>
            </div>
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Tracking Correos</label>
              <input type="text" value="ES98374829104AL" class="w-full h-8 px-2 border border-stone-300 rounded bg-white font-mono">
            </div>
            <button onclick="alert('Pedido #PED-894 actualizado.');" class="px-4 py-2 bg-stone-900 text-white font-bold rounded">
              Actualizar Pedido
            </button>
          </div>
        </div>
      </div>

      <!-- ================= PANTALLA 4: GESTIONAR PRODUCTOS DE LA TIENDA ================= -->
      <div id="adm-4" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <span class="text-stone-900 font-semibold">4 Productos de la tienda</span>
        </nav>
        <div class="flex justify-between items-center">
          <div>
            <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Productos de la tienda</h1>
            <p class="text-xs text-stone-500 mt-1">Gestión del catálogo de merchandising</p>
          </div>
          <button onclick="switchAdminView('adm-4-1')" class="px-4 py-2 bg-[#8B0000] text-amber-200 font-bold rounded-lg text-xs uppercase tracking-wider shadow">
            + 4.1 Añadir Producto
          </button>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm text-xs">
          <table class="w-full text-left">
            <thead class="bg-stone-50 border-b border-stone-200 text-stone-500 uppercase font-bold">
              <tr>
                <th class="py-3 px-4">Producto</th>
                <th class="py-3 px-4">Categoría</th>
                <th class="py-3 px-4">Precio</th>
                <th class="py-3 px-4">Stock</th>
                <th class="py-3 px-4 text-right">Acción (4.2)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-stone-100">
              <tr>
                <td class="py-3 px-4 font-bold text-stone-900">Sudadera Roja Tuna Derecho</td>
                <td class="py-3 px-4">Ropa Oficial</td>
                <td class="py-3 px-4 font-bold text-[#8B0000]">28,00 €</td>
                <td class="py-3 px-4">42 unidades</td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-4-2')" class="text-blue-700 font-bold hover:underline">Modificar/Eliminar</button></td>
              </tr>
              <tr>
                <td class="py-3 px-4 font-bold text-stone-900">CD "25 Años de Ronda"</td>
                <td class="py-3 px-4">Música</td>
                <td class="py-3 px-4 font-bold text-[#8B0000]">12,00 €</td>
                <td class="py-3 px-4">80 unidades</td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-4-2')" class="text-blue-700 font-bold hover:underline">Modificar/Eliminar</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- ================= PANTALLA 4.1: AÑADIR PRODUCTO ================= -->
      <div id="adm-4-1" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <a href="#adm-4" onclick="switchAdminView('adm-4')" class="hover:text-stone-900">Productos</a> › 
          <span class="text-stone-900 font-semibold">4.1 Añadir producto</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Añadir producto</h1>
          <p class="text-xs text-stone-500 mt-1">Registra un nuevo artículo en la tienda oficial</p>
        </div>

        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-lg text-xs space-y-3">
          <form onsubmit="alert('«Producto añadido al catálogo con éxito»'); switchAdminView('adm-4'); return false;" class="space-y-3">
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Nombre del producto *</label>
              <input type="text" required placeholder="Ej. Camiseta Oficial 30 Aniversario" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            </div>
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Categoría</label>
                <select class="w-full px-3 py-2 border border-stone-300 rounded outline-none bg-white">
                  <option>Ropa</option>
                  <option>Música</option>
                  <option>Accesorios</option>
                </select>
              </div>
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Precio (€) *</label>
                <input type="number" step="0.5" required placeholder="15.00" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
              </div>
            </div>
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Stock inicial *</label>
              <input type="number" required placeholder="50" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            </div>
            <button type="submit" class="w-full py-2.5 bg-[#8B0000] text-amber-200 font-bold rounded uppercase">
              Guardar y Publicar Producto
            </button>
          </form>
        </div>
      </div>

      <!-- ================= PANTALLA 4.2: MODIFICAR O ELIMINAR PRODUCTO ================= -->
      <div id="adm-4-2" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <a href="#adm-4" onclick="switchAdminView('adm-4')" class="hover:text-stone-900">Productos</a> › 
          <span class="text-stone-900 font-semibold">4.2 Modificar o eliminar producto</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Modificar producto</h1>
          <p class="text-xs text-stone-500 mt-1">Edición de datos o baja del catálogo</p>
        </div>

        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-lg text-xs space-y-4">
          <form onsubmit="alert('«Producto modificado correctamente»'); switchAdminView('adm-4'); return false;" class="space-y-3">
            <input type="text" value="Sudadera Roja Tuna Derecho" class="w-full px-3 py-2 border border-stone-300 rounded font-bold">
            <input type="number" value="28.00" step="0.5" class="w-full px-3 py-2 border border-stone-300 rounded">
            <input type="number" value="42" class="w-full px-3 py-2 border border-stone-300 rounded">
            <div class="flex gap-2 pt-2">
              <button type="submit" class="flex-1 py-2 bg-stone-900 text-white font-bold rounded">Guardar Cambios</button>
              <button type="button" onclick="alert('«Producto eliminado del catálogo»'); switchAdminView('adm-4');" class="px-4 py-2 bg-red-800 text-white font-bold rounded">Eliminar</button>
            </div>
          </form>
        </div>
      </div>

      <!-- ================= PANTALLA 5: LISTA DE MIEMBROS ================= -->
      <div id="adm-5" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <span class="text-stone-900 font-semibold">5 Lista de miembros</span>
        </nav>
        <div class="flex justify-between items-center">
          <div>
            <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Lista de miembros</h1>
            <p class="text-xs text-stone-500 mt-1">Cuadrilla activa de la Tuna de Derecho</p>
          </div>
          <button onclick="switchAdminView('adm-5-2')" class="px-4 py-2 bg-[#8B0000] text-amber-200 font-bold rounded-lg text-xs uppercase tracking-wider shadow">
            + 5.2 Añadir Nuevo Miembro
          </button>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm text-xs">
          <table class="w-full text-left">
            <thead class="bg-stone-50 border-b border-stone-200 text-stone-500 uppercase font-bold">
              <tr>
                <th class="py-3 px-4">Nombre y Mote</th>
                <th class="py-3 px-4">Rango</th>
                <th class="py-3 px-4">Instrumento</th>
                <th class="py-3 px-4">Teléfono</th>
                <th class="py-3 px-4 text-right">Acción (5.1)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-stone-100">
              <tr>
                <td class="py-3 px-4 font-bold text-stone-900">Javier Fernández "El Jurisconsulto"</td>
                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-red-100 text-[#8B0000] font-bold">Tuno Mayor</span></td>
                <td class="py-3 px-4">Bandurria</td>
                <td class="py-3 px-4 font-mono">600 123 456</td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-5-1')" class="text-blue-700 font-bold hover:underline">Modificar</button></td>
              </tr>
              <tr>
                <td class="py-3 px-4 font-bold text-stone-900">Carlos López "El Pasante"</td>
                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-bold">Novato / Pardillo</span></td>
                <td class="py-3 px-4">Pandereta</td>
                <td class="py-3 px-4 font-mono">644 112 233</td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-5-1')" class="text-blue-700 font-bold hover:underline">Modificar</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- ================= PANTALLA 5.1 & 5.2: GESTIÓN DE MIEMBRO ================= -->
      <div id="adm-5-1" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <a href="#adm-5" onclick="switchAdminView('adm-5')" class="hover:text-stone-900">Miembros</a> › 
          <span class="text-stone-900 font-semibold">5.1 Modificar miembro</span>
        </nav>
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-3">
          <h2 class="font-serif-tuna font-bold text-xl text-stone-900">Modificar datos del miembro</h2>
          <input type="text" value="Javier Fernández" class="w-full px-3 py-2 border border-stone-300 rounded font-bold">
          <input type="text" value="El Jurisconsulto" class="w-full px-3 py-2 border border-stone-300 rounded">
          <select class="w-full px-3 py-2 border border-stone-300 rounded bg-white font-bold text-[#8B0000]">
            <option selected>Tuno Mayor</option>
            <option>Tuno</option>
            <option>Novato</option>
          </select>
          <button onclick="alert('«Datos de miembro actualizados»'); switchAdminView('adm-5');" class="w-full py-2 bg-stone-900 text-white font-bold rounded">Guardar Cambios</button>
        </div>
      </div>

      <div id="adm-5-2" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <a href="#adm-5" onclick="switchAdminView('adm-5')" class="hover:text-stone-900">Miembros</a> › 
          <span class="text-stone-900 font-semibold">5.2 Añadir nuevo miembro</span>
        </nav>
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-3">
          <h2 class="font-serif-tuna font-bold text-xl text-stone-900">Añadir nuevo miembro / novato</h2>
          <input type="text" placeholder="Nombre completo" required class="w-full px-3 py-2 border border-stone-300 rounded">
          <input type="text" placeholder="Apodo / Mote tunantesco" class="w-full px-3 py-2 border border-stone-300 rounded">
          <input type="text" placeholder="Instrumento principal" class="w-full px-3 py-2 border border-stone-300 rounded">
          <button onclick="alert('«Nuevo miembro añadido a la cuadrilla»'); switchAdminView('adm-5');" class="w-full py-2 bg-[#8B0000] text-amber-200 font-bold rounded">Registrar Miembro</button>
        </div>
      </div>

      <!-- ================= PANTALLA 6: GESTIONAR CUENTA ================= -->
      <div id="adm-6" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <span class="text-stone-900 font-semibold">6 Cuenta</span>
        </nav>
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Gestionar cuenta</h1>
          <p class="text-xs text-stone-500 mt-1">Configuración del perfil de administrador</p>
        </div>

        <div class="grid sm:grid-cols-2 gap-6 text-xs">
          <div onclick="switchAdminView('adm-6-1')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm">
            <span class="text-3xl mb-2 block">👤</span>
            <h3 class="font-serif-tuna font-bold text-base text-stone-900">6.1 Modificar información personal</h3>
            <p class="text-stone-500 mt-1">Nombre, teléfono y correo administrativo.</p>
          </div>
          <div onclick="switchAdminView('adm-6-2')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm">
            <span class="text-3xl mb-2 block">🔒</span>
            <h3 class="font-serif-tuna font-bold text-base text-stone-900">6.2 Cambiar contraseña</h3>
            <p class="text-stone-500 mt-1">Actualizar clave de acceso seguro.</p>
          </div>
        </div>
      </div>

      <div id="adm-6-1" class="admin-subview hidden space-y-6">
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-3">
          <h2 class="font-serif-tuna font-bold text-xl text-stone-900">6.1 Información Personal</h2>
          <input type="text" value="Javier Fernández" class="w-full px-3 py-2 border border-stone-300 rounded font-bold">
          <input type="email" value="tuna.derecho.almeria@gmail.com" class="w-full px-3 py-2 border border-stone-300 rounded">
          <button onclick="alert('«Información administrativa actualizada»'); switchAdminView('adm-6');" class="w-full py-2 bg-stone-900 text-white font-bold rounded">Guardar Cambios</button>
        </div>
      </div>

      <div id="adm-6-2" class="admin-subview hidden space-y-6">
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-3">
          <h2 class="font-serif-tuna font-bold text-xl text-stone-900">6.2 Cambiar Contraseña</h2>
          <input type="password" value="********" class="w-full px-3 py-2 border border-stone-300 rounded">
          <input type="password" placeholder="Nueva contraseña de administrador" class="w-full px-3 py-2 border border-stone-300 rounded">
          <button onclick="alert('«Contraseña administrativa actualizada»'); switchAdminView('adm-6');" class="w-full py-2 bg-[#8B0000] text-amber-200 font-bold rounded">Actualizar Clave</button>
        </div>
      </div>

      <!-- ================= PANTALLA 7: GESTIONAR CERTÁMENES ================= -->
      <div id="adm-7" class="admin-subview hidden space-y-6">
        <nav class="text-xs text-stone-500">
          <a href="#adm-0" onclick="switchAdminView('adm-0')" class="hover:text-stone-900">Panel</a> › 
          <span class="text-stone-900 font-semibold">7 Gestionar certámenes</span>
        </nav>
        <div class="flex justify-between items-center">
          <div>
            <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Gestionar certámenes</h1>
            <p class="text-xs text-stone-500 mt-1">Palmarés, festivales y premios de la Tuna</p>
          </div>
          <button onclick="switchAdminView('adm-7-2')" class="px-4 py-2 bg-[#8B0000] text-amber-200 font-bold rounded-lg text-xs uppercase tracking-wider shadow">
            + 7.2 Crear Nuevo Certamen
          </button>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm text-xs">
          <table class="w-full text-left">
            <thead class="bg-stone-50 border-b border-stone-200 text-stone-500 uppercase font-bold">
              <tr>
                <th class="py-3 px-4">Año</th>
                <th class="py-3 px-4">Certamen</th>
                <th class="py-3 px-4">Ciudad</th>
                <th class="py-3 px-4">Premio</th>
                <th class="py-3 px-4 text-right">Acción (7.1)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-stone-100">
              <tr>
                <td class="py-3 px-4 font-bold">2024</td>
                <td class="py-3 px-4 font-semibold text-stone-900">Certamen Nacional de Tunas de Derecho</td>
                <td class="py-3 px-4">Salamanca</td>
                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-bold">🏆 1º Premio Mejor Tuna</span></td>
                <td class="py-3 px-4 text-right"><button onclick="switchAdminView('adm-7-1')" class="text-blue-700 font-bold hover:underline">Modificar</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div id="adm-7-1" class="admin-subview hidden space-y-6">
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-3">
          <h2 class="font-serif-tuna font-bold text-xl text-stone-900">7.1 Modificar Certamen</h2>
          <input type="text" value="Certamen Nacional de Tunas de Derecho" class="w-full px-3 py-2 border border-stone-300 rounded font-bold">
          <input type="text" value="Salamanca" class="w-full px-3 py-2 border border-stone-300 rounded">
          <input type="text" value="1º Premio Mejor Tuna" class="w-full px-3 py-2 border border-stone-300 rounded">
          <button onclick="alert('«Certamen actualizado correctamente»'); switchAdminView('adm-7');" class="w-full py-2 bg-stone-900 text-white font-bold rounded">Guardar Cambios</button>
        </div>
      </div>

      <div id="adm-7-2" class="admin-subview hidden space-y-6">
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-3">
          <h2 class="font-serif-tuna font-bold text-xl text-stone-900">7.2 Registrar Nuevo Certamen</h2>
          <input type="text" placeholder="Nombre del certamen" required class="w-full px-3 py-2 border border-stone-300 rounded">
          <input type="text" placeholder="Ciudad" required class="w-full px-3 py-2 border border-stone-300 rounded">
          <input type="number" placeholder="Año" value="2026" class="w-full px-3 py-2 border border-stone-300 rounded">
          <input type="text" placeholder="Premios conseguidos" class="w-full px-3 py-2 border border-stone-300 rounded">
          <button onclick="alert('«Nuevo certamen registrado con éxito»'); switchAdminView('adm-7');" class="w-full py-2 bg-[#8B0000] text-amber-200 font-bold rounded">Registrar Certamen</button>
        </div>
      </div>

    </main>
  </div>

  <!-- SCRIPT ADMIN -->
  <script>
    function switchAdminView(viewId) {
      document.querySelectorAll('.admin-subview').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.subview-pill').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.admin-menu-item').forEach(el => el.classList.remove('active'));

      const target = document.getElementById(viewId);
      if (target) {
        target.classList.remove('hidden');
        window.scrollTo({ top: 90, behavior: 'smooth' });
      }

      // Marcar píldora
      const btn = Array.from(document.querySelectorAll('.subview-pill')).find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes(viewId));
      if (btn) btn.classList.add('active');

      // Marcar sidebar
      if (viewId === 'adm-0') document.getElementById('side-0').classList.add('active');
      if (viewId.startsWith('adm-1')) document.getElementById('side-1').classList.add('active');
      if (viewId.startsWith('adm-2')) document.getElementById('side-2').classList.add('active');
      if (viewId.startsWith('adm-3')) document.getElementById('side-3').classList.add('active');
      if (viewId.startsWith('adm-4')) document.getElementById('side-4').classList.add('active');
      if (viewId.startsWith('adm-5')) document.getElementById('side-5').classList.add('active');
      if (viewId.startsWith('adm-6')) document.getElementById('side-6').classList.add('active');
      if (viewId.startsWith('adm-7')) document.getElementById('side-7').classList.add('active');
    }
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    content = get_admin_html()
    target = r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\admin.html"
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Guardado:", target)

