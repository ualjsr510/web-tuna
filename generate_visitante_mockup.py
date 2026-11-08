# -*- coding: utf-8 -*-
"""
Generador del Mockup para VISITANTE (visitante.html)
Fiel a los 26 wireframes de Visitante:
- 0 Inicio visitante
- 1 Conoce la tuna (1.1 Historia, 1.2 Miembros)
- 2 Contratación (2.1 Acceso contratación, 2.1.1 Formulario contratación)
- 3 Multimedia (3.1 Mejores momentos: 3.1.1 Vídeos, 3.1.2 Fotos; 3.2 Certámenes)
- 4 Tienda (4.1 Catálogo interactivo con filtros, 4.2 Cesta y Checkout 4.2.1 / 4.2.1.1 Dirección y Pago)
- 5 Cancionero (5.1 Repertorio con letras, 5.2 Spotify)
- 6 Únete a nosotros (6.1 Formulario, 6.2 Local de ensayo)
- 7 Inicio de sesión (7.1 Recuperar contraseña, 7.2 Registro)
"""

import os

def get_visitante_html():
    return """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería · Portal Visitante</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {
      --rojo-tuna: #8B0000;
      --rojo-oscuro: #5C0000;
      --rojo-vivo: #991B1B;
      --dorado: #D4AF37;
      --dorado-claro: #F3E5AB;
      --fondo-crema: #FAF8F5;
      --carbon: #18181B;
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
      letter-spacing: 0.2em;
      text-transform: uppercase;
      font-size: 0.7rem;
      font-weight: 700;
    }
    .hero-salamanca {
      background: linear-gradient(180deg, #1A0505 0%, #3B0A0A 55%, #5C0E0E 100%);
      position: relative;
    }
    .hero-salamanca::after {
      content: "";
      position: absolute;
      inset: 0;
      background-image: radial-gradient(rgba(212, 175, 55, 0.15) 1px, transparent 1px);
      background-size: 24px 24px;
      pointer-events: none;
    }
    .wireframe-nav-active {
      color: #8B0000;
      font-weight: 700;
      border-bottom: 2px solid #8B0000;
    }
    .subview-pill.active {
      background-color: #8B0000;
      color: #FFFFFF;
      font-weight: 700;
      border-color: #5C0000;
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
          <span class="text-amber-400 font-bold tracking-wider uppercase text-[10px] block">MOCKUP 1 DE 3 · PERFIL ACTUAL: VISITANTE</span>
          <span class="text-slate-300 text-[11px]">Tuna de la Facultad de Derecho de Almería</span>
        </div>
      </div>

      <!-- Selector para cambiar de mockup -->
      <div class="flex items-center bg-[#1f1f1f] p-1 rounded-xl border border-slate-700">
        <a href="visitante.html" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#8B0000] border-b-2 border-[#D4AF37] shadow flex items-center gap-1.5">
          <span>🌐</span> Visitante <span class="text-[10px] opacity-75">(Público)</span>
        </a>
        <a href="cliente.html" class="px-3.5 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white transition flex items-center gap-1.5">
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
          Tuno Mayor: +34 600 123 456
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
          TELÉFONOS DIRECTOS: +34 600 123 456 · +34 612 345 678
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
        <a href="https://youtube.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-red-700 transition text-[11px] font-bold text-white flex items-center gap-1">
          <span>▶️</span> YouTube
        </a>
        <a href="https://spotify.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-green-700 transition text-[11px] font-bold text-white flex items-center gap-1">
          <span>🟢</span> Spotify
        </a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- HEADER FIEL AL WIREFRAME DE VISITANTE (LOGO TUNA + NAVEGACIÓN + CESTA/LOGIN) -->
  <!-- ========================================================================= -->
  <header class="bg-white border-b border-stone-200 sticky top-12 z-40 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between gap-4">
      
      <!-- Logo TUNA con Escudo de Derecho -->
      <a href="#view-0" onclick="switchView('view-0')" class="flex items-center gap-3 group">
        <div class="w-12 h-12 rounded-full bg-[#8B0000] border-2 border-[#D4AF37] flex items-center justify-center text-amber-300 font-serif-tuna font-black text-xl shadow group-hover:scale-105 transition">
          TD
        </div>
        <div>
          <div class="font-serif-tuna font-black text-xl tracking-tight text-[#5C0000] leading-none">
            TUNA DE DERECHO
          </div>
          <div class="badge-editorial text-[#8B0000] text-[9px] mt-1 font-bold">
            Universidad de Almería · Beca Roja
          </div>
        </div>
      </a>

      <!-- Menú Fiel a los Wireframes de Visitante -->
      <nav class="hidden lg:flex items-center gap-6 text-[13px] font-medium text-stone-700">
        <button onclick="switchView('view-0')" id="nav-v0" class="hover:text-[#8B0000] transition">Inicio</button>
        <button onclick="switchView('view-1')" id="nav-v1" class="hover:text-[#8B0000] transition">1. Conoce la tuna</button>
        <button onclick="switchView('view-2')" id="nav-v2" class="hover:text-[#8B0000] transition">2. Contratación</button>
        <button onclick="switchView('view-3')" id="nav-v3" class="hover:text-[#8B0000] transition">3. Multimedia</button>
        <button onclick="switchView('view-4-catalogo')" id="nav-v4" class="px-3 py-1 rounded-full bg-red-50 text-[#8B0000] font-bold border border-red-200 hover:bg-red-100 transition flex items-center gap-1.5 shadow-sm">
          <span>🛍️</span> 4. Tienda
        </button>
        <button onclick="switchView('view-5')" id="nav-v5" class="hover:text-[#8B0000] transition">5. Cancionero</button>
        <button onclick="switchView('view-6')" id="nav-v6" class="hover:text-[#8B0000] transition">6. Únete</button>
      </nav>

      <!-- Botones de Acción según Wireframe -->
      <div class="flex items-center gap-2.5">
        <button onclick="switchView('view-4-cesta')" class="px-3 py-1.5 rounded-lg border border-stone-300 bg-stone-50 hover:bg-stone-100 text-stone-800 font-semibold text-xs flex items-center gap-1.5 transition">
          <span>🛒</span> Cesta (<span id="cart-counter" class="font-bold text-[#8B0000]">2</span>)
        </button>
        <button onclick="switchView('view-7')" class="px-3 py-1.5 rounded-lg border border-[#8B0000] text-[#8B0000] font-bold text-xs hover:bg-red-50 transition">
          Iniciar sesión
        </button>
        <button onclick="switchView('view-2-form')" class="px-4 py-2 rounded-lg bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold text-xs shadow transition border border-[#D4AF37] uppercase tracking-wider">
          Contratar
        </button>
      </div>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- BARRA DE PANTALLAS DEL WIREFRAME (PERMITE SALTAR A CUALQUIERA DE LAS 26) -->
  <!-- ========================================================================= -->
  <div class="bg-stone-100 border-b border-stone-300 py-2 px-4 text-xs overflow-x-auto whitespace-nowrap shadow-inner">
    <div class="max-w-7xl mx-auto flex items-center gap-1.5">
      <span class="font-bold text-stone-500 uppercase tracking-wider text-[10px] mr-1">Pantallas Wireframe Visitante:</span>
      <button onclick="switchView('view-0')" class="subview-pill active px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">0. Inicio</button>
      <button onclick="switchView('view-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">1. Conoce</button>
      <button onclick="switchView('view-1-1')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">1.1 Historia</button>
      <button onclick="switchView('view-1-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">1.2 Miembros</button>
      <button onclick="switchView('view-2')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2. Contratación</button>
      <button onclick="switchView('view-2-form')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">2.1.1 Formulario Contratar</button>
      <button onclick="switchView('view-3')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3. Multimedia</button>
      <button onclick="switchView('view-3-videos')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3.1.1 Vídeos</button>
      <button onclick="switchView('view-3-fotos')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3.1.2 Fotos</button>
      <button onclick="switchView('view-3-certamenes')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">3.2 Certámenes</button>
      <button onclick="switchView('view-4-tienda')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">4. Tienda (Home)</button>
      <button onclick="switchView('view-4-catalogo')" class="subview-pill px-2.5 py-1 rounded border border-amber-600 bg-amber-50 text-[#8B0000] font-bold text-[11px]">4.1 Catálogo</button>
      <button onclick="switchView('view-4-cesta')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">4.2 Cesta</button>
      <button onclick="switchView('view-4-envio')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">4.2.1.1 Envío y Pago</button>
      <button onclick="switchView('view-5')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">5. Cancionero</button>
      <button onclick="switchView('view-5-spotify')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">5.2 Spotify</button>
      <button onclick="switchView('view-6')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">6. Únete</button>
      <button onclick="switchView('view-6-ensayo')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">6.2 Local Ensayo</button>
      <button onclick="switchView('view-7')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">7. Iniciar Sesión</button>
      <button onclick="switchView('view-7-recuperar')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">7.1 Recuperar Clave</button>
      <button onclick="switchView('view-7-registro')" class="subview-pill px-2.5 py-1 rounded border border-stone-300 text-stone-700 hover:bg-white text-[11px]">7.2 Registro</button>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- CONTENEDOR PRINCIPAL: PANTALLAS INTERACTIVAS DEL WIREFRAME VISITANTE -->
  <!-- ========================================================================= -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-8">

    <!-- ================= PANTALLA 0: INICIO VISITANTE ================= -->
    <div id="view-0" class="subview-content space-y-8">
      
      <!-- Hero estilo tunasalamanca.com adaptado a Almería -->
      <section class="hero-salamanca rounded-2xl text-white p-8 md:p-14 text-center shadow-xl border border-amber-600/50">
        <div class="badge-editorial text-[#D4AF37] mb-3">MÚSICA · UNIVERSIDAD · TRADICIÓN · DESDE 1995</div>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-serif-tuna font-normal text-stone-100 leading-tight">
          Almería se canta<br><span class="italic text-amber-200">con capa y bandurria</span>
        </h1>
        <p class="text-stone-300 text-sm sm:text-base max-w-2xl mx-auto mt-4 font-light leading-relaxed">
          Tradición estudiantil de la Facultad de Derecho de la Universidad de Almería. Serenatas, bodas, certámenes y rondallas por toda España.
        </p>
        
        <div class="mt-8 flex flex-wrap items-center justify-center gap-4">
          <button onclick="switchView('view-2-form')" class="px-6 py-3 bg-[#D4AF37] hover:bg-amber-400 text-stone-950 font-bold text-xs uppercase tracking-wider rounded-lg shadow-lg transition">
            Solicitar Actuación
          </button>
          <button onclick="switchView('view-5')" class="px-6 py-3 bg-transparent border border-stone-300 hover:border-amber-300 text-stone-100 font-bold text-xs uppercase tracking-wider rounded-lg transition">
            Escuchar la Tuna
          </button>
          <button onclick="switchView('view-4-catalogo')" class="px-6 py-3 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 border border-[#D4AF37] font-bold text-xs uppercase tracking-wider rounded-lg transition flex items-center gap-2">
            <span>🛍️</span> Tienda Oficial
          </button>
        </div>

        <!-- Módulo de Contacto Directo Ultra-Visible en Hero -->
        <div class="mt-8 pt-6 border-t border-red-900/80 inline-flex flex-wrap items-center justify-center gap-6 text-xs">
          <div class="flex items-center gap-2">
            <span class="text-amber-400 font-bold">Javier (Tuno Mayor):</span>
            <a href="tel:+34600123456" class="font-serif-tuna font-bold text-white text-base hover:text-amber-300">+34 600 123 456</a>
          </div>
          <div class="h-4 w-px bg-stone-700 hidden sm:block"></div>
          <div class="flex items-center gap-2">
            <span class="text-amber-400 font-bold">Marcos (Relaciones Públicas):</span>
            <a href="tel:+34612345678" class="font-serif-tuna font-bold text-white text-base hover:text-amber-300">+34 612 345 678</a>
          </div>
        </div>
      </section>

      <!-- Los 6 Bloques Principales Fieles al Wireframe index.html de Visitante -->
      <div>
        <div class="text-center mb-6">
          <span class="badge-editorial text-[#8B0000]">ÁRBOL DE CONTENIDOS</span>
          <h2 class="text-2xl font-serif-tuna font-bold text-stone-900 mt-1">Explora las Secciones Principales</h2>
          <div class="w-12 h-1 bg-[#D4AF37] mx-auto mt-2"></div>
        </div>

        <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- 1 Conoce la tuna -->
          <div onclick="switchView('view-1')" class="bg-white rounded-xl border border-stone-200 p-5 shadow-sm hover:border-[#8B0000] transition cursor-pointer group flex flex-col justify-between">
            <div>
              <div class="h-28 rounded-lg bg-red-100/70 border border-red-200 flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">🏛️</div>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900">1 Conoce la tuna</h3>
              <p class="text-xs text-stone-600 mt-1">Historia, fundación desde 1995 y miembros de la cuadrilla.</p>
            </div>
            <div class="text-[#8B0000] font-bold text-xs mt-4 group-hover:underline">Ver Historia y Miembros →</div>
          </div>

          <!-- 2 Contratación -->
          <div onclick="switchView('view-2')" class="bg-white rounded-xl border border-stone-200 p-5 shadow-sm hover:border-[#8B0000] transition cursor-pointer group flex flex-col justify-between">
            <div>
              <div class="h-28 rounded-lg bg-amber-100/70 border border-amber-200 flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">📜</div>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900">2 Contratación</h3>
              <p class="text-xs text-stone-600 mt-1">Pide cuenta para contratar para bodas, serenatas y congresos.</p>
            </div>
            <div class="text-[#8B0000] font-bold text-xs mt-4 group-hover:underline">Solicitar Presupuesto →</div>
          </div>

          <!-- 3 Contenido multimedia -->
          <div onclick="switchView('view-3')" class="bg-white rounded-xl border border-stone-200 p-5 shadow-sm hover:border-[#8B0000] transition cursor-pointer group flex flex-col justify-between">
            <div>
              <div class="h-28 rounded-lg bg-stone-100 border border-stone-200 flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">🎬</div>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900">3 Contenido multimedia</h3>
              <p class="text-xs text-stone-600 mt-1">Mejores momentos, vídeos, fotos y certámenes premiados.</p>
            </div>
            <div class="text-[#8B0000] font-bold text-xs mt-4 group-hover:underline">Ver Galería Multimedia →</div>
          </div>

          <!-- 4 Tienda (DESTACADO) -->
          <div onclick="switchView('view-4-catalogo')" class="bg-white rounded-xl border-2 border-[#8B0000] p-5 shadow-md hover:shadow-lg transition cursor-pointer group flex flex-col justify-between bg-gradient-to-b from-red-50/40 to-white">
            <div>
              <div class="h-28 rounded-lg bg-red-900 text-amber-300 border border-amber-400 flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">🛍️</div>
              <span class="text-[10px] font-bold uppercase tracking-wider text-[#8B0000] bg-red-100 px-2 py-0.5 rounded">Oficial</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mt-1">4 Tienda</h3>
              <p class="text-xs text-stone-600 mt-1">Catálogo de merchandising, sudaderas, CDs y cesta de compra.</p>
            </div>
            <div class="text-[#8B0000] font-bold text-xs mt-4 group-hover:underline">Comprar Artículos Oficiales →</div>
          </div>

          <!-- 5 Cancionero -->
          <div onclick="switchView('view-5')" class="bg-white rounded-xl border border-stone-200 p-5 shadow-sm hover:border-[#8B0000] transition cursor-pointer group flex flex-col justify-between">
            <div>
              <div class="h-28 rounded-lg bg-stone-100 border border-stone-200 flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">🎵</div>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900">5 Cancionero</h3>
              <p class="text-xs text-stone-600 mt-1">Repertorio tradicional de ronda y pistas oficiales en Spotify.</p>
            </div>
            <div class="text-[#8B0000] font-bold text-xs mt-4 group-hover:underline">Ver Canciones & Spotify →</div>
          </div>

          <!-- 6 Únete a nosotros -->
          <div onclick="switchView('view-6')" class="bg-white rounded-xl border border-stone-200 p-5 shadow-sm hover:border-[#8B0000] transition cursor-pointer group flex flex-col justify-between">
            <div>
              <div class="h-28 rounded-lg bg-stone-100 border border-stone-200 flex items-center justify-center text-4xl mb-3 group-hover:scale-105 transition">🤝</div>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900">6 Únete a nosotros</h3>
              <p class="text-xs text-stone-600 mt-1">Formulario para nuevos novatos y ubicación del local de ensayo.</p>
            </div>
            <div class="text-[#8B0000] font-bold text-xs mt-4 group-hover:underline">Aprende a Tocar con Nosotros →</div>
          </div>
        </section>
      </div>

    </div>

    <!-- ================= PANTALLA 1: CONOCE LA TUNA ================= -->
    <div id="view-1" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › <span class="text-stone-900 font-semibold">1 Conoce la tuna</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Conoce la tuna</h1>
        <p class="text-xs text-stone-500 mt-1">Nuestra trayectoria universitaria y los miembros que forman la hermandad</p>
      </div>

      <div class="h-44 rounded-xl bg-[#5C0000] text-amber-200 flex flex-col items-center justify-center border border-amber-400/60 shadow p-4 text-center">
        <span class="text-3xl mb-1">🏛️</span>
        <span class="font-serif-tuna font-bold text-xl text-white">Tuna de la Facultad de Derecho de Almería</span>
        <span class="text-xs text-stone-300 mt-1">Desde 1995 llevando la beca roja con orgullo</span>
      </div>

      <section class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div onclick="switchView('view-1-1')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer transition shadow-sm">
          <div class="h-32 bg-stone-100 rounded-lg flex items-center justify-center text-4xl mb-3">📜</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">1.1 Historia</h3>
          <p class="text-xs text-stone-600 mt-1">Descubre nuestros orígenes, viajes y participación en homenajes y certámenes.</p>
          <span class="text-[#8B0000] font-bold text-xs block mt-3">Leer historia completa →</span>
        </div>
        <div onclick="switchView('view-1-2')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer transition shadow-sm">
          <div class="h-32 bg-stone-100 rounded-lg flex items-center justify-center text-4xl mb-3">👥</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">1.2 Miembros</h3>
          <p class="text-xs text-stone-600 mt-1">Conoce a los tunos, pardillos y novatos que componen la cuadrilla actual.</p>
          <span class="text-[#8B0000] font-bold text-xs block mt-3">Ver cuadrilla oficial →</span>
        </div>
      </section>
    </div>

    <!-- ================= PANTALLA 1.1: HISTORIA ================= -->
    <div id="view-1-1" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-1" onclick="switchView('view-1')" class="hover:text-stone-900">Conoce la tuna</a> › 
        <span class="text-stone-900 font-semibold">1.1 Historia</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Historia</h1>
        <p class="text-xs text-stone-500 mt-1">La trayectoria de la Tuna de la Facultad de Derecho de Almería desde 1995</p>
      </div>

      <div class="bg-white p-8 rounded-xl border border-stone-200 shadow-sm space-y-6 text-sm text-stone-700 leading-relaxed">
        <div class="flex items-center gap-3 pb-4 border-b border-stone-100">
          <span class="px-3 py-1 bg-red-100 text-[#8B0000] font-bold text-xs rounded-full">Orígenes</span>
          <span class="text-stone-500 text-xs">Universidad de Almería · Campus de La Cañada</span>
        </div>
        <p>
          La <strong>Tuna de la Facultad de Derecho de Almería</strong> nació formalmente en el año 1995, impulsada por un grupo de entusiastas estudiantes de ciencias jurídicas que quisieron enriquecer la vida universitaria de la recién emancipada Universidad de Almería (UAL).
        </p>
        <p>
          Adoptaron como seña de identidad la <strong>beca roja</strong> (color oficial de la Facultad de Derecho), sobre el tradicional traje negro compuesto por jubón, camisa blanca de cuello escarolado y gregüescos.
        </p>

        <div class="grid sm:grid-cols-3 gap-4 pt-4">
          <div class="p-4 bg-stone-50 rounded-lg border border-stone-200">
            <div class="font-serif-tuna font-bold text-xl text-[#8B0000]">1995</div>
            <div class="text-xs font-bold text-stone-900 mt-1">Primera Cuadrilla</div>
            <div class="text-xs text-stone-500 mt-1">Primeros pasacalles por la Puerta de Purchena y serenatas en el Zapillo.</div>
          </div>
          <div class="p-4 bg-stone-50 rounded-lg border border-stone-200">
            <div class="font-serif-tuna font-bold text-xl text-[#8B0000]">2005 - 2020</div>
            <div class="text-xs font-bold text-stone-900 mt-1">Certámenes Nacionales</div>
            <div class="text-xs text-stone-500 mt-1">Premios a la Mejor Tuna, Mejor Pandereta y Mejor Pasacalles en certámenes de Derecho.</div>
          </div>
          <div class="p-4 bg-stone-50 rounded-lg border border-stone-200">
            <div class="font-serif-tuna font-bold text-xl text-[#8B0000]">2026</div>
            <div class="text-xs font-bold text-stone-900 mt-1">Disco "25 Años de Ronda"</div>
            <div class="text-xs text-stone-500 mt-1">Grabación oficial remasterizada con 16 canciones populares.</div>
          </div>
        </div>

        <div class="pt-4">
          <button onclick="switchView('view-1')" class="px-4 py-2 border border-stone-300 rounded text-xs font-semibold hover:bg-stone-50">
            ← Volver a Conoce la tuna
          </button>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 1.2: MIEMBROS ================= -->
    <div id="view-1-2" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-1" onclick="switchView('view-1')" class="hover:text-stone-900">Conoce la tuna</a> › 
        <span class="text-stone-900 font-semibold">1.2 Miembros</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Miembros</h1>
        <p class="text-xs text-stone-500 mt-1">La cuadrilla que da vida a nuestra tuna</p>
      </div>

      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm text-center">
          <div class="w-20 h-20 mx-auto rounded-full bg-[#8B0000] text-amber-200 font-bold text-2xl flex items-center justify-center border-2 border-[#D4AF37] mb-3">JT</div>
          <h3 class="font-serif-tuna font-bold text-base text-stone-900">Javier "Jurisconsulto"</h3>
          <div class="text-xs font-bold text-[#8B0000]">Tuno Mayor · Bandurria</div>
          <div class="text-xs text-stone-500 mt-1">Generación 2018</div>
          <div class="mt-3 pt-3 border-t border-stone-100 text-xs text-stone-600">Tel: <strong>600 123 456</strong></div>
        </div>

        <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm text-center">
          <div class="w-20 h-20 mx-auto rounded-full bg-[#8B0000] text-amber-200 font-bold text-2xl flex items-center justify-center border-2 border-[#D4AF37] mb-3">MG</div>
          <h3 class="font-serif-tuna font-bold text-base text-stone-900">Marcos "El Notario"</h3>
          <div class="text-xs font-bold text-[#8B0000]">Contador / RR.PP. · Guitarra</div>
          <div class="text-xs text-stone-500 mt-1">Generación 2019</div>
          <div class="mt-3 pt-3 border-t border-stone-100 text-xs text-stone-600">Tel: <strong>612 345 678</strong></div>
        </div>

        <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm text-center">
          <div class="w-20 h-20 mx-auto rounded-full bg-[#8B0000] text-amber-200 font-bold text-2xl flex items-center justify-center border-2 border-[#D4AF37] mb-3">AP</div>
          <h3 class="font-serif-tuna font-bold text-base text-stone-900">Antonio "El Fiscal"</h3>
          <div class="text-xs font-bold text-[#8B0000]">Solista Principal · Laúd</div>
          <div class="text-xs text-stone-500 mt-1">Generación 2020</div>
          <div class="mt-3 pt-3 border-t border-stone-100 text-xs text-stone-600">Voz y arreglos</div>
        </div>

        <div class="bg-white p-5 rounded-xl border border-stone-200 shadow-sm text-center">
          <div class="w-20 h-20 mx-auto rounded-full bg-[#8B0000] text-amber-200 font-bold text-2xl flex items-center justify-center border-2 border-[#D4AF37] mb-3">CL</div>
          <h3 class="font-serif-tuna font-bold text-base text-stone-900">Carlos "El Pasante"</h3>
          <div class="text-xs font-bold text-amber-700">Novato / Pardillo · Pandereta</div>
          <div class="text-xs text-stone-500 mt-1">Generación 2024</div>
          <div class="mt-3 pt-3 border-t border-stone-100 text-xs text-stone-600">Acrobacias y ritmo</div>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 2: CONTRATACIÓN DE SERVICIOS ================= -->
    <div id="view-2" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">2 Contratación de nuestros servicios</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Contratación de nuestros servicios</h1>
        <p class="text-xs text-stone-500 mt-1">Pide cuenta para contratar a la tuna para tu evento especial</p>
      </div>

      <div class="bg-white p-8 rounded-xl border border-stone-200 shadow-sm grid md:grid-cols-2 gap-8 items-center">
        <div>
          <span class="badge-editorial text-[#8B0000]">PUNTUALIDAD · ALEGRÍA · MÚSICA EN VIVO</span>
          <h3 class="text-2xl font-serif-tuna font-bold text-stone-900 mt-2">¿Cómo funciona la contratación?</h3>
          <p class="text-xs text-stone-600 mt-3 leading-relaxed">
            Para solicitar una actuación puedes rellenar nuestro formulario oficial indicando los detalles del evento, o bien iniciar sesión / crear tu cuenta de cliente para poder hacer seguimiento de la solicitud, consultar el presupuesto y descargar la ficha de confirmación.
          </p>
          <div class="mt-6 flex flex-wrap gap-3">
            <button onclick="switchView('view-2-form')" class="px-5 py-2.5 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded-lg text-xs uppercase tracking-wider transition">
              2.1.1 Rellenar Formulario de Contratación
            </button>
            <button onclick="switchView('view-7')" class="px-5 py-2.5 border border-stone-300 rounded-lg text-xs font-bold hover:bg-stone-50 transition">
              2.1 Iniciar Sesión para Contratar
            </button>
          </div>
        </div>

        <div class="bg-[#5C0000] text-white p-6 rounded-xl border border-amber-400/70 shadow">
          <span class="badge-editorial text-amber-300">ATENCIÓN TELEFÓNICA URGENTE</span>
          <h4 class="font-serif-tuna font-bold text-xl text-white mt-1">¿Tu evento es en menos de 7 días?</h4>
          <p class="text-xs text-stone-200 mt-2">Llámanos directamente para coordinar la cuadrilla en tiempo récord:</p>
          <div class="mt-4 space-y-2 text-xs">
            <div class="p-2.5 bg-black/40 rounded border border-amber-400/40 font-bold">
              📞 Javier (Tuno Mayor): <a href="tel:+34600123456" class="text-amber-300 underline">+34 600 123 456</a>
            </div>
            <div class="p-2.5 bg-black/40 rounded border border-amber-400/40 font-bold">
              📞 Marcos (R. Públicas): <a href="tel:+34612345678" class="text-amber-300 underline">+34 612 345 678</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 2.1.1: FORMULARIO DE CONTRATACIÓN ================= -->
    <div id="view-2-form" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-2" onclick="switchView('view-2')" class="hover:text-stone-900">Contratación</a> › 
        <span class="text-stone-900 font-semibold">2.1.1 Rellenar formulario de contratación</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Formulario de contratación</h1>
        <p class="text-xs text-stone-500 mt-1">Introduce los datos para solicitar la actuación de la Tuna</p>
      </div>

      <div class="bg-white p-8 rounded-xl border border-stone-200 shadow-sm max-w-3xl">
        <form onsubmit="alert('¡Solicitud de contratación recibida! Te responderemos con la disponibilidad en menos de 24 horas.'); return false;" class="space-y-4 text-xs">
          <div class="grid sm:grid-cols-2 gap-4">
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Nombre Completo *</label>
              <input type="text" required placeholder="Ej. Laura Gómez Martínez" class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none focus:border-[#8B0000]">
            </div>
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Teléfono Móvil *</label>
              <input type="tel" required placeholder="600 000 000" class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none focus:border-[#8B0000]">
            </div>
          </div>

          <div class="grid sm:grid-cols-2 gap-4">
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Correo Electrónico *</label>
              <input type="email" required placeholder="tu@email.com" class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none focus:border-[#8B0000]">
            </div>
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Tipo de Evento *</label>
              <select class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none bg-white">
                <option>Boda (Salida iglesia / Cóctel / Banquete)</option>
                <option>Serenata a la novia / balcón sorpresa</option>
                <option>Acto académico / Graduación universitaria</option>
                <option>Cena de empresa o gala corporativa</option>
                <option>Cumpleaños / Aniversario familiar</option>
              </select>
            </div>
          </div>

          <div class="grid sm:grid-cols-3 gap-4">
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Fecha del Evento *</label>
              <input type="date" required class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none focus:border-[#8B0000]">
            </div>
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Hora Prevista *</label>
              <input type="time" required value="21:00" class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none focus:border-[#8B0000]">
            </div>
            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Municipio / Lugar *</label>
              <input type="text" required placeholder="Almería, Roquetas..." class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none focus:border-[#8B0000]">
            </div>
          </div>

          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Observaciones / Peticiones de canciones</label>
            <textarea rows="3" placeholder="Indícanos si es una sorpresa, canciones que no pueden faltar o peticiones especiales..." class="w-full px-3 py-2.5 border border-stone-300 rounded-lg outline-none focus:border-[#8B0000]"></textarea>
          </div>

          <div class="pt-4 flex items-center justify-between border-t border-stone-100">
            <button type="button" onclick="switchView('view-2')" class="text-stone-500 hover:text-stone-800">
              ← Cancelar y volver
            </button>
            <button type="submit" class="px-6 py-3 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded-lg uppercase tracking-wider text-xs shadow border border-[#D4AF37]">
              Enviar Formulario de Contratación
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- ================= PANTALLA 3: MULTIMEDIA ================= -->
    <div id="view-3" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">3 Contenido multimedia</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Contenido multimedia</h1>
        <p class="text-xs text-stone-500 mt-1">Mejores momentos y certámenes de la Tuna</p>
      </div>

      <div class="grid md:grid-cols-2 gap-6">
        <div onclick="switchView('view-3-videos')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition">
          <div class="h-32 bg-stone-900 rounded-lg flex items-center justify-center text-4xl text-red-500 mb-3">▶️</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">3.1 Nuestros mejores momentos (Vídeos y Fotos)</h3>
          <p class="text-xs text-stone-600 mt-1">Actuaciones en directo, pasacalles por la Feria y serenatas tradicionales.</p>
          <span class="text-[#8B0000] font-bold text-xs block mt-3">Ver vídeos y fotos →</span>
        </div>

        <div onclick="switchView('view-3-certamenes')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition">
          <div class="h-32 bg-[#5C0000] rounded-lg flex items-center justify-center text-4xl text-amber-300 mb-3">🏆</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">3.2 Certámenes</h3>
          <p class="text-xs text-stone-600 mt-1">Premios obtenidos en certámenes nacionales e internacionales de Derecho.</p>
          <span class="text-[#8B0000] font-bold text-xs block mt-3">Ver palmarés y certámenes →</span>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 3.1.1: VÍDEOS ================= -->
    <div id="view-3-videos" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-3" onclick="switchView('view-3')" class="hover:text-stone-900">Multimedia</a> › 
        <span class="text-stone-900 font-semibold">3.1.1 Vídeos</span>
      </nav>
      <div class="flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Vídeos</h1>
          <p class="text-xs text-stone-500 mt-1">Actuaciones oficiales en directo</p>
        </div>
        <button onclick="switchView('view-3-fotos')" class="text-xs font-bold text-[#8B0000] hover:underline">
          Ver fotos (3.1.2) →
        </button>
      </div>

      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-44 bg-stone-900 flex flex-col items-center justify-center text-white cursor-pointer group">
            <span class="text-4xl text-red-500 group-hover:scale-125 transition">▶️</span>
            <span class="text-xs text-stone-400 mt-2 font-mono">03:45 · YouTube</span>
          </div>
          <div class="p-4">
            <h4 class="font-serif-tuna font-bold text-stone-900 text-sm">Clavelitos en la Feria de Almería</h4>
            <p class="text-xs text-stone-500 mt-1">Ronda en el Balcón del Ayuntamiento</p>
          </div>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-44 bg-stone-900 flex flex-col items-center justify-center text-white cursor-pointer group">
            <span class="text-4xl text-red-500 group-hover:scale-125 transition">▶️</span>
            <span class="text-xs text-stone-400 mt-2 font-mono">04:12 · YouTube</span>
          </div>
          <div class="p-4">
            <h4 class="font-serif-tuna font-bold text-stone-900 text-sm">Serenata de Boda en Finca</h4>
            <p class="text-xs text-stone-500 mt-1">Ronda con 14 tunos en directo</p>
          </div>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-44 bg-stone-900 flex flex-col items-center justify-center text-white cursor-pointer group">
            <span class="text-4xl text-red-500 group-hover:scale-125 transition">▶️</span>
            <span class="text-xs text-stone-400 mt-2 font-mono">05:20 · YouTube</span>
          </div>
          <div class="p-4">
            <h4 class="font-serif-tuna font-bold text-stone-900 text-sm">Pasacalles Certamen de Salamanca</h4>
            <p class="text-xs text-stone-500 mt-1">Premio al Mejor Pasacalles</p>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 3.1.2: FOTOS ================= -->
    <div id="view-3-fotos" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-3" onclick="switchView('view-3')" class="hover:text-stone-900">Multimedia</a> › 
        <span class="text-stone-900 font-semibold">3.1.2 Fotos</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Fotos</h1>
        <p class="text-xs text-stone-500 mt-1">Galería fotográfica de actos y viajes</p>
      </div>

      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-48 bg-gradient-to-tr from-red-950 to-red-800 flex flex-col items-center justify-center text-amber-200">
            <span class="text-4xl mb-1">📸</span>
            <span class="text-xs">Foto Oficial de Cuadrilla</span>
          </div>
          <div class="p-3 text-xs text-stone-600 font-bold">Graduación en el Paraninfo de la UAL</div>
        </div>
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-48 bg-stone-800 flex flex-col items-center justify-center text-stone-300">
            <span class="text-4xl mb-1">🎸</span>
            <span class="text-xs">Ensayo en la Facultad</span>
          </div>
          <div class="p-3 text-xs text-stone-600 font-bold">Tarde de cuerdas en el aula de música</div>
        </div>
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-48 bg-gradient-to-tr from-amber-900 to-red-900 flex flex-col items-center justify-center text-amber-300">
            <span class="text-4xl mb-1">🌙</span>
            <span class="text-xs">Serenata Nocturna</span>
          </div>
          <div class="p-3 text-xs text-stone-600 font-bold">Ronda bajo el balcón en Almería centro</div>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 3.2: CERTÁMENES ================= -->
    <div id="view-3-certamenes" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-3" onclick="switchView('view-3')" class="hover:text-stone-900">Multimedia</a> › 
        <span class="text-stone-900 font-semibold">3.2 Certámenes</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Certámenes</h1>
        <p class="text-xs text-stone-500 mt-1">Premios y participación en festivales nacionales e internacionales</p>
      </div>

      <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
        <table class="w-full text-left text-xs">
          <thead class="bg-stone-50 text-stone-500 uppercase font-bold border-b border-stone-200">
            <tr>
              <th class="py-3 px-4">Año</th>
              <th class="py-3 px-4">Certamen</th>
              <th class="py-3 px-4">Ciudad</th>
              <th class="py-3 px-4">Premio Obtenido</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-stone-100">
            <tr>
              <td class="py-3 px-4 font-bold">2024</td>
              <td class="py-3 px-4 font-semibold text-stone-900">Certamen Nacional de Tunas de Derecho</td>
              <td class="py-3 px-4">Salamanca</td>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-bold">🏆 1º Premio Mejor Tuna</span></td>
            </tr>
            <tr>
              <td class="py-3 px-4 font-bold">2023</td>
              <td class="py-3 px-4 font-semibold text-stone-900">Certamen Ciudad de Granada</td>
              <td class="py-3 px-4">Granada</td>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-bold">🥈 Mejor Pasacalles</span></td>
            </tr>
            <tr>
              <td class="py-3 px-4 font-bold">2022</td>
              <td class="py-3 px-4 font-semibold text-stone-900">Certamen de Tunas de Murcia</td>
              <td class="py-3 px-4">Murcia</td>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-bold">🥁 Mejor Pandereta</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= PANTALLA 4: TIENDA HOME ================= -->
    <div id="view-4-tienda" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">4 Tienda</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Tienda</h1>
        <p class="text-xs text-stone-500 mt-1">Productos oficiales de la Tuna de Derecho</p>
      </div>

      <div class="h-36 bg-stone-100 border border-stone-200 rounded-xl flex flex-col items-center justify-center text-center p-4">
        <span class="text-3xl mb-1">🛍️</span>
        <span class="font-serif-tuna font-bold text-lg text-stone-900">Merchandising Oficial de la Tuna</span>
        <span class="text-xs text-stone-500 mt-1">Envíos a toda España con fines de autofinanciación</span>
      </div>

      <div class="grid sm:grid-cols-2 gap-6">
        <div onclick="switchView('view-4-catalogo')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition">
          <div class="h-32 bg-stone-100 rounded flex items-center justify-center text-4xl mb-3">👕</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">4.1 Catálogo</h3>
          <p class="text-xs text-stone-600 mt-1">Todos los productos disponibles con selector de tallas y compra directa.</p>
          <span class="text-[#8B0000] font-bold text-xs block mt-3">Entrar al catálogo →</span>
        </div>

        <div onclick="switchView('view-4-cesta')" class="bg-white p-6 rounded-xl border border-stone-200 hover:border-[#8B0000] cursor-pointer shadow-sm transition">
          <div class="h-32 bg-stone-100 rounded flex items-center justify-center text-4xl mb-3">🛒</div>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">4.2 Cesta</h3>
          <p class="text-xs text-stone-600 mt-1">Revisa y modifica los productos añadidos antes de realizar el pago.</p>
          <span class="text-[#8B0000] font-bold text-xs block mt-3">Ver mi cesta actual →</span>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 4.1: CATÁLOGO CON FILTROS Y DETALLE FIEL AL WIREFRAME ================= -->
    <div id="view-4-catalogo" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-4-tienda" onclick="switchView('view-4-tienda')" class="hover:text-stone-900">Tienda</a> › 
        <span class="text-stone-900 font-semibold">4.1 Catálogo</span>
      </nav>
      <div class="flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Catálogo</h1>
          <p class="text-xs text-stone-500 mt-1">Filtra y elige tus productos oficiales</p>
        </div>
        <button onclick="switchView('view-4-cesta')" class="px-4 py-2 bg-[#8B0000] text-amber-200 font-bold rounded-lg text-xs uppercase tracking-wider">
          🛒 Ver Cesta (<span id="cat-badge">2</span>)
        </button>
      </div>

      <!-- Barra de Filtros Fiel a Catalogo.html -->
      <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm flex flex-wrap items-end gap-4 text-xs">
        <label class="flex flex-col gap-1 w-52">
          <span class="font-bold text-stone-700">Categoría</span>
          <select class="h-9 px-3 border border-stone-300 rounded bg-white outline-none">
            <option>Todas las categorías</option>
            <option>Ropa (Sudaderas)</option>
            <option>Música (CDs)</option>
            <option>Accesorios (Parches)</option>
            <option>Publicaciones (Cancioneros)</option>
          </select>
        </label>
        <label class="flex flex-col gap-1 w-52">
          <span class="font-bold text-stone-700">Precio</span>
          <select class="h-9 px-3 border border-stone-300 rounded bg-white outline-none">
            <option>Cualquier precio</option>
            <option>Menos de 10 €</option>
            <option>De 10 € a 25 €</option>
            <option>Más de 25 €</option>
          </select>
        </label>
        <button type="button" class="h-9 px-5 bg-stone-900 text-white font-bold rounded hover:bg-stone-800 transition">
          Aplicar filtros
        </button>
      </div>

      <!-- Layout con Grid de Productos + Panel de Detalle Derecho (como en Catalogo.html wireframe) -->
      <div class="grid lg:grid-cols-12 gap-8 items-start">
        
        <!-- Grid de 4 productos principales -->
        <div class="lg:col-span-8 grid sm:grid-cols-2 md:grid-cols-3 gap-4">
          <!-- Producto 1 -->
          <div class="bg-white p-3 rounded-xl border border-stone-200 shadow-sm flex flex-col justify-between">
            <div>
              <div class="h-28 bg-stone-100 rounded flex items-center justify-center text-4xl mb-2">👕</div>
              <strong class="text-xs text-stone-900 block font-serif-tuna">Sudadera Roja Derecho</strong>
              <div class="text-[#8B0000] font-bold text-xs mt-1">28,00 €</div>
            </div>
            <button onclick="selectProductDetail('Sudadera Roja Derecho', 28.00, '👕', 'Sudadera oficial con capucha y escudo bordado en oro de la UAL.')" class="mt-3 text-xs text-stone-600 hover:text-[#8B0000] underline font-semibold text-left">
              Ver detalle →
            </button>
          </div>

          <!-- Producto 2 -->
          <div class="bg-white p-3 rounded-xl border border-stone-200 shadow-sm flex flex-col justify-between">
            <div>
              <div class="h-28 bg-stone-100 rounded flex items-center justify-center text-4xl mb-2">💿</div>
              <strong class="text-xs text-stone-900 block font-serif-tuna">CD 25 Años de Ronda</strong>
              <div class="text-[#8B0000] font-bold text-xs mt-1">12,00 €</div>
            </div>
            <button onclick="selectProductDetail('CD 25 Años de Ronda', 12.00, '💿', 'Álbum grabado en estudio con 16 temas populares remasterizados.')" class="mt-3 text-xs text-stone-600 hover:text-[#8B0000] underline font-semibold text-left">
              Ver detalle →
            </button>
          </div>

          <!-- Producto 3 -->
          <div class="bg-white p-3 rounded-xl border border-stone-200 shadow-sm flex flex-col justify-between">
            <div>
              <div class="h-28 bg-stone-100 rounded flex items-center justify-center text-4xl mb-2">🎖️</div>
              <strong class="text-xs text-stone-900 block font-serif-tuna">Parche Beca en Oro</strong>
              <div class="text-[#8B0000] font-bold text-xs mt-1">6,50 €</div>
            </div>
            <button onclick="selectProductDetail('Parche Beca en Oro', 6.50, '🎖️', 'Escudo bordado con hilo de oro para capa o chaqueta.')" class="mt-3 text-xs text-stone-600 hover:text-[#8B0000] underline font-semibold text-left">
              Ver detalle →
            </button>
          </div>

          <!-- Producto 4 -->
          <div class="bg-white p-3 rounded-xl border border-stone-200 shadow-sm flex flex-col justify-between">
            <div>
              <div class="h-28 bg-stone-100 rounded flex items-center justify-center text-4xl mb-2">📖</div>
              <strong class="text-xs text-stone-900 block font-serif-tuna">Cancionero Ilustrado</strong>
              <div class="text-[#8B0000] font-bold text-xs mt-1">9,00 €</div>
            </div>
            <button onclick="selectProductDetail('Cancionero Ilustrado', 9.00, '📖', 'Libreto con acordes de guitarra y bandurria de 40 canciones.')" class="mt-3 text-xs text-stone-600 hover:text-[#8B0000] underline font-semibold text-left">
              Ver detalle →
            </button>
          </div>
        </div>

        <!-- Panel Lateral de Detalle del Producto (Exacto a Catalogo.html Wireframe) -->
        <div class="lg:col-span-4 bg-white p-5 rounded-xl border-2 border-stone-300 shadow-md text-xs space-y-3">
          <span class="badge-editorial text-[#8B0000]">DETALLE DEL PRODUCTO</span>
          <div id="detail-icon" class="h-36 bg-stone-100 rounded flex items-center justify-center text-6xl">👕</div>
          <h3 id="detail-title" class="font-serif-tuna font-bold text-base text-stone-900">Sudadera Roja Derecho</h3>
          <p id="detail-desc" class="text-stone-500 text-xs">Sudadera oficial con capucha y escudo bordado en oro de la UAL.</p>
          <div id="detail-price" class="text-lg font-serif-tuna font-bold text-[#8B0000]">28,00 €</div>

          <div class="flex gap-2 items-end pt-2">
            <label class="flex-1">
              <span class="font-bold text-stone-700 block mb-1">Talla</span>
              <select class="w-full h-8 px-2 border border-stone-300 rounded bg-white text-xs">
                <option>Talla M</option>
                <option selected>Talla L</option>
                <option>Talla XL</option>
              </select>
            </label>
            <label class="w-20">
              <span class="font-bold text-stone-700 block mb-1">Cantidad</span>
              <input type="number" value="1" min="1" class="w-full h-8 px-2 border border-stone-300 rounded text-xs text-center">
            </label>
          </div>

          <button onclick="addToCart('Sudadera Roja', 28.00)" class="w-full py-2.5 bg-[#8B0000] hover:bg-[#5C0000] text-white font-bold rounded uppercase tracking-wider text-xs shadow transition">
            Añadir a la cesta
          </button>

          <div class="flex justify-between pt-2 border-t border-stone-100">
            <button onclick="switchView('view-4-cesta')" class="text-[#8B0000] font-bold hover:underline">Ir a la cesta →</button>
            <button onclick="alert('Explora el resto del catálogo');" class="text-stone-500 hover:text-stone-800">Seguir comprando</button>
          </div>
        </div>

      </div>
    </div>

    <!-- ================= PANTALLA 4.2: CESTA ================= -->
    <div id="view-4-cesta" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-4-tienda" onclick="switchView('view-4-tienda')" class="hover:text-stone-900">Tienda</a> › 
        <span class="text-stone-900 font-semibold">4.2 Cesta</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Cesta</h1>
        <p class="text-xs text-stone-500 mt-1">Revisa y modifica los productos que has añadido</p>
      </div>

      <div class="grid lg:grid-cols-12 gap-8">
        <div class="lg:col-span-8 bg-white p-6 rounded-xl border border-stone-200 shadow-sm">
          <div class="divide-y divide-stone-100 text-xs">
            <div class="py-4 flex justify-between items-center">
              <div class="flex items-center gap-3">
                <span class="text-3xl">👕</span>
                <div>
                  <strong class="text-stone-900 block text-sm">Sudadera Roja Tuna de Derecho</strong>
                  <span class="text-stone-500">Talla L · Color Rojo Burdeos</span>
                </div>
              </div>
              <div class="text-right">
                <span class="font-bold text-stone-900 text-sm">28,00 €</span>
                <span class="text-stone-400 block text-[11px]">Cant: 1</span>
              </div>
            </div>

            <div class="py-4 flex justify-between items-center">
              <div class="flex items-center gap-3">
                <span class="text-3xl">🎖️</span>
                <div>
                  <strong class="text-stone-900 block text-sm">Parche Beca en Oro</strong>
                  <span class="text-stone-500">Bordado oficial para capa</span>
                </div>
              </div>
              <div class="text-right">
                <span class="font-bold text-stone-900 text-sm">6,50 €</span>
                <span class="text-stone-400 block text-[11px]">Cant: 1</span>
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-stone-200 flex justify-between items-center text-xs">
            <button onclick="switchView('view-4-catalogo')" class="text-[#8B0000] font-bold hover:underline">
              ← Seguir comprando
            </button>
            <button onclick="alert('Cesta vaciada');" class="text-stone-400 hover:text-red-700">
              Vaciar cesta
            </button>
          </div>
        </div>

        <div class="lg:col-span-4 bg-white p-6 rounded-xl border border-stone-200 shadow-sm text-xs space-y-4">
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900 pb-2 border-b border-stone-100">Resumen del Pedido</h3>
          <div class="flex justify-between text-stone-600">
            <span>Subtotal artículos:</span>
            <span class="font-bold text-stone-900">34,50 €</span>
          </div>
          <div class="flex justify-between text-stone-600">
            <span>Envío estándar Península:</span>
            <span class="font-bold text-green-700">GRATIS</span>
          </div>
          <div class="pt-3 border-t border-stone-200 flex justify-between text-sm font-bold text-stone-900">
            <span>Total:</span>
            <span class="text-lg text-[#8B0000] font-black">34,50 €</span>
          </div>

          <button onclick="switchView('view-4-envio')" class="w-full py-3 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded-lg uppercase tracking-wider text-xs shadow transition border border-[#D4AF37]">
            Tramitar Pedido (4.2.1) →
          </button>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 4.2.1.1: DIRECCIÓN DE ENVÍO Y PAGO ================= -->
    <div id="view-4-envio" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-4-tienda" onclick="switchView('view-4-tienda')" class="hover:text-stone-900">Tienda</a> › 
        <a href="#view-4-cesta" onclick="switchView('view-4-cesta')" class="hover:text-stone-900">Cesta</a> › 
        <span class="text-stone-900 font-semibold">4.2.1.1 Dirección de envío y pago</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Dirección de envío y pago</h1>
        <p class="text-xs text-stone-500 mt-1">Completa los datos para recibir tu pedido oficial</p>
      </div>

      <div class="bg-white p-8 rounded-xl border border-stone-200 shadow-sm max-w-2xl text-xs space-y-4">
        <div class="space-y-3">
          <label class="block font-bold text-stone-700 uppercase">Nombre del destinatario *</label>
          <input type="text" value="José Manuel Martínez" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          
          <label class="block font-bold text-stone-700 uppercase">Dirección postal completa *</label>
          <input type="text" placeholder="Calle, número, piso y puerta" value="Avda. del Mediterráneo, 120, 3ºB" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">

          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block font-bold text-stone-700 uppercase">Código Postal *</label>
              <input type="text" value="04009" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            </div>
            <div>
              <label class="block font-bold text-stone-700 uppercase">Ciudad *</label>
              <input type="text" value="Almería" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            </div>
          </div>
        </div>

        <div class="pt-4 border-t border-stone-200 space-y-2">
          <span class="font-bold text-stone-800 uppercase block">4.2.1.1.1 Método de Pago</span>
          <div class="p-3 bg-stone-50 rounded border border-stone-200 space-y-2">
            <label class="flex items-center gap-2 cursor-pointer font-semibold text-stone-900">
              <input type="radio" name="pago" checked class="text-[#8B0000]">
              <span>Tarjeta de Crédito / Débito (Pasarela Segura SSL)</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer text-stone-700">
              <input type="radio" name="pago" class="text-[#8B0000]">
              <span>Bizum Directo al número oficial (+34 600 123 456)</span>
            </label>
          </div>
        </div>

        <div class="pt-4 flex justify-between items-center">
          <button onclick="switchView('view-4-cesta')" class="text-stone-500 hover:text-stone-900">← Volver a la cesta</button>
          <button onclick="alert('¡Pago confirmado! Recibo generado: #PED-2026-904. Recibirás el tracking por email.');" class="px-6 py-2.5 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded uppercase tracking-wider shadow border border-[#D4AF37]">
            Confirmar y Pagar (34,50 €)
          </button>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 5: CANCIONERO ================= -->
    <div id="view-5" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">5 Cancionero</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Cancionero</h1>
        <p class="text-xs text-stone-500 mt-1">Repertorio de ronda, pasodobles y pistas en Spotify</p>
      </div>

      <div class="grid md:grid-cols-2 gap-6">
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm space-y-3 text-xs">
          <span class="badge-editorial text-[#8B0000]">NODO 5.1</span>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">Nuestro Repertorio de Canciones</h3>
          <p class="text-stone-600">Letras tradicionales con acordes para guitarra y bandurria:</p>

          <details class="p-3 bg-stone-50 rounded border border-stone-200" open>
            <summary class="font-bold text-stone-900 cursor-pointer">🌹 Clavelitos</summary>
            <p class="mt-2 text-stone-600 font-serif-tuna italic leading-relaxed">
              "Mocita dame el clavel, dame el clavel de tu boca,<br>
              que pa' eso no hay que tener mucha vergüenza ni poca.<br>
              Yo te daré un cascabel, te lo prometo mocita,<br>
              si tú me das ese clavel que llevas en tu boquita..."
            </p>
          </details>

          <details class="p-3 bg-stone-50 rounded border border-stone-200">
            <summary class="font-bold text-stone-900 cursor-pointer">🎓 Pasacalles de Fonseca</summary>
            <p class="mt-2 text-stone-600 font-serif-tuna italic leading-relaxed">
              "Adiós villa de Fonseca, ya me marcho de aquí,<br>
              no te olvides de este tuno que suspira por ti..."
            </p>
          </details>
        </div>

        <div class="bg-[#141414] text-white p-6 rounded-xl border-2 border-green-500 shadow-md flex flex-col justify-between text-xs">
          <div>
            <span class="badge-editorial text-green-400">NODO 5.2</span>
            <h3 class="font-serif-tuna font-bold text-xl text-white mt-1 mb-2">Escúchanos en Spotify</h3>
            <p class="text-stone-300 mb-4">Álbum oficial "25 Años de Ronda" con la Tuna de Derecho de Almería:</p>

            <div class="p-3 bg-stone-900 rounded border border-stone-800 space-y-2">
              <div class="flex justify-between items-center">
                <span>1. Clavelitos</span>
                <span class="font-mono text-stone-400">03:12</span>
              </div>
              <div class="flex justify-between items-center">
                <span>2. Serenata Almeriense</span>
                <span class="font-mono text-stone-400">04:05</span>
              </div>
              <div class="flex justify-between items-center">
                <span>3. La Morena de mi Copla</span>
                <span class="font-mono text-stone-400">02:58</span>
              </div>
            </div>
          </div>

          <a href="https://spotify.com" target="_blank" class="mt-6 w-full py-2.5 bg-green-500 hover:bg-green-400 text-stone-950 font-bold uppercase tracking-wider text-center rounded transition">
            Abrir en Spotify Oficial
          </a>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 6: ÚNETE A NOSOTROS ================= -->
    <div id="view-6" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">6 Únete a nosotros</span>
      </nav>
      <div>
        <h1 class="text-3xl font-serif-tuna font-bold text-stone-900">Únete a nosotros</h1>
        <p class="text-xs text-stone-500 mt-1">Formulario de inscripción para novatos y horarios de ensayo</p>
      </div>

      <div class="grid md:grid-cols-2 gap-6">
        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm text-xs space-y-3">
          <span class="badge-editorial text-[#8B0000]">NODO 6.1</span>
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900">Formulario para unirse</h3>
          <p class="text-stone-600">¿Estudias en la UAL? No necesitas experiencia musical previa, te formamos gratis:</p>

          <form onsubmit="alert('¡Inscripción recibida! El Tuno Mayor te contactará para invitarte al local de ensayo.'); return false;" class="space-y-3">
            <input type="text" placeholder="Nombre completo" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            <input type="tel" placeholder="Teléfono móvil" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            <input type="text" placeholder="Grado en la Universidad de Almería" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            <select class="w-full px-3 py-2 border border-stone-300 rounded outline-none bg-white">
              <option>Quiero aprender desde cero</option>
              <option>Sé tocar algo de guitarra</option>
              <option>Sé tocar bandurria o laúd</option>
              <option>Toco percusión / pandereta</option>
            </select>
            <button type="submit" class="w-full py-2.5 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded uppercase tracking-wider text-xs">
              Enviar Solicitud
            </button>
          </form>
        </div>

        <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm text-xs flex flex-col justify-between">
          <div class="space-y-3">
            <span class="badge-editorial text-[#8B0000]">NODO 6.2</span>
            <h3 class="font-serif-tuna font-bold text-lg text-stone-900">Local de Ensayo</h3>
            <div class="p-3 bg-stone-50 rounded border border-stone-200 space-y-1">
              <strong>📍 Facultad de Derecho (Planta Baja):</strong>
              <p class="text-stone-600">Universidad de Almería, Ctra. Sacramento s/n, La Cañada.</p>
            </div>
            <div class="p-3 bg-stone-50 rounded border border-stone-200 space-y-1">
              <strong>🕒 Días y Horarios:</strong>
              <p class="text-stone-600">Martes y Jueves de 19:30 h a 21:30 h.</p>
            </div>
          </div>
          <div class="mt-4 p-3 bg-[#5C0000] text-white rounded text-center">
            Teléfono del Local: <strong>+34 600 123 456</strong>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 7: INICIO DE SESIÓN ================= -->
    <div id="view-7" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <span class="text-stone-900 font-semibold">7 Inicio de sesión</span>
      </nav>

      <div class="max-w-md mx-auto bg-white p-8 rounded-xl border border-stone-200 shadow-xl text-xs space-y-4">
        <div class="text-center">
          <div class="w-12 h-12 rounded-full bg-[#8B0000] text-amber-300 font-serif-tuna font-bold text-lg flex items-center justify-center mx-auto mb-2 border-2 border-[#D4AF37]">TD</div>
          <h2 class="font-serif-tuna font-bold text-2xl text-stone-900">Inicio de sesión</h2>
          <p class="text-stone-500 mt-1">Accede con tus credenciales de cliente</p>
        </div>

        <form onsubmit="window.location.href='cliente.html'; return false;" class="space-y-3">
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Correo electrónico</label>
            <input type="email" value="cliente@almeria.es" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <div class="flex justify-between items-center mb-1">
              <label class="block font-bold text-stone-700 uppercase">Contraseña</label>
              <button type="button" onclick="switchView('view-7-recuperar')" class="text-[#8B0000] hover:underline">7.1 ¿Olvidaste la clave?</button>
            </div>
            <input type="password" value="********" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <button type="submit" class="w-full py-2.5 bg-[#8B0000] hover:bg-[#5C0000] text-white font-bold rounded uppercase tracking-wider">
            Entrar como Cliente
          </button>
        </form>

        <div class="pt-4 border-t border-stone-100 text-center text-stone-600">
          Nodo 7.2: ¿No tienes cuenta? <button onclick="switchView('view-7-registro')" class="text-[#8B0000] font-bold underline">Registrarse</button>
        </div>
      </div>
    </div>

    <!-- ================= PANTALLA 7.1: RECUPERAR CONTRASEÑA ================= -->
    <div id="view-7-recuperar" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-7" onclick="switchView('view-7')" class="hover:text-stone-900">Inicio de sesión</a> › 
        <span class="text-stone-900 font-semibold">7.1 Recuperar contraseña</span>
      </nav>
      <div class="max-w-md mx-auto bg-white p-8 rounded-xl border border-stone-200 shadow-md text-xs space-y-4">
        <h2 class="font-serif-tuna font-bold text-2xl text-stone-900">Recuperar contraseña</h2>
        <p class="text-stone-500">Indica tu correo electrónico y te enviaremos un enlace de recuperación.</p>
        <form onsubmit="alert('Enlace de restablecimiento enviado a tu correo.'); switchView('view-7'); return false;" class="space-y-3">
          <input type="email" placeholder="tu@email.com" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          <button type="submit" class="w-full py-2 bg-stone-900 text-white font-bold rounded uppercase tracking-wider">Enviar enlace</button>
        </form>
      </div>
    </div>

    <!-- ================= PANTALLA 7.2: REGISTRO ================= -->
    <div id="view-7-registro" class="subview-content hidden space-y-6">
      <nav class="text-xs text-stone-500">
        <a href="#view-0" onclick="switchView('view-0')" class="hover:text-stone-900">Inicio</a> › 
        <a href="#view-7" onclick="switchView('view-7')" class="hover:text-stone-900">Inicio de sesión</a> › 
        <span class="text-stone-900 font-semibold">7.2 Registrarse</span>
      </nav>
      <div class="max-w-md mx-auto bg-white p-8 rounded-xl border border-stone-200 shadow-md text-xs space-y-4">
        <h2 class="font-serif-tuna font-bold text-2xl text-stone-900">Registrarse como Cliente</h2>
        <p class="text-stone-500">Crea tu cuenta para gestionar contratos y pedidos de la tienda.</p>
        <form onsubmit="alert('¡Cuenta creada con éxito! Redirigiendo a tu panel...'); window.location.href='cliente.html'; return false;" class="space-y-3">
          <input type="text" placeholder="Nombre completo" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          <input type="email" placeholder="Correo electrónico" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          <input type="tel" placeholder="Teléfono" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          <input type="password" placeholder="Contraseña (mínimo 8 caracteres)" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          <button type="submit" class="w-full py-2.5 bg-[#8B0000] text-amber-200 font-bold rounded uppercase tracking-wider">Crear Cuenta</button>
        </form>
      </div>
    </div>

  </main>

  <!-- ========================================================================= -->
  <!-- FOOTER FIEL AL WIREFRAME: CONTACTO · SÍGUENOS · LEGAL · ÚNETE -->
  <!-- ========================================================================= -->
  <footer class="bg-[#120404] text-stone-300 border-t-2 border-[#D4AF37] pt-12 pb-8 text-xs mt-auto">
    <div class="max-w-7xl mx-auto px-4 grid sm:grid-cols-2 md:grid-cols-4 gap-8 pb-8 border-b border-stone-800">
      
      <!-- Contacto -->
      <div>
        <p class="font-serif-tuna font-bold text-amber-300 text-sm mb-3 uppercase tracking-wider">Contacto</p>
        <p class="text-stone-300 font-semibold">Tuna Facultad de Derecho UAL</p>
        <p class="text-stone-400 mt-1">tuna.derecho.almeria@gmail.com</p>
        <p class="text-white font-bold mt-2">Tel: +34 600 123 456</p>
        <p class="text-white font-bold">Tel: +34 612 345 678</p>
      </div>

      <!-- Síguenos -->
      <div>
        <p class="font-serif-tuna font-bold text-amber-300 text-sm mb-3 uppercase tracking-wider">Síguenos</p>
        <ul class="space-y-1.5 text-stone-400">
          <li><a href="https://instagram.com" target="_blank" class="hover:text-amber-300">Instagram: @tunaderechoalmeria</a></li>
          <li><a href="https://tiktok.com" target="_blank" class="hover:text-amber-300">TikTok: @tunaderechoual</a></li>
          <li><a href="https://youtube.com" target="_blank" class="hover:text-amber-300">YouTube: Tuna Derecho UAL</a></li>
          <li><a href="https://spotify.com" target="_blank" class="hover:text-amber-300">Spotify: Tuna Derecho Almería</a></li>
        </ul>
      </div>

      <!-- Legal -->
      <div>
        <p class="font-serif-tuna font-bold text-amber-300 text-sm mb-3 uppercase tracking-wider">Legal</p>
        <ul class="space-y-1.5 text-stone-400">
          <li><a href="#" class="hover:text-white">Aviso legal</a></li>
          <li><a href="#" class="hover:text-white">Política de privacidad</a></li>
          <li><a href="#" class="hover:text-white">Política de cookies</a></li>
          <li><a href="#" class="hover:text-white">Estatutos de la Asociación</a></li>
        </ul>
      </div>

      <!-- Únete -->
      <div>
        <p class="font-serif-tuna font-bold text-amber-300 text-sm mb-3 uppercase tracking-wider">Únete</p>
        <p class="text-stone-400">¿Quieres ser parte de la Tuna?</p>
        <button onclick="switchView('view-6')" class="mt-2 text-amber-300 font-bold hover:underline block">
          Formulario para unirse (6.1) →
        </button>
        <button onclick="switchView('view-6-ensayo')" class="text-stone-400 hover:text-white block mt-1">
          Local de ensayo (6.2)
        </button>
      </div>

    </div>

    <!-- Copyright -->
    <div class="max-w-7xl mx-auto px-4 pt-6 flex flex-col sm:flex-row items-center justify-between text-[11px] text-stone-500 gap-2">
      <div>© 2026 TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA. TODOS LOS DERECHOS RESERVADOS.</div>
      <div class="text-amber-400 font-semibold">Diseño corporativo en Rojo Derecho (#8B0000) y Oro</div>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- BOTÓN FLOTANTE PERMANENTE DE WHATSAPP -->
  <!-- ========================================================================= -->
  <a href="https://wa.me/34600123456" target="_blank" class="fixed bottom-6 right-6 z-50 flex items-center gap-2 px-4 py-3 rounded-full bg-green-700 hover:bg-green-600 text-white font-bold text-xs shadow-2xl transition hover:scale-105 border-2 border-white pulse-call" title="WhatsApp Directo">
    <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347m-5.421 7.403"/></svg>
    <span class="hidden sm:inline">WhatsApp Tuna: +34 600 123 456</span>
  </a>

  <!-- SCRIPT INTERACTIVO DE NAVEGACIÓN Y CARRITO -->
  <script>
    function switchView(viewId) {
      document.querySelectorAll('.subview-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.subview-pill').forEach(el => el.classList.remove('active'));

      const target = document.getElementById(viewId);
      if (target) {
        target.classList.remove('hidden');
        window.scrollTo({ top: 90, behavior: 'smooth' });
      }

      // Marcar botón activo en barra
      const btn = Array.from(document.querySelectorAll('.subview-pill')).find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes(viewId));
      if (btn) btn.classList.add('active');
    }

    let cartCount = 2;
    function addToCart(title, price) {
      cartCount++;
      document.getElementById('cart-counter').textContent = cartCount;
      const b = document.getElementById('cat-badge');
      if (b) b.textContent = cartCount;
      alert('¡Añadido a la cesta! ' + title + ' (' + price.toFixed(2) + ' €). Artículos en cesta: ' + cartCount);
    }

    function selectProductDetail(title, price, icon, desc) {
      document.getElementById('detail-title').textContent = title;
      document.getElementById('detail-price').textContent = price.toFixed(2) + ' €';
      document.getElementById('detail-icon').textContent = icon;
      document.getElementById('detail-desc').textContent = desc;
    }
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    content = get_visitante_html()
    target = r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\visitante.html"
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Guardado:", target)

