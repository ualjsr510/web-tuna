# -*- coding: utf-8 -*-
"""
Generador del Mockup para CLIENTE (cliente.html)
Fiel a los 10 wireframes de Cliente:
- 0 Inicio de cliente (index.html)
- 1 Ver historial de contratos (Contratos.html)
- 1.1 Ver contrato en detalle (ContratoDetalle.html)
- 2 Ver historial de pedidos (Pedidos.html)
- 2.1 Ver pedido en detalle (PedidoDetalle.html)
- 2.1.1 Editar datos del pedido (PedidoEditar.html)
- 2.1.2 Tramitar devolución (PedidoDevolucion.html)
- 3 Gestionar cuenta (Cuenta.html)
- 3.1 Modificar información personal (CuentaDatos.html)
- 3.2 Cambiar contraseña (CuentaPassword.html)
"""

def get_cliente_html():
    return """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería · Área de Cliente</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {
      --rojo-tuna: #8B0000;
      --rojo-oscuro: #5C0000;
      --dorado: #D4AF37;
      --fondo-crema: #FAF8F5;
    }
    body {
      background-color: var(--fondo-crema);
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
    .subview-pill.active {
      background-color: #8B0000;
      color: #FFFFFF;
      font-weight: 700;
      border-color: #5C0000;
    }
    .client-nav-btn.active {
      color: #8B0000;
      font-weight: 700;
      border-bottom: 2px solid #8B0000;
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
          <span class="text-amber-400 font-bold tracking-wider uppercase text-[10px] block">MOCKUP 2 DE 3 · PERFIL ACTUAL: CLIENTE</span>
          <span class="text-slate-300 text-[11px]">Tuna de la Facultad de Derecho de Almería</span>
        </div>
      </div>

      <!-- Selector para cambiar de mockup -->
      <div class="flex items-center bg-[#1f1f1f] p-1 rounded-xl border border-slate-700">
        <a href="visitante.html" class="px-3.5 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white transition flex items-center gap-1.5">
          <span>🌐</span> Visitante <span class="text-[10px] opacity-75">(Público)</span>
        </a>
        <a href="cliente.html" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#8B0000] border-b-2 border-[#D4AF37] shadow flex items-center gap-1.5">
          <span>👤</span> Cliente <span class="text-[10px] opacity-75">(Registrado)</span>
        </a>
        <a href="admin.html" class="px-3.5 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white transition flex items-center gap-1.5">
          <span>⚙️</span> Administrador <span class="text-[10px] opacity-75">(Gestión)</span>
        </a>
      </div>

      <!-- Teléfono directo en cabecera -->
      <div class="hidden lg:flex items-center gap-3">
        <a href="tel:+34600123456" class="flex items-center gap-1.5 px-3 py-1 bg-red-900 hover:bg-red-800 text-amber-200 rounded-full font-bold border border-amber-400/80 shadow pulse-call">
          <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          Atención Clientes: +34 600 123 456
        </a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- BARRA DE CONTACTO CORPORATIVA Y REDES SOCIALES (ULTRA-VISIBLE) -->
  <!-- ========================================================================= -->
  <div class="bg-[#5C0000] text-white border-b-2 border-[#D4AF37] py-2.5 px-4 text-xs shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex flex-wrap items-center gap-4 sm:gap-6">
        <a href="tel:+34600123456" class="flex items-center gap-2 font-black text-sm text-amber-300 hover:text-amber-200 transition">
          <span class="p-1 bg-red-950 rounded-full">📞</span>
          TELÉFONOS DE CONTACTO: +34 600 123 456 · +34 612 345 678
        </a>
        <a href="mailto:tuna.derecho.almeria@gmail.com" class="flex items-center gap-1.5 text-slate-200 hover:text-amber-300 transition">
          <span>✉️</span> tuna.derecho.almeria@gmail.com
        </a>
      </div>

      <!-- Enlaces sociales con badges -->
      <div class="flex items-center gap-2 sm:gap-3">
        <span class="badge-editorial text-amber-300 hidden md:inline">Redes Oficiales:</span>
        <a href="https://instagram.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-pink-700 transition text-[11px] font-bold text-white flex items-center gap-1">
          <span>📷</span> @tunaderechoalmeria
        </a>
        <a href="https://tiktok.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-black transition text-[11px] font-bold text-white flex items-center gap-1">
          <span>🎵</span> TikTok
        </a>
        <a href="https://facebook.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-blue-700 transition text-[11px] font-bold text-white flex items-center gap-1">
          <span>👥</span> Facebook
        </a>
        <a href="https://spotify.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-green-700 transition text-[11px] font-bold text-white flex items-center gap-1">
          <span>🟢</span> Spotify
        </a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- HEADER FIEL AL WIREFRAME DE CLIENTE (LOGO TUNA + NAV: INICIO, CONTRATOS, PEDIDOS, CUENTA) -->
  <!-- ========================================================================= -->
  <header class="bg-white border-b border-stone-200 sticky top-12 z-40 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between gap-4">
      
      <!-- Logo TUNA -->
      <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-full bg-[#8B0000] border border-[#D4AF37] flex items-center justify-center text-amber-300 font-serif-tuna font-bold text-base shadow">
          TD
        </div>
        <div>
          <div class="font-serif-tuna font-bold text-lg text-[#5C0000] leading-none">TUNA DE DERECHO</div>
          <div class="badge-editorial text-[#8B0000] text-[8px] mt-0.5 font-bold">Área de Cliente Registrado</div>
        </div>
      </a>

      <!-- Navegación Fiel a cliente/index.html wireframe -->
      <nav class="flex items-center gap-6 text-[13px] font-medium text-stone-700">
        <button onclick="switchClientView('c-view-0')" id="c-nav-0" class="client-nav-btn active hover:text-[#8B0000] transition py-1">Inicio</button>
        <button onclick="switchClientView('c-view-1')" id="c-nav-1" class="client-nav-btn hover:text-[#8B0000] transition py-1">1 Contratos</button>
        <button onclick="switchClientView('c-view-2')" id="c-nav-2" class="client-nav-btn hover:text-[#8B0000] transition py-1">2 Pedidos</button>
        <button onclick="switchClientView('c-view-3')" id="c-nav-3" class="client-nav-btn hover:text-[#8B0000] transition py-1">3 Cuenta</button>
      </nav>

      <!-- Usuario y Cerrar sesión -->
      <div class="flex items-center gap-3 text-xs">
        <span class="text-stone-600 hidden sm:inline font-semibold">José Manuel Martínez</span>
        <a href="visitante.html" class="px-3 py-1.5 border border-stone-300 rounded font-bold text-stone-700 hover:bg-stone-50 transition">
          Cerrar sesión
        </a>
      </div>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- BARRA DE PANTALLAS DEL WIREFRAME CLIENTE (10 PANTALLAS) -->
  <!-- ========================================================================= -->
  <div class="bg-stone-100 border-b border-stone-300 py-2 px-4 text-xs overflow-x-auto whitespace-nowrap shadow-inner">
    <div class="max-w-7xl mx-auto flex items-center gap-2">
      <span class="font-bold text-stone-500 uppercase tracking-wider text-[10px] mr-1">Pantallas Wireframe Cliente:</span>
      <button onclick="switchClientView('c-view-0')" class="subview-pill active px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">0. Inicio Cliente</button>
      <button onclick="switchClientView('c-view-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">1. Historial Contratos</button>
      <button onclick="switchClientView('c-view-1-detail')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">1.1 Contrato en Detalle</button>
      <button onclick="switchClientView('c-view-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2. Historial Pedidos</button>
      <button onclick="switchClientView('c-view-2-detail')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2.1 Pedido en Detalle</button>
      <button onclick="switchClientView('c-view-2-edit')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2.1.1 Editar Datos Pedido</button>
      <button onclick="switchClientView('c-view-2-devolucion')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2.1.2 Tramitar Devolución</button>
      <button onclick="switchClientView('c-view-3')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3. Gestionar Cuenta</button>
      <button onclick="switchClientView('c-view-3-datos')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3.1 Información Personal</button>
      <button onclick="switchClientView('c-view-3-pass')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3.2 Cambiar Contraseña</button>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- CONTENEDOR PRINCIPAL: PANTALLAS INTERACTIVAS CLIENTE -->
  <!-- ========================================================================= -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-8">

    <!-- ================= PANTALLA 0: INICIO DE CLIENTE ================= -->
    <div id="c-view-0" class="client-subview-content space-y-8">
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Hola, José Manuel Martínez</h1>
        <p class="text-xs text-stone-500 mt-1">Tu área de cliente en la Tuna de Derecho de Almería</p>
      </div>

      <!-- Las 3 Tarjetas Principales Fieles al Wireframe cliente/index.html -->
      <section class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- 1 Historial contratos -->
        <div onclick="switchClientView('c-view-1')" class="bg-white p-5 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition flex flex-col justify-between group">
          <div>
            <div class="h-28 bg-red-100/70 border border-red-200 rounded-lg flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">📜</div>
            <h3 class="font-serif-tuna font-bold text-base text-stone-900">1 Ver historial de contratos</h3>
            <p class="text-xs text-stone-600 mt-1">Tus solicitudes de contratación para actuaciones y eventos.</p>
          </div>
          <span class="text-[#8B0000] font-bold text-xs mt-3 block">Acceder a contratos →</span>
        </div>

        <!-- 2 Historial pedidos -->
        <div onclick="switchClientView('c-view-2')" class="bg-white p-5 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition flex flex-col justify-between group">
          <div>
            <div class="h-28 bg-amber-100/70 border border-amber-200 rounded-lg flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">🛍️</div>
            <h3 class="font-serif-tuna font-bold text-base text-stone-900">2 Ver historial de pedidos</h3>
            <p class="text-xs text-stone-600 mt-1">Tus compras y artículos de merchandising oficial.</p>
          </div>
          <span class="text-[#8B0000] font-bold text-xs mt-3 block">Acceder a pedidos →</span>
        </div>

        <!-- 3 Gestionar cuenta -->
        <div onclick="switchClientView('c-view-3')" class="bg-white p-5 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition flex flex-col justify-between group">
          <div>
            <div class="h-28 bg-stone-100 border border-stone-200 rounded-lg flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">⚙️</div>
            <h3 class="font-serif-tuna font-bold text-base text-stone-900">3 Gestionar cuenta</h3>
            <p class="text-xs text-stone-600 mt-1">Tus datos personales y cambio de contraseña.</p>
          </div>
          <span class="text-[#8B0000] font-bold text-xs mt-3 block">Configurar perfil →</span>
        </div>
      </section>

      <!-- Bloques de Resumen Inferior (Último Contrato y Último Pedido) Fiel a Wireframe -->
      <section class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Último contrato -->
        <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm space-y-3">
          <h2 class="font-serif-tuna font-bold text-base text-stone-900">Último contrato</h2>
          <table class="w-full text-left text-xs border border-stone-200 rounded overflow-hidden">
            <thead class="bg-stone-50 border-b border-stone-200">
              <tr>
                <th class="py-2.5 px-3">Nº</th>
                <th class="py-2.5 px-3">Evento</th>
                <th class="py-2.5 px-3">Estado</th>
                <th class="py-2.5 px-3 text-right">Acción</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="py-2.5 px-3 font-bold">#CTR-042</td>
                <td class="py-2.5 px-3">Boda Civil & Banquete</td>
                <td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded bg-green-100 text-green-800 font-bold">Confirmado</span></td>
                <td class="py-2.5 px-3 text-right"><button onclick="switchClientView('c-view-1-detail')" class="text-[#8B0000] font-bold hover:underline">Ver</button></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Último pedido -->
        <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm space-y-3">
          <h2 class="font-serif-tuna font-bold text-base text-stone-900">Último pedido</h2>
          <table class="w-full text-left text-xs border border-stone-200 rounded overflow-hidden">
            <thead class="bg-stone-50 border-b border-stone-200">
              <tr>
                <th class="py-2.5 px-3">Nº</th>
                <th class="py-2.5 px-3">Total</th>
                <th class="py-2.5 px-3">Estado</th>
                <th class="py-2.5 px-3 text-right">Acción</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="py-2.5 px-3 font-bold">#PED-894</td>
                <td class="py-2.5 px-3 font-bold">34,50 €</td>
                <td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold">Enviado</span></td>
                <td class="py-2.5 px-3 text-right"><button onclick="switchClientView('c-view-2-detail')" class="text-[#8B0000] font-bold hover:underline">Ver</button></td>
              </tr>
            </tbody>
          </table>
        </div>

      </section>
    </div>

    <!-- ================= PANTALLA 1: HISTORIAL DE CONTRATOS ================= -->
    <div id="c-view-1" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">1 Contratos</span>
      </nav>
      <div class="flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Historial de contratos</h1>
          <p class="text-xs text-stone-500 mt-1">Tus solicitudes de contratación de la Tuna de Derecho</p>
        </div>
        <a href="visitante.html#view-2-form" class="px-4 py-2 bg-[#8B0000] text-amber-200 font-bold text-xs uppercase tracking-wider rounded-lg shadow">
          + Solicitar Nueva Actuación
        </a>
      </div>

      <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
        <table class="w-full text-left text-xs">
          <thead class="bg-stone-50 text-stone-500 uppercase font-bold border-b border-stone-200">
            <tr>
              <th class="py-3 px-4">Nº Contrato</th>
              <th class="py-3 px-4">Evento</th>
              <th class="py-3 px-4">Fecha y Hora</th>
              <th class="py-3 px-4">Lugar</th>
              <th class="py-3 px-4">Asistentes</th>
              <th class="py-3 px-4">Estado</th>
              <th class="py-3 px-4 text-right">Detalle (1.1)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-stone-100">
            <tr>
              <td class="py-3 px-4 font-bold">#CTR-042</td>
              <td class="py-3 px-4 font-semibold text-stone-900">Boda Civil & Banquete</td>
              <td class="py-3 px-4">18/07/2026 21:00</td>
              <td class="py-3 px-4">Finca Almería Costa</td>
              <td class="py-3 px-4">120</td>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-green-100 text-green-800 font-bold">Confirmado</span></td>
              <td class="py-3 px-4 text-right">
                <button onclick="switchClientView('c-view-1-detail')" class="text-[#8B0000] font-bold hover:underline">Ver detalle</button>
              </td>
            </tr>
            <tr>
              <td class="py-3 px-4 font-bold">#CTR-019</td>
              <td class="py-3 px-4 font-semibold text-stone-900">Serenata de Balcón Sorpresa</td>
              <td class="py-3 px-4">14/02/2025 23:30</td>
              <td class="py-3 px-4">Casco Histórico, Almería</td>
              <td class="py-3 px-4">15</td>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-stone-100 text-stone-700 font-bold">Realizado</span></td>
              <td class="py-3 px-4 text-right">
                <button onclick="switchClientView('c-view-1-detail')" class="text-[#8B0000] font-bold hover:underline">Ver detalle</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= PANTALLA 1.1: CONTRATO EN DETALLE ================= -->
    <div id="c-view-1-detail" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#c-view-1" onclick="switchClientView('c-view-1')" class="hover:text-stone-900">1 Contratos</a> › 
        <span class="text-stone-900 font-semibold">1.1 Ver contrato en detalle</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Contrato #CTR-042</h1>
        <p class="text-xs text-stone-500 mt-1">Ficha completa de la solicitud de actuación</p>
      </div>

      <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-2xl text-xs space-y-4">
        <div class="flex justify-between items-center pb-3 border-b border-stone-200">
          <span class="font-bold text-stone-500 uppercase">Estado del Contrato:</span>
          <span class="px-3 py-1 rounded bg-green-100 text-green-800 font-bold text-sm">Aceptado / Confirmado</span>
        </div>

        <div class="space-y-2.5 divide-y divide-stone-100">
          <div class="pt-2 flex justify-between"><span class="text-stone-500">Cliente titular:</span><span class="font-bold">José Manuel Martínez</span></div>
          <div class="pt-2 flex justify-between"><span class="text-stone-500">Tipo de evento:</span><span class="font-bold">Boda Civil & Banquete</span></div>
          <div class="pt-2 flex justify-between"><span class="text-stone-500">Fecha y hora acordadas:</span><span class="font-bold">18 de Julio de 2026 · 21:00 h</span></div>
          <div class="pt-2 flex justify-between"><span class="text-stone-500">Lugar de actuación:</span><span class="font-bold">Finca Almería Costa (Camino de la Higuera)</span></div>
          <div class="pt-2 flex justify-between"><span class="text-stone-500">Cuadrilla asignada:</span><span class="font-bold">12 Tunos con banderas y panderetas</span></div>
          <div class="pt-2 flex justify-between"><span class="text-stone-500">Repertorio pactado:</span><span>Clavelitos, Fonseca, La Morena de mi Copla + pasacalles</span></div>
          <div class="pt-2 flex justify-between"><span class="text-stone-500">Importe acordado:</span><span class="text-[#8B0000] font-black text-sm">450,00 € (Señal abonada: 150 €)</span></div>
        </div>

        <div class="p-3 bg-amber-50 rounded border border-amber-200 text-stone-700 text-[11px]">
          <strong>Nota de la Tuna:</strong> El Tuno Mayor Javier (+34 600 123 456) llamará 48 horas antes para coordinar el acceso de los coches al recinto.
        </div>

        <div class="pt-4 flex justify-between">
          <button onclick="switchClientView('c-view-1')" class="px-4 py-2 border border-stone-300 rounded text-stone-700 font-bold hover:bg-stone-50">
            ← Volver al listado
          </button>
          <a href="tel:+34600123456" class="px-4 py-2 bg-green-700 text-white font-bold rounded flex items-center gap-1.5">
            <span>📞</span> Contactar con el Tuno Mayor
          </a>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 2: HISTORIAL DE PEDIDOS ================= -->
    <div id="c-view-2" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">2 Pedidos</span>
      </nav>
      <div class="flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Historial de pedidos</h1>
          <p class="text-xs text-stone-500 mt-1">Tus compras de merchandising en la tienda oficial</p>
        </div>
        <a href="visitante.html#view-4-catalogo" class="px-4 py-2 bg-[#8B0000] text-amber-200 font-bold text-xs uppercase tracking-wider rounded-lg shadow">
          Ir a la Tienda
        </a>
      </div>

      <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
        <table class="w-full text-left text-xs">
          <thead class="bg-stone-50 text-stone-500 uppercase font-bold border-b border-stone-200">
            <tr>
              <th class="py-3 px-4">Nº Pedido</th>
              <th class="py-3 px-4">Fecha</th>
              <th class="py-3 px-4">Artículos</th>
              <th class="py-3 px-4">Total</th>
              <th class="py-3 px-4">Estado</th>
              <th class="py-3 px-4 text-right">Detalle (2.1)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-stone-100">
            <tr>
              <td class="py-3 px-4 font-bold">#PED-894</td>
              <td class="py-3 px-4">02/03/2026</td>
              <td class="py-3 px-4 font-semibold text-stone-900">1x Sudadera Roja (L), 1x Parche Beca Oro</td>
              <td class="py-3 px-4 font-bold text-stone-900">34,50 €</td>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold">Enviado por Correos</span></td>
              <td class="py-3 px-4 text-right">
                <button onclick="switchClientView('c-view-2-detail')" class="text-[#8B0000] font-bold hover:underline">Ver detalle</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= PANTALLA 2.1: PEDIDO EN DETALLE ================= -->
    <div id="c-view-2-detail" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#c-view-2" onclick="switchClientView('c-view-2')" class="hover:text-stone-900">2 Pedidos</a> › 
        <span class="text-stone-900 font-semibold">2.1 Ver pedido en detalle</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Pedido #PED-894</h1>
        <p class="text-xs text-stone-500 mt-1">Detalle del pedido y gestión de incidencias</p>
      </div>

      <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-2xl text-xs space-y-4">
        <div class="flex justify-between items-center pb-3 border-b border-stone-200">
          <div>
            <span class="font-bold text-stone-800 block">Número de seguimiento Correos:</span>
            <span class="font-mono text-blue-700 font-bold">ES98374829104AL</span>
          </div>
          <span class="px-3 py-1 bg-blue-100 text-blue-800 font-bold rounded">En Reparto</span>
        </div>

        <div class="space-y-2">
          <div class="flex justify-between"><span class="text-stone-500">Dirección de entrega:</span><span class="font-bold">Avda. del Mediterráneo 120, 3ºB, Almería (04009)</span></div>
          <div class="flex justify-between"><span class="text-stone-500">Método de pago:</span><span class="font-bold">Tarjeta Bancaria SSL</span></div>
          <div class="flex justify-between"><span class="text-stone-500">Total abonado:</span><span class="font-black text-[#8B0000] text-sm">34,50 €</span></div>
        </div>

        <div class="pt-3 border-t border-stone-100">
          <span class="font-bold text-stone-700 block mb-2 uppercase">Artículos incluidos:</span>
          <div class="divide-y divide-stone-100">
            <div class="py-2 flex justify-between"><span>1x Sudadera Roja Tuna Derecho (Talla L)</span><span class="font-bold">28,00 €</span></div>
            <div class="py-2 flex justify-between"><span>1x Parche Beca Bordado Oro</span><span class="font-bold">6,50 €</span></div>
          </div>
        </div>

        <!-- Botones de Acción Fieles al Wireframe: 2.1.1 y 2.1.2 -->
        <div class="pt-4 border-t border-stone-200 flex flex-wrap gap-3 justify-between items-center">
          <button onclick="switchClientView('c-view-2')" class="text-stone-500 hover:text-stone-800">← Volver a pedidos</button>
          <div class="space-x-2">
            <button onclick="switchClientView('c-view-2-edit')" class="px-3 py-1.5 bg-stone-900 hover:bg-stone-800 text-white rounded font-bold">
              2.1.1 Editar Datos del Pedido
            </button>
            <button onclick="switchClientView('c-view-2-devolucion')" class="px-3 py-1.5 bg-red-800 hover:bg-red-700 text-white rounded font-bold">
              2.1.2 Tramitar Devolución
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 2.1.1: EDITAR DATOS DEL PEDIDO ================= -->
    <div id="c-view-2-edit" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#c-view-2" onclick="switchClientView('c-view-2')" class="hover:text-stone-900">2 Pedidos</a> › 
        <span class="text-stone-900 font-semibold">2.1.1 Editar datos del pedido</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Editar datos del pedido</h1>
        <p class="text-xs text-stone-500 mt-1">Modifica la dirección o instrucciones de entrega</p>
      </div>

      <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-4">
        <form onsubmit="document.getElementById('c-confirm-edit').classList.remove('hidden'); return false;" class="space-y-3">
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Dirección de entrega</label>
            <input type="text" value="Avda. del Mediterráneo 120, 3ºB" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Teléfono para el transportista</label>
            <input type="tel" value="612 345 678" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Instrucciones adicionales</label>
            <textarea rows="2" placeholder="Dejar en conserjería si no contesta..." class="w-full px-3 py-2 border border-stone-300 rounded outline-none"></textarea>
          </div>
          <button type="submit" class="w-full py-2 bg-stone-900 text-white font-bold rounded uppercase">
            Guardar cambios
          </button>
        </form>

        <div id="c-confirm-edit" class="hidden p-3 bg-green-50 border border-green-300 rounded text-green-900 text-xs">
          ✅ «Datos del pedido actualizados con éxito»
        </div>

        <button onclick="switchClientView('c-view-2-detail')" class="text-stone-500 hover:text-stone-900 block text-center w-full">
          ← Volver al detalle del pedido
        </button>
      </div>
    </div>

    <!-- ================= PANTALLA 2.1.2: TRAMITAR DEVOLUCIÓN ================= -->
    <div id="c-view-2-devolucion" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#c-view-2" onclick="switchClientView('c-view-2')" class="hover:text-stone-900">2 Pedidos</a> › 
        <span class="text-stone-900 font-semibold">2.1.2 Tramitar devolución</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Tramitar devolución</h1>
        <p class="text-xs text-stone-500 mt-1">Solicita el cambio de talla o reembolso</p>
      </div>

      <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-4">
        <form onsubmit="document.getElementById('c-confirm-dev').classList.remove('hidden'); return false;" class="space-y-3">
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Producto a devolver</label>
            <select class="w-full px-3 py-2 border border-stone-300 rounded outline-none bg-white">
              <option>Sudadera Roja Tuna de Derecho (Talla L)</option>
              <option>Parche Beca en Oro</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Motivo de devolución</label>
            <select class="w-full px-3 py-2 border border-stone-300 rounded outline-none bg-white">
              <option>Talla incorrecta (quiero cambiar a M o XL)</option>
              <option>Defecto en costura o bordado</option>
              <option>Ya no deseo el producto</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Comentario adicional</label>
            <textarea rows="2" placeholder="Detalles del cambio..." class="w-full px-3 py-2 border border-stone-300 rounded outline-none"></textarea>
          </div>
          <button type="submit" class="w-full py-2 bg-[#8B0000] text-amber-200 font-bold rounded uppercase">
            Enviar Solicitud de Devolución
          </button>
        </form>

        <div id="c-confirm-dev" class="hidden p-3 bg-green-50 border border-green-300 rounded text-green-900 text-xs">
          ✅ «Solicitud de devolución registrada. Te enviaremos la etiqueta de Correos por email.»
        </div>

        <button onclick="switchClientView('c-view-2-detail')" class="text-stone-500 hover:text-stone-900 block text-center w-full">
          ← Volver al detalle del pedido
        </button>
      </div>
    </div>

    <!-- ================= PANTALLA 3: GESTIONAR CUENTA ================= -->
    <div id="c-view-3" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">3 Cuenta</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Gestionar cuenta</h1>
        <p class="text-xs text-stone-500 mt-1">Configuración de tus datos personales y contraseña</p>
      </div>

      <div class="grid sm:grid-cols-2 gap-6">
        <div onclick="switchClientView('c-view-3-datos')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition">
          <div class="h-28 bg-stone-100 rounded flex items-center justify-center text-4xl mb-3">👤</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">3.1 Modificar información personal</h3>
          <p class="text-xs text-stone-600 mt-1">Actualiza tu nombre, correo y teléfono de contacto.</p>
          <span class="text-[#8B0000] font-bold text-xs mt-3 block">Modificar datos →</span>
        </div>

        <div onclick="switchClientView('c-view-3-pass')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition">
          <div class="h-28 bg-stone-100 rounded flex items-center justify-center text-4xl mb-3">🔒</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">3.2 Cambiar contraseña</h3>
          <p class="text-xs text-stone-600 mt-1">Modifica la clave de acceso a tu panel de cliente.</p>
          <span class="text-[#8B0000] font-bold text-xs mt-3 block">Cambiar clave →</span>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 3.1: MODIFICAR INFORMACIÓN PERSONAL ================= -->
    <div id="c-view-3-datos" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#c-view-3" onclick="switchClientView('c-view-3')" class="hover:text-stone-900">3 Cuenta</a> › 
        <span class="text-stone-900 font-semibold">3.1 Modificar información personal</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Modificar información personal</h1>
        <p class="text-xs text-stone-500 mt-1">Actualiza tus datos de contacto</p>
      </div>

      <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-4">
        <form onsubmit="document.getElementById('c-confirm-datos').classList.remove('hidden'); return false;" class="space-y-3">
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Nombre Completo</label>
            <input type="text" value="José Manuel Martínez" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Teléfono</label>
            <input type="tel" value="612 345 678" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Correo Electrónico</label>
            <input type="email" value="cliente@almeria.es" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <button type="submit" class="w-full py-2 bg-stone-900 text-white font-bold rounded uppercase">
            Guardar cambios
          </button>
        </form>

        <div id="c-confirm-datos" class="hidden p-3 bg-green-50 border border-green-300 rounded text-green-900 text-xs">
          ✅ «Información personal actualizada correctamente»
        </div>

        <button onclick="switchClientView('c-view-3')" class="text-stone-500 hover:text-stone-900 block text-center w-full">
          ← Volver a cuenta
        </button>
      </div>
    </div>

    <!-- ================= PANTALLA 3.2: CAMBIAR CONTRASEÑA ================= -->
    <div id="c-view-3-pass" class="client-subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#c-view-0" onclick="switchClientView('c-view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#c-view-3" onclick="switchClientView('c-view-3')" class="hover:text-stone-900">3 Cuenta</a> › 
        <span class="text-stone-900 font-semibold">3.2 Cambiar contraseña</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Cambiar contraseña</h1>
        <p class="text-xs text-stone-500 mt-1">Actualiza tu clave de acceso</p>
      </div>

      <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm max-w-md text-xs space-y-4">
        <form onsubmit="document.getElementById('c-confirm-pass').classList.remove('hidden'); return false;" class="space-y-3">
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Contraseña actual</label>
            <input type="password" value="********" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Nueva contraseña</label>
            <input type="password" placeholder="Mínimo 8 caracteres" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Confirmar nueva contraseña</label>
            <input type="password" placeholder="Repite la contraseña" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <button type="submit" class="w-full py-2 bg-[#8B0000] text-amber-200 font-bold rounded uppercase">
            Actualizar contraseña
          </button>
        </form>

        <div id="c-confirm-pass" class="hidden p-3 bg-green-50 border border-green-300 rounded text-green-900 text-xs">
          ✅ «Contraseña actualizada correctamente»
        </div>

        <button onclick="switchClientView('c-view-3')" class="text-stone-500 hover:text-stone-900 block text-center w-full">
          ← Volver a cuenta
        </button>
      </div>
    </div>

  </main>

  <!-- ========================================================================= -->
  <!-- FOOTER CLIENTE FIEL AL WIREFRAME: CONTACTO · SÍGUENOS · LEGAL -->
  <!-- ========================================================================= -->
  <footer class="bg-[#120404] text-stone-300 border-t-2 border-[#D4AF37] pt-8 pb-6 text-xs mt-auto">
    <div class="max-w-7xl mx-auto px-4 grid sm:grid-cols-3 gap-6 pb-6 border-b border-stone-800">
      <div>
        <p class="font-serif-tuna font-bold text-amber-300 mb-2 uppercase">Contacto Directo</p>
        <p class="text-stone-300">Tuna de Derecho · Universidad de Almería</p>
        <p class="text-stone-400 mt-1">tuna.derecho.almeria@gmail.com</p>
        <p class="text-white font-bold mt-1">Tel: +34 600 123 456</p>
      </div>
      <div>
        <p class="font-serif-tuna font-bold text-amber-300 mb-2 uppercase">Síguenos</p>
        <p class="text-stone-400">Instagram · YouTube · TikTok · Spotify</p>
      </div>
      <div>
        <p class="font-serif-tuna font-bold text-amber-300 mb-2 uppercase">Legal</p>
        <p class="text-stone-400">Aviso legal · Privacidad · Cookies</p>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 pt-4 text-center text-[11px] text-stone-500">
      © 2026 TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA · ÁREA PRIVADA DE CLIENTE
    </div>
  </footer>

  <script>
    function switchClientView(viewId) {
      document.querySelectorAll('.client-subview-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.subview-pill').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.client-nav-btn').forEach(el => el.classList.remove('active'));

      const target = document.getElementById(viewId);
      if (target) {
        target.classList.remove('hidden');
        window.scrollTo({ top: 90, behavior: 'smooth' });
      }

      // Activar píldora correspondiente
      const btn = Array.from(document.querySelectorAll('.subview-pill')).find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes(viewId));
      if (btn) btn.classList.add('active');

      // Activar nav principal según sección
      if (viewId === 'c-view-0') document.getElementById('c-nav-0').classList.add('active');
      if (viewId.startsWith('c-view-1')) document.getElementById('c-nav-1').classList.add('active');
      if (viewId.startsWith('c-view-2')) document.getElementById('c-nav-2').classList.add('active');
      if (viewId.startsWith('c-view-3')) document.getElementById('c-nav-3').classList.add('active');
    }
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    content = get_cliente_html()
    target = r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\cliente.html"
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Guardado:", target)

