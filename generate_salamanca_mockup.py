# -*- coding: utf-8 -*-
"""
Generador del Mockup Oficial de la Tuna de Derecho de Almería
Diseño inspirado en la elegancia de tunasalamanca.com:
- Tipografía editorial elegante, serif clásico en titulares y subtítulos refinados.
- Paleta: Rojo corporativo de Derecho (#8B0000 / #991B1B / #7F1D1D), detalles en dorado noble (#D4AF37 / #C5A059), blanco puro, crema suave (#FAF7F2 / #F8FAFC) y antracita profundo (#121212).
- Micro-bloques con etiquetas en mayúsculas ("MÚSICA · UNIVERSIDAD · TRADICIÓN"), numeración editorial (01, 02, 03, 04).
- Cajas de hitos y momentos: Siglo XIII / Siglo XIX / Actualidad / Disco 2026 / Ensayos / Certámenes.
- Datos de contacto ultra visibles con nombres de responsables (ej. Tuno Mayor, Relaciones Públicas), teléfonos directos, redes y WhatsApp.
- Integración completa de los 3 PERFILES DE USUARIO (Visitante con Tienda y Cesta, Cliente y Administrador) según los árboles de contenido y wireframes.
"""

import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería · Web Oficial</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {
      --rojo-tuna: #8B0000;
      --rojo-profundo: #670000;
      --rojo-carmesí: #991B1B;
      --dorado: #D4AF37;
      --dorado-suave: #F3E5AB;
      --dorado-oscuro: #AA820A;
      --fondo-calido: #FAF7F2;
      --carbon: #141414;
      --texto-mutado: #6B7280;
    }

    body {
      background-color: var(--fondo-calido);
      color: #1F2937;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    .font-serif-tuna {
      font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
    }

    /* Fondo hero estilo Salamanca con textura solemne */
    .hero-salamanca-style {
      background: linear-gradient(180deg, #180505 0%, #350909 50%, #4D0E0E 100%);
      position: relative;
    }
    .hero-salamanca-style::after {
      content: "";
      position: absolute;
      inset: 0;
      background-image: radial-gradient(rgba(212, 175, 55, 0.12) 1px, transparent 1px);
      background-size: 28px 28px;
      pointer-events: none;
    }

    .badge-editorial {
      letter-spacing: 0.22em;
      text-transform: uppercase;
      font-size: 0.72rem;
      font-weight: 700;
    }

    .border-gold {
      border-color: #D4AF37;
    }

    .tab-profile-btn.active {
      background-color: #FFFFFF;
      color: #8B0000;
      font-weight: 700;
      border-bottom: 3px solid #D4AF37;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .client-sidebar-btn.active {
      background-color: #8B0000;
      color: #FFFFFF;
      font-weight: 600;
    }

    .admin-sidebar-btn.active {
      background-color: #8B0000;
      color: #FFFFFF;
      font-weight: 600;
    }

    .pulse-contact {
      animation: pulse-ring 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    @keyframes pulse-ring {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.05); }
    }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-red-900 selection:text-amber-200">

  <!-- ========================================================================= -->
  <!-- 0. BARRA SUPERIOR FIJA: SELECTOR DE PERFILES (VISITANTE / CLIENTE / ADMIN) -->
  <!-- ========================================================================= -->
  <div class="sticky top-0 z-50 bg-[#121212] border-b border-amber-600/40 text-white shadow-xl">
    <div class="max-w-7xl mx-auto px-4 py-2 flex flex-col md:flex-row items-center justify-between gap-2 text-xs">
      <div class="flex items-center gap-2.5">
        <span class="w-6 h-6 rounded bg-red-900 text-amber-300 font-serif-tuna font-black flex items-center justify-center border border-amber-500 text-xs">TD</span>
        <div>
          <span class="text-amber-400 font-bold tracking-wider uppercase text-[10px] block">MOCKUP OFICIAL · SELECTOR DE PERFIL</span>
          <span class="text-slate-300 text-[11px]">Tuna de la Facultad de Derecho de Almería</span>
        </div>
      </div>

      <!-- Selector interactivo de los 3 perfiles -->
      <div class="flex items-center bg-[#1f1f1f] p-1 rounded-xl border border-slate-700">
        <button onclick="switchProfile('visitante')" id="tab-visitante" class="tab-profile-btn active px-3.5 py-1.5 rounded-lg text-xs transition flex items-center gap-1.5">
          <span>🌐</span> Visitante <span class="text-[10px] opacity-75">(Público)</span>
        </button>
        <button onclick="switchProfile('cliente')" id="tab-cliente" class="tab-profile-btn px-3.5 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white transition flex items-center gap-1.5">
          <span>👤</span> Cliente <span class="text-[10px] opacity-75">(Registrado)</span>
        </button>
        <button onclick="switchProfile('admin')" id="tab-admin" class="tab-profile-btn px-3.5 py-1.5 rounded-lg text-xs text-slate-300 hover:text-white transition flex items-center gap-1.5">
          <span>⚙️</span> Administrador <span class="text-[10px] opacity-75">(Gestión)</span>
        </button>
      </div>

      <!-- Teléfono directo en cabecera superior -->
      <div class="hidden lg:flex items-center gap-3">
        <a href="tel:+34600123456" class="flex items-center gap-1.5 px-3 py-1 bg-red-800 hover:bg-red-700 text-white rounded-full font-bold border border-amber-400/80 shadow pulse-contact">
          <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          Tuno Mayor: +34 600 123 456
        </a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- BARRA DE CONTACTO CORPORATIVA ROJA Y DORADA (ULTRA VISIBLE) -->
  <!-- ========================================================================= -->
  <div class="bg-[#670000] text-white border-b-2 border-[#D4AF37] py-2.5 px-4 text-xs shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex flex-wrap items-center gap-4 sm:gap-6">
        <a href="tel:+34600123456" class="flex items-center gap-2 font-black text-sm text-amber-300 hover:text-amber-200 transition">
          <span class="p-1 bg-red-900 rounded-full">📞</span>
          TELÉFONOS OFICIALES: +34 600 123 456 · +34 612 345 678
        </a>
        <a href="mailto:tuna.derecho.almeria@gmail.com" class="flex items-center gap-1.5 text-slate-200 hover:text-amber-300 transition">
          <span>✉️</span> tuna.derecho.almeria@gmail.com
        </a>
      </div>

      <!-- Enlaces sociales con badges -->
      <div class="flex items-center gap-3">
        <span class="badge-editorial text-amber-300 hidden md:inline">Redes Oficiales:</span>
        <div class="flex items-center gap-2">
          <a href="https://instagram.com" target="_blank" class="px-2 py-0.5 rounded bg-red-900 hover:bg-pink-700 transition text-[11px] font-bold text-white flex items-center gap-1" title="Instagram">
            <span>📷</span> @tunaderechoalmeria
          </a>
          <a href="https://tiktok.com" target="_blank" class="px-2 py-0.5 rounded bg-red-900 hover:bg-black transition text-[11px] font-bold text-white flex items-center gap-1" title="TikTok">
            <span>🎵</span> TikTok
          </a>
          <a href="https://facebook.com" target="_blank" class="px-2 py-0.5 rounded bg-red-900 hover:bg-blue-700 transition text-[11px] font-bold text-white flex items-center gap-1" title="Facebook">
            <span>👥</span> Facebook
          </a>
          <a href="https://youtube.com" target="_blank" class="px-2 py-0.5 rounded bg-red-900 hover:bg-red-700 transition text-[11px] font-bold text-white flex items-center gap-1" title="YouTube">
            <span>▶️</span> YouTube
          </a>
          <a href="https://spotify.com" target="_blank" class="px-2 py-0.5 rounded bg-red-900 hover:bg-green-700 transition text-[11px] font-bold text-white flex items-center gap-1" title="Spotify">
            <span>🟢</span> Spotify
          </a>
        </div>
      </div>
    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- 1. PERFIL: VISITANTE (DISEÑO INSPIRADO EN TUNASALAMANCA.COM) -->
  <!-- ========================================================================= -->
  <div id="profile-visitante" class="flex-1 flex flex-col">

    <!-- Header Principal Visitante (Estilo Salamantino: Tipografía solemne y espaciada) -->
    <header class="bg-white/95 backdrop-blur-md border-b border-stone-200 sticky top-12 z-40 transition-all">
      <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between gap-4">
        
        <!-- Logo con Escudo y Tipografía Clásica -->
        <a href="#visitante-inicio" onclick="showVisitanteSection('visitante-inicio')" class="flex items-center gap-3 group">
          <div class="w-12 h-12 rounded-full bg-[#8B0000] border-2 border-[#D4AF37] flex items-center justify-center text-amber-300 font-serif-tuna font-black text-xl shadow-md group-hover:scale-105 transition">
            TD
          </div>
          <div>
            <div class="font-serif-tuna font-black text-xl tracking-tight text-[#670000] leading-none">
              TUNA DE DERECHO
            </div>
            <div class="badge-editorial text-[#8B0000] text-[9px] mt-1 font-bold">
              Universidad de Almería · Beca Roja
            </div>
          </div>
        </a>

        <!-- Navegación Pública según Árbol de Contenidos -->
        <nav class="hidden xl:flex items-center gap-6 text-[13px] font-medium text-stone-700">
          <button onclick="showVisitanteSection('visitante-inicio')" class="hover:text-[#8B0000] transition">Inicio</button>
          <button onclick="showVisitanteSection('visitante-conoce')" class="hover:text-[#8B0000] transition">1. Conoce la Tuna</button>
          <button onclick="showVisitanteSection('visitante-contratacion')" class="hover:text-[#8B0000] transition">2. Contratación</button>
          <button onclick="showVisitanteSection('visitante-multimedia')" class="hover:text-[#8B0000] transition">3. Vídeos y Certámenes</button>
          <button onclick="showVisitanteSection('visitante-tienda')" class="px-3 py-1 rounded-full bg-red-50 text-[#8B0000] font-bold border border-red-200 hover:bg-red-100 transition flex items-center gap-1.5 shadow-sm">
            <span>🛍️</span> 4. Tienda Oficial
          </button>
          <button onclick="showVisitanteSection('visitante-cancionero')" class="hover:text-[#8B0000] transition">5. Cancionero</button>
          <button onclick="showVisitanteSection('visitante-unete')" class="hover:text-[#8B0000] transition">6. Únete</button>
        </nav>

        <!-- Acciones Rápidas: Cesta + Login + Contratar -->
        <div class="flex items-center gap-2.5">
          <!-- Cesta Tienda -->
          <button onclick="showVisitanteSection('visitante-cesta')" class="px-3 py-1.5 rounded-lg border border-stone-300 bg-stone-50 hover:bg-stone-100 text-stone-800 font-semibold text-xs flex items-center gap-1.5 transition">
            <span>🛒</span> Cesta <span id="cart-counter" class="bg-[#8B0000] text-white rounded-full px-1.5 py-0.2 text-[10px] font-bold">2</span>
          </button>

          <!-- Acceso / Login -->
          <button onclick="showVisitanteSection('visitante-acceso')" class="px-3 py-1.5 rounded-lg border border-[#8B0000] text-[#8B0000] font-bold text-xs hover:bg-red-50 transition">
            7. Iniciar sesión
          </button>

          <!-- Solicitar Actuación estilo botón Salamanca -->
          <button onclick="showVisitanteSection('visitante-contratacion')" class="px-4 py-2 rounded-lg bg-[#8B0000] hover:bg-[#670000] text-amber-200 font-bold text-xs shadow-md transition border border-[#D4AF37] tracking-wider uppercase">
            Solicitar Actuación
          </button>
        </div>
      </div>
    </header>

    <!-- Sub-Barra de Navegación Rápida para el Evaluador -->
    <div class="bg-stone-100 border-b border-stone-200 py-1.5 px-4 text-xs overflow-x-auto whitespace-nowrap">
      <div class="max-w-7xl mx-auto flex items-center gap-2">
        <span class="font-bold text-stone-500 uppercase tracking-wider text-[10px]">Vistas del Árbol de Visitante:</span>
        <button onclick="showVisitanteSection('visitante-inicio')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">0. Portada</button>
        <button onclick="showVisitanteSection('visitante-conoce')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">1. Historia y Miembros</button>
        <button onclick="showVisitanteSection('visitante-contratacion')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">2. Contratación</button>
        <button onclick="showVisitanteSection('visitante-multimedia')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">3. Multimedia & Certámenes</button>
        <button onclick="showVisitanteSection('visitante-tienda')" class="px-2.5 py-1 rounded bg-[#8B0000] text-amber-200 font-bold border border-amber-600">4. Tienda (Catálogo)</button>
        <button onclick="showVisitanteSection('visitante-cesta')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">4.2 Cesta & Pasarela</button>
        <button onclick="showVisitanteSection('visitante-cancionero')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">5. Cancionero & Spotify</button>
        <button onclick="showVisitanteSection('visitante-unete')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">6. Únete (Formulario/Ensayos)</button>
        <button onclick="showVisitanteSection('visitante-acceso')" class="px-2.5 py-1 rounded bg-white hover:bg-red-50 text-stone-700 font-medium border border-stone-300">7. Acceso / Registro</button>
      </div>
    </div>


    <!-- ================= CONTENIDOS VISITANTE ================= -->

    <!-- SECCIÓN 0: INICIO VISITANTE (HERO + BLOQUES HISTÓRICOS + QUÉ HACEMOS) -->
    <div id="visitante-inicio" class="visitante-subview">

      <!-- HERO EDITORIAL (Estilo: "Salamanca se canta con capa y bandurria" adaptado a Almería) -->
      <section class="hero-salamanca-style text-white py-20 lg:py-28 relative overflow-hidden">
        <div class="max-w-5xl mx-auto px-4 relative z-10 text-center">
          
          <div class="badge-editorial text-[#D4AF37] mb-4">
            MÚSICA · UNIVERSIDAD · TRADICIÓN · DESDE 1995
          </div>

          <h1 class="text-4xl sm:text-6xl lg:text-7xl font-serif-tuna font-normal mb-6 tracking-tight text-stone-100 leading-tight">
            Almería se canta<br>
            <span class="italic text-amber-200 font-serif-tuna">con capa y bandurria</span>
          </h1>

          <p class="text-base sm:text-lg lg:text-xl text-stone-300 max-w-3xl mx-auto mb-10 font-light leading-relaxed">
            Una tradición universitaria que recorre plazas, certámenes y celebraciones con un repertorio de pasodobles, serenatas, boleros y canciones de ronda estudiantil.
          </p>

          <!-- Botones de Acción Estilo Salamanca -->
          <div class="flex flex-wrap items-center justify-center gap-4 mb-14">
            <button onclick="showVisitanteSection('visitante-contratacion')" class="px-8 py-3.5 rounded-lg bg-[#D4AF37] hover:bg-amber-400 text-stone-950 font-bold text-sm tracking-wider uppercase shadow-xl transition">
              Solicitar una Actuación
            </button>
            <button onclick="showVisitanteSection('visitante-cancionero')" class="px-8 py-3.5 rounded-lg bg-transparent border-2 border-stone-300 hover:border-amber-300 text-stone-100 font-bold text-sm tracking-wider uppercase transition">
              Escuchar la Tuna
            </button>
            <button onclick="showVisitanteSection('visitante-tienda')" class="px-8 py-3.5 rounded-lg bg-[#8B0000] hover:bg-[#670000] text-amber-200 border border-[#D4AF37] font-bold text-sm tracking-wider uppercase shadow-lg transition flex items-center gap-2">
              <span>🛍️</span> Tienda Oficial
            </button>
          </div>

          <!-- TARJETA DESTACADA DE CONTACTO TELEFÓNICO DIRECTO -->
          <div class="inline-flex flex-wrap items-center justify-center gap-6 p-5 rounded-2xl bg-black/60 border border-[#D4AF37] backdrop-blur-md shadow-2xl">
            <div class="text-left flex items-center gap-3">
              <span class="w-10 h-10 rounded-full bg-red-900 border border-amber-400 flex items-center justify-center text-lg">📞</span>
              <div>
                <span class="badge-editorial text-amber-400 block text-[9px]">CONTACTO DIRECTO / CONTRATACIONES</span>
                <a href="tel:+34600123456" class="text-xl sm:text-2xl font-serif-tuna font-bold text-white hover:text-amber-300 transition">+34 600 123 456</a>
              </div>
            </div>
            <div class="h-10 w-px bg-stone-700 hidden sm:block"></div>
            <div class="text-left flex items-center gap-3">
              <span class="w-10 h-10 rounded-full bg-green-800 border border-green-400 flex items-center justify-center text-lg">💬</span>
              <div>
                <span class="badge-editorial text-green-300 block text-[9px]">ATENCIÓN INMEDIATA POR WHATSAPP</span>
                <a href="https://wa.me/34600123456" target="_blank" class="text-base sm:text-lg font-bold text-white hover:text-green-300 transition">Enviar Mensaje Directo</a>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- FRANJA DE HITOS TEMPORALES (Inspirado en tunasalamanca.com: Siglo XIII, Siglo XIX, Actualidad, Disco, Ensayos, Viajes) -->
      <section class="border-y border-stone-200 bg-white py-8">
        <div class="max-w-7xl mx-auto px-4 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6 text-center">
          
          <div class="border-r border-stone-100 last:border-none px-2">
            <div class="font-serif-tuna font-bold text-lg text-[#8B0000]">1995</div>
            <div class="text-xs text-stone-600 mt-0.5">Fundación Oficial en la UAL</div>
          </div>

          <div class="border-r border-stone-100 last:border-none px-2">
            <div class="font-serif-tuna font-bold text-lg text-[#8B0000]">Beca Roja</div>
            <div class="text-xs text-stone-600 mt-0.5">Facultad de Derecho</div>
          </div>

          <div class="border-r border-stone-100 last:border-none px-2">
            <div class="font-serif-tuna font-bold text-lg text-[#8B0000]">Actualidad</div>
            <div class="text-xs text-stone-600 mt-0.5">¡Cuadrilla activa y en gira!</div>
          </div>

          <div class="border-r border-stone-100 last:border-none px-2">
            <div class="font-serif-tuna font-bold text-lg text-[#8B0000]">Disco 2026</div>
            <div class="text-xs text-stone-600 mt-0.5">"25 Años de Ronda"</div>
          </div>

          <div class="border-r border-stone-100 last:border-none px-2">
            <div class="font-serif-tuna font-bold text-lg text-[#8B0000]">Ensayos</div>
            <div class="text-xs text-stone-600 mt-0.5">Facultad de Derecho (Martes/Jueves)</div>
          </div>

          <div class="px-2">
            <div class="font-serif-tuna font-bold text-lg text-[#8B0000]">Certámenes</div>
            <div class="text-xs text-stone-600 mt-0.5">Por toda España y Portugal</div>
          </div>

        </div>
      </section>

      <!-- SECCIÓN QUIÉNES SOMOS (ESTILO EDITORIAL SALAMANCA) -->
      <section class="max-w-6xl mx-auto px-4 py-16 lg:py-24">
        <div class="grid lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-5">
            <div class="badge-editorial text-[#8B0000] mb-2">QUIÉNES SOMOS</div>
            <h2 class="text-3xl sm:text-4xl font-serif-tuna text-stone-900 leading-tight">
              La voz estudiantil de la Facultad de Derecho
            </h2>
            <div class="w-12 h-1 bg-[#D4AF37] my-6"></div>
            <p class="text-stone-600 text-sm leading-relaxed mb-4">
              La Tuna de la Facultad de Derecho de Almería representa la centenaria tradición estudiantil que une música, hermandad y vida universitaria. Vestidos con jubón, gregüescos y la característica beca roja, llevamos la picaresca y la alegría por calles, escenarios y balcones.
            </p>
            <p class="text-stone-600 text-sm leading-relaxed mb-6">
              Reunimos a estudiantes y antiguos alumnos que mantienen vivo el repertorio de pasodobles, habaneras, rondallas y música tradicional española.
            </p>
            <button onclick="showVisitanteSection('visitante-conoce')" class="text-[#8B0000] font-bold text-sm hover:underline flex items-center gap-1">
              Conoce nuestra historia y miembros →
            </button>
          </div>

          <div class="lg:col-span-7 grid sm:grid-cols-2 gap-4">
            <div class="p-6 bg-white rounded-xl border border-stone-200 shadow-sm">
              <span class="text-3xl text-[#8B0000] block mb-3">🏛️</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Tradición Académica</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Vinculados a la Universidad de Almería, participamos en actos solemnes, aperturas de curso y graduaciones oficiales.</p>
            </div>
            <div class="p-6 bg-white rounded-xl border border-stone-200 shadow-sm">
              <span class="text-3xl text-[#8B0000] block mb-3">🌹</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Rondas y Serenatas</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Especialistas en sorprender a novias, aniversarios y serenatas nocturnas en balcones del casco histórico.</p>
            </div>
            <div class="p-6 bg-white rounded-xl border border-stone-200 shadow-sm">
              <span class="text-3xl text-[#8B0000] block mb-3">🏆</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Certámenes Nacionales</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Galardonados con primeros premios a la Mejor Tuna, Mejor Pasacalles y Pandereta en certámenes de Derecho de España.</p>
            </div>
            <div class="p-6 bg-white rounded-xl border border-stone-200 shadow-sm border-l-4 border-l-[#8B0000]">
              <span class="text-3xl text-[#8B0000] block mb-3">🛍️</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Tienda de Merchandising</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Sudaderas rojas, parches oficiales de beca bordados en oro y discos para apoyar los viajes de la agrupación.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- SECCIÓN QUÉ HACEMOS (NUMERACIÓN EDITORIAL: 01, 02, 03, 04) -->
      <section class="bg-stone-50 border-y border-stone-200 py-16 lg:py-24">
        <div class="max-w-6xl mx-auto px-4">
          <div class="text-center max-w-2xl mx-auto mb-16">
            <span class="badge-editorial text-[#8B0000]">QUÉ HACEMOS</span>
            <h2 class="text-3xl sm:text-4xl font-serif-tuna text-stone-900 mt-2">
              Música para cada celebración
            </h2>
            <div class="w-12 h-1 bg-[#D4AF37] mx-auto my-4"></div>
            <p class="text-sm text-stone-600">Adaptamos nuestra cuadrilla e indumentaria según el tipo de celebración o evento cultural.</p>
          </div>

          <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- 01 Actos universitarios -->
            <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm hover:border-[#8B0000] transition group">
              <span class="font-serif-tuna font-bold text-3xl text-[#8B0000] block mb-2 opacity-80 group-hover:opacity-100">01</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Actos universitarios</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Graduaciones, homenajes, recepciones y actos solemnes de la Facultad de Derecho y la comunidad universitaria.</p>
            </div>

            <!-- 02 Celebraciones privadas -->
            <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm hover:border-[#8B0000] transition group">
              <span class="font-serif-tuna font-bold text-3xl text-[#8B0000] block mb-2 opacity-80 group-hover:opacity-100">02</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Celebraciones</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Bodas, serenatas, cenas de empresa, aniversarios y encuentros familiares dentro y fuera de Almería.</p>
            </div>

            <!-- 03 Viajes y certámenes -->
            <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm hover:border-[#8B0000] transition group">
              <span class="font-serif-tuna font-bold text-3xl text-[#8B0000] block mb-2 opacity-80 group-hover:opacity-100">03</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Viajes y certámenes</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Festivales por España y el extranjero, encuentros de hermandad con tunas de Portugal, Francia e Iberoamérica.</p>
            </div>

            <!-- 04 Ensayos abiertos -->
            <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm hover:border-[#8B0000] transition group">
              <span class="font-serif-tuna font-bold text-3xl text-[#8B0000] block mb-2 opacity-80 group-hover:opacity-100">04</span>
              <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-2">Ensayos abiertos</h3>
              <p class="text-xs text-stone-600 leading-relaxed">Durante el curso en la Facultad de Derecho (martes y jueves a las 19:30 h). Clases de instrumentos gratuitas para nuevos novatos.</p>
            </div>
          </div>

          <div class="mt-12 text-center">
            <button onclick="showVisitanteSection('visitante-contratacion')" class="px-8 py-3.5 bg-[#8B0000] hover:bg-[#670000] text-amber-200 font-bold rounded-lg text-xs uppercase tracking-wider shadow-lg transition border border-[#D4AF37]">
              Solicitar Presupuesto para tu Evento
            </button>
          </div>
        </div>
      </section>

      <!-- SECCIÓN DESTACADA: TIENDA OFICIAL DE MERCHANDISING (PREVIA EN PORTADA) -->
      <section class="max-w-6xl mx-auto px-4 py-16">
        <div class="bg-white rounded-2xl border-2 border-stone-200 p-8 shadow-md">
          <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-6 border-b border-stone-200">
            <div>
              <span class="badge-editorial text-[#8B0000]">TIENDA OFICIAL</span>
              <h2 class="text-2xl sm:text-3xl font-serif-tuna text-stone-900 mt-1">Merchandising y Recuerdos de la Tuna</h2>
              <p class="text-xs text-stone-500 mt-1">Apoya los proyectos de la Tuna adquiriendo artículos oficiales con envío a domicilio.</p>
            </div>
            <button onclick="showVisitanteSection('visitante-tienda')" class="px-5 py-2.5 bg-[#8B0000] hover:bg-[#670000] text-white font-bold rounded-lg text-xs uppercase tracking-wider transition">
              Ver Catálogo Completo (4 Artículos) →
            </button>
          </div>

          <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mt-6">
            <div class="p-4 bg-stone-50 rounded-xl border border-stone-200 text-center">
              <span class="text-5xl block mb-2">👕</span>
              <h3 class="font-bold text-stone-900 text-sm">Sudadera Roja Bordada</h3>
              <p class="text-xs text-stone-500">Escudo UAL y lema oficial</p>
              <div class="text-[#8B0000] font-black text-base mt-2">28,00 €</div>
              <button onclick="addToCart('Sudadera Roja Bordada', 28.00)" class="mt-3 w-full py-1.5 bg-[#8B0000] text-white rounded text-xs font-bold">Añadir a la Cesta</button>
            </div>

            <div class="p-4 bg-stone-50 rounded-xl border border-stone-200 text-center">
              <span class="text-5xl block mb-2">💿</span>
              <h3 class="font-bold text-stone-900 text-sm">CD "25 Años de Ronda"</h3>
              <p class="text-xs text-stone-500">16 temas remasterizados</p>
              <div class="text-[#8B0000] font-black text-base mt-2">12,00 €</div>
              <button onclick="addToCart('CD 25 Años de Ronda', 12.00)" class="mt-3 w-full py-1.5 bg-[#8B0000] text-white rounded text-xs font-bold">Añadir a la Cesta</button>
            </div>

            <div class="p-4 bg-stone-50 rounded-xl border border-stone-200 text-center">
              <span class="text-5xl block mb-2">🎖️</span>
              <h3 class="font-bold text-stone-900 text-sm">Parche Beca en Oro</h3>
              <p class="text-xs text-stone-500">Hilo dorado oficial para capa</p>
              <div class="text-[#8B0000] font-black text-base mt-2">6,50 €</div>
              <button onclick="addToCart('Parche Beca en Oro', 6.50)" class="mt-3 w-full py-1.5 bg-[#8B0000] text-white rounded text-xs font-bold">Añadir a la Cesta</button>
            </div>

            <div class="p-4 bg-stone-50 rounded-xl border border-stone-200 text-center">
              <span class="text-5xl block mb-2">📖</span>
              <h3 class="font-bold text-stone-900 text-sm">Cancionero Ilustrado</h3>
              <p class="text-xs text-stone-500">Letras y acordes tradicionales</p>
              <div class="text-[#8B0000] font-black text-base mt-2">9,00 €</div>
              <button onclick="addToCart('Cancionero Ilustrado', 9.00)" class="mt-3 w-full py-1.5 bg-[#8B0000] text-white rounded text-xs font-bold">Añadir a la Cesta</button>
            </div>
          </div>
        </div>
      </section>

    </div>


    <!-- SECCIÓN 1: CONOCE LA TUNA (HISTORIA Y MIEMBROS) -->
    <div id="visitante-conoce" class="visitante-subview hidden max-w-6xl mx-auto px-4 py-16">
      <div class="mb-10 text-center">
        <span class="badge-editorial text-[#8B0000]">NODO 1</span>
        <h2 class="text-4xl font-serif-tuna text-stone-900 mt-1">Conoce la Tuna de Derecho</h2>
        <div class="w-12 h-1 bg-[#D4AF37] mx-auto my-3"></div>
        <p class="text-stone-600 text-sm">Historia, fundación, trajes y cuadrilla de la Universidad de Almería</p>
      </div>

      <!-- 1.1 Historia estilo cronología Salamanca -->
      <div class="bg-white rounded-2xl border border-stone-200 p-8 shadow-sm mb-12">
        <div class="flex items-center gap-2 mb-6">
          <span class="px-2.5 py-0.5 rounded bg-red-100 text-[#8B0000] font-bold text-xs">Nodo 1.1</span>
          <h3 class="font-serif-tuna font-bold text-2xl text-stone-900">De los primeros sopistas almerienses a hoy</h3>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
          <div class="p-5 rounded-xl bg-stone-50 border border-stone-200">
            <div class="font-serif-tuna font-bold text-2xl text-[#8B0000]">1995</div>
            <div class="font-bold text-stone-900 text-sm mt-1">Fundación en la UAL</div>
            <p class="text-xs text-stone-600 mt-2 leading-relaxed">Un grupo de estudiantes de la naciente Facultad de Derecho decide fundar la agrupación para portar la beca roja por las calles almerienses.</p>
          </div>

          <div class="p-5 rounded-xl bg-stone-50 border border-stone-200">
            <div class="font-serif-tuna font-bold text-2xl text-[#8B0000]">2005 - 2015</div>
            <div class="font-bold text-stone-900 text-sm mt-1">Consolidación y Giras</div>
            <p class="text-xs text-stone-600 mt-2 leading-relaxed">Participación continua en el Circuito Nacional de Tunas de Derecho de España, cosechando premios de Pasacalles y Pandereta.</p>
          </div>

          <div class="p-5 rounded-xl bg-stone-50 border border-stone-200">
            <div class="font-serif-tuna font-bold text-2xl text-[#8B0000]">Presente</div>
            <div class="font-bold text-stone-900 text-sm mt-1">Tradición Viva</div>
            <p class="text-xs text-stone-600 mt-2 leading-relaxed">Activa participación en la Feria de Almería, serenatas nupciales, certámenes ibéricos y formación continua de nuevos estudiantes.</p>
          </div>
        </div>
      </div>

      <!-- 1.2 Miembros de la Tuna -->
      <div class="bg-white rounded-2xl border border-stone-200 p-8 shadow-sm">
        <div class="flex items-center gap-2 mb-6">
          <span class="px-2.5 py-0.5 rounded bg-red-100 text-[#8B0000] font-bold text-xs">Nodo 1.2</span>
          <h3 class="font-serif-tuna font-bold text-2xl text-stone-900">Miembros y Cuadrilla Actual</h3>
        </div>

        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="p-4 rounded-xl border border-stone-200 text-center bg-stone-50">
            <div class="w-16 h-16 rounded-full bg-[#8B0000] text-amber-200 flex items-center justify-center font-bold text-xl mx-auto mb-2 border-2 border-[#D4AF37]">JT</div>
            <div class="font-bold text-stone-900 text-sm">Javier "Jurisconsulto"</div>
            <div class="text-xs text-[#8B0000] font-semibold">Tuno Mayor · Bandurria</div>
            <div class="text-[11px] text-stone-500 mt-1">Tel: 600 123 456</div>
          </div>

          <div class="p-4 rounded-xl border border-stone-200 text-center bg-stone-50">
            <div class="w-16 h-16 rounded-full bg-[#8B0000] text-amber-200 flex items-center justify-center font-bold text-xl mx-auto mb-2 border-2 border-[#D4AF37]">MG</div>
            <div class="font-bold text-stone-900 text-sm">Marcos "El Notario"</div>
            <div class="text-xs text-[#8B0000] font-semibold">Contador · Guitarra</div>
            <div class="text-[11px] text-stone-500 mt-1">Tel: 612 345 678</div>
          </div>

          <div class="p-4 rounded-xl border border-stone-200 text-center bg-stone-50">
            <div class="w-16 h-16 rounded-full bg-[#8B0000] text-amber-200 flex items-center justify-center font-bold text-xl mx-auto mb-2 border-2 border-[#D4AF37]">AP</div>
            <div class="font-bold text-stone-900 text-sm">Antonio "El Fiscal"</div>
            <div class="text-xs text-[#8B0000] font-semibold">Solista · Laúd</div>
            <div class="text-[11px] text-stone-500 mt-1">Voz Principal</div>
          </div>

          <div class="p-4 rounded-xl border border-stone-200 text-center bg-stone-50">
            <div class="w-16 h-16 rounded-full bg-[#8B0000] text-amber-200 flex items-center justify-center font-bold text-xl mx-auto mb-2 border-2 border-[#D4AF37]">CL</div>
            <div class="font-bold text-stone-900 text-sm">Carlos "El Pasante"</div>
            <div class="text-xs text-amber-700 font-semibold">Novato · Pandereta</div>
            <div class="text-[11px] text-stone-500 mt-1">Acrobacias</div>
          </div>
        </div>
      </div>
    </div>


    <!-- SECCIÓN 2: CONTRATACIÓN (FORMULARIO 2.1 Y 2.1.1 + CONTACTO) -->
    <div id="visitante-contratacion" class="visitante-subview hidden max-w-6xl mx-auto px-4 py-16">
      <div class="mb-10 text-center">
        <span class="badge-editorial text-[#8B0000]">NODO 2</span>
        <h2 class="text-4xl font-serif-tuna text-stone-900 mt-1">Contratación de Actuaciones</h2>
        <div class="w-12 h-1 bg-[#D4AF37] mx-auto my-3"></div>
        <p class="text-stone-600 text-sm">Haz que la Tuna forme parte de tu celebración. Te responderemos con disponibilidad y presupuesto.</p>
      </div>

      <div class="grid lg:grid-cols-12 gap-8">
        <!-- Tarjeta de Contacto Directo estilo Salamanca -->
        <div class="lg:col-span-5 bg-[#670000] text-white rounded-2xl p-8 border-2 border-[#D4AF37] shadow-xl flex flex-col justify-between">
          <div>
            <span class="badge-editorial text-amber-300">CONTACTO INMEDIATO</span>
            <h3 class="text-2xl font-serif-tuna text-stone-100 mt-2 mb-4">¿Tienes una fecha próxima?</h3>
            <p class="text-stone-200 text-xs leading-relaxed mb-6">
              Para bodas, serenatas de medianoche o aniversarios, llámanos directamente por teléfono a cualquiera de nuestros responsables para asegurar la disponibilidad de la cuadrilla:
            </p>

            <div class="space-y-4 mb-6">
              <div class="p-3 bg-black/40 rounded-xl border border-amber-500/40">
                <div class="text-[10px] text-amber-300 font-bold uppercase">Javier (Tuno Mayor):</div>
                <a href="tel:+34600123456" class="text-xl font-serif-tuna font-bold text-white hover:text-amber-300 transition block">+34 600 123 456</a>
              </div>
              <div class="p-3 bg-black/40 rounded-xl border border-amber-500/40">
                <div class="text-[10px] text-amber-300 font-bold uppercase">Marcos (Relaciones Públicas):</div>
                <a href="tel:+34612345678" class="text-xl font-serif-tuna font-bold text-white hover:text-amber-300 transition block">+34 612 345 678</a>
              </div>
            </div>

            <a href="https://wa.me/34600123456" target="_blank" class="w-full py-3 bg-green-700 hover:bg-green-600 text-white font-bold rounded-lg text-xs uppercase tracking-wider text-center flex items-center justify-center gap-2 transition shadow">
              <span>💬</span> Escribir por WhatsApp Directo
            </a>
          </div>

          <div class="pt-6 mt-6 border-t border-red-900 text-xs text-stone-300">
            ✉️ tuna.derecho.almeria@gmail.com
          </div>
        </div>

        <!-- Formulario Oficial 2.1.1 -->
        <div class="lg:col-span-7 bg-white rounded-2xl border border-stone-200 p-8 shadow-sm">
          <div class="flex items-center justify-between mb-6 pb-4 border-b border-stone-100">
            <div>
              <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 2.1.1</span>
              <h3 class="font-serif-tuna font-bold text-xl text-stone-900">Formulario de Petición de Actuación</h3>
            </div>
            <span class="text-xs text-stone-400">Respuesta en 24h</span>
          </div>

          <form onsubmit="alert('¡Solicitud enviada! Nos pondremos en contacto contigo.'); return false;" class="space-y-4 text-xs">
            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Nombre y Apellidos *</label>
                <input type="text" required placeholder="Tu nombre" class="w-full px-3 py-2.5 rounded-lg border border-stone-300 focus:border-[#8B0000] outline-none">
              </div>
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Teléfono Móvil *</label>
                <input type="tel" required placeholder="600 000 000" class="w-full px-3 py-2.5 rounded-lg border border-stone-300 focus:border-[#8B0000] outline-none">
              </div>
            </div>

            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Correo Electrónico *</label>
                <input type="email" required placeholder="tu@email.com" class="w-full px-3 py-2.5 rounded-lg border border-stone-300 focus:border-[#8B0000] outline-none">
              </div>
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Tipo de Actuación *</label>
                <select class="w-full px-3 py-2.5 rounded-lg border border-stone-300 focus:border-[#8B0000] outline-none bg-white">
                  <option>Boda (Salida de iglesia / Banquete)</option>
                  <option>Serenata a la novia / balcón</option>
                  <option>Acto universitario / Graduación</option>
                  <option>Cena de empresa / Congreso</option>
                  <option>Cumpleaños o Jubilación</option>
                  <option>Otro evento</option>
                </select>
              </div>
            </div>

            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Fecha del Evento *</label>
                <input type="date" required class="w-full px-3 py-2.5 rounded-lg border border-stone-300 focus:border-[#8B0000] outline-none">
              </div>
              <div>
                <label class="block font-bold text-stone-700 uppercase mb-1">Municipio / Lugar *</label>
                <input type="text" required placeholder="Almería, Roquetas, El Ejido..." class="w-full px-3 py-2.5 rounded-lg border border-stone-300 focus:border-[#8B0000] outline-none">
              </div>
            </div>

            <div>
              <label class="block font-bold text-stone-700 uppercase mb-1">Comentarios o canciones especiales solicitadas</label>
              <textarea rows="3" placeholder="Detalles de sorpresa, horas previstas o temas del repertorio..." class="w-full px-3 py-2.5 rounded-lg border border-stone-300 focus:border-[#8B0000] outline-none"></textarea>
            </div>

            <div class="pt-2 flex items-center justify-between">
              <span class="text-stone-500">¿Ya eres cliente? <button type="button" onclick="switchProfile('cliente')" class="text-[#8B0000] font-bold underline">Entra a tu cuenta</button></span>
              <button type="submit" class="px-6 py-3 bg-[#8B0000] hover:bg-[#670000] text-amber-200 font-bold rounded-lg uppercase tracking-wider text-xs shadow transition border border-[#D4AF37]">
                Enviar Solicitud
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>


    <!-- SECCIÓN 3: MULTIMEDIA (VÍDEOS, FOTOS Y CERTÁMENES) -->
    <div id="visitante-multimedia" class="visitante-subview hidden max-w-6xl mx-auto px-4 py-16">
      <div class="mb-10 text-center">
        <span class="badge-editorial text-[#8B0000]">NODO 3</span>
        <h2 class="text-4xl font-serif-tuna text-stone-900 mt-1">Vídeos, Fotos y Certámenes</h2>
        <div class="w-12 h-1 bg-[#D4AF37] mx-auto my-3"></div>
        <p class="text-stone-600 text-sm">Momentos en escenario, certámenes y actuaciones en directo</p>
      </div>

      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Vídeo 1 -->
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-44 bg-stone-900 flex flex-col items-center justify-center text-white relative group cursor-pointer">
            <span class="text-4xl text-red-500 group-hover:scale-125 transition">▶️</span>
            <span class="text-xs text-stone-400 mt-2 font-mono">03:45 · YouTube</span>
          </div>
          <div class="p-4">
            <span class="text-[10px] font-bold text-[#8B0000] uppercase">Vídeo 3.1.1</span>
            <h4 class="font-serif-tuna font-bold text-stone-900 text-base">Clavelitos en el Balcón</h4>
            <p class="text-xs text-stone-500 mt-1">Feria de Almería</p>
          </div>
        </div>

        <!-- Vídeo 2 -->
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm">
          <div class="h-44 bg-stone-900 flex flex-col items-center justify-center text-white relative group cursor-pointer">
            <span class="text-4xl text-red-500 group-hover:scale-125 transition">▶️</span>
            <span class="text-xs text-stone-400 mt-2 font-mono">04:15 · YouTube</span>
          </div>
          <div class="p-4">
            <span class="text-[10px] font-bold text-[#8B0000] uppercase">Vídeo 3.1.1</span>
            <h4 class="font-serif-tuna font-bold text-stone-900 text-base">Ronda Nocturna de Capas</h4>
            <p class="text-xs text-stone-500 mt-1">Casco Histórico</p>
          </div>
        </div>

        <!-- Certamen 3.2 -->
        <div class="bg-white rounded-xl border-2 border-amber-400 overflow-hidden shadow-sm bg-gradient-to-b from-amber-50/50 to-white">
          <div class="h-44 bg-[#670000] flex flex-col items-center justify-center text-amber-300 p-4 text-center">
            <span class="text-4xl mb-1">🏆</span>
            <span class="font-serif-tuna font-bold text-lg">1º Premio Mejor Tuna</span>
            <span class="text-xs text-stone-300">Certamen Nacional de Derecho</span>
          </div>
          <div class="p-4">
            <span class="text-[10px] font-bold text-[#8B0000] uppercase">Certamen 3.2</span>
            <h4 class="font-serif-tuna font-bold text-stone-900 text-base">XXX Certamen de Tunas de Derecho</h4>
            <p class="text-xs text-stone-500 mt-1">Primer premio de pasacalles y pandereta</p>
          </div>
        </div>
      </div>
    </div>


    <!-- ========================================================================= -->
    <!-- SECCIÓN 4: TIENDA OFICIAL (CATÁLOGO, CESTA Y PASARELA) ⭐ -->
    <!-- ========================================================================= -->
    <div id="visitante-tienda" class="visitante-subview hidden max-w-6xl mx-auto px-4 py-16">
      <div class="mb-8 flex flex-col md:flex-row items-start md:items-end justify-between gap-4">
        <div>
          <span class="badge-editorial text-[#8B0000]">NODO 4</span>
          <h2 class="text-4xl font-serif-tuna text-stone-900 mt-1">Tienda Oficial de la Tuna</h2>
          <div class="w-12 h-1 bg-[#D4AF37] my-3"></div>
          <p class="text-stone-600 text-sm">Productos oficiales: ropa, grabaciones musicales y accesorios con envío directo.</p>
        </div>
        <button onclick="showVisitanteSection('visitante-cesta')" class="px-5 py-2.5 rounded-lg bg-[#8B0000] hover:bg-[#670000] text-amber-200 font-bold text-xs uppercase tracking-wider shadow-md transition flex items-center gap-2 border border-[#D4AF37]">
          <span>🛒</span> Ver Cesta (<span id="store-badge-cart">2</span> artículos)
        </button>
      </div>

      <!-- Filtros según Wireframe Catalogo.html -->
      <div class="bg-white rounded-xl border border-stone-200 p-4 mb-8 shadow-sm flex flex-wrap items-center gap-4 text-xs">
        <div class="flex-1 min-w-[180px]">
          <label class="block font-bold text-stone-600 uppercase mb-1">Categoría</label>
          <select class="w-full px-3 py-2 border border-stone-300 rounded-lg bg-white outline-none">
            <option>Todas las categorías</option>
            <option>Ropa y Sudaderas</option>
            <option>Música y Grabaciones</option>
            <option>Accesorios y Parches</option>
          </select>
        </div>
        <div class="flex-1 min-w-[180px]">
          <label class="block font-bold text-stone-600 uppercase mb-1">Precio</label>
          <select class="w-full px-3 py-2 border border-stone-300 rounded-lg bg-white outline-none">
            <option>Cualquier precio</option>
            <option>Menos de 15 €</option>
            <option>15 € a 30 €</option>
          </select>
        </div>
        <div class="self-end">
          <button class="px-5 py-2 bg-stone-900 text-white rounded-lg font-bold hover:bg-stone-800 transition">
            Aplicar Filtros
          </button>
        </div>
      </div>

      <!-- Catálogo 4.1 -->
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Producto 1 -->
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
          <div>
            <div class="h-44 bg-stone-100 flex items-center justify-center text-5xl">👕</div>
            <div class="p-4">
              <span class="text-[10px] text-[#8B0000] font-bold uppercase">Ropa Oficial</span>
              <h4 class="font-serif-tuna font-bold text-stone-900 text-base mt-1">Sudadera Roja Tuna de Derecho</h4>
              <p class="text-xs text-stone-500 mt-1">Escudo bordado de la Facultad de Derecho.</p>
              <div class="mt-3 text-lg font-serif-tuna font-bold text-[#8B0000]">28,00 €</div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('Sudadera Roja', 28.00)" class="w-full py-2 bg-[#8B0000] hover:bg-[#670000] text-white font-bold rounded text-xs uppercase tracking-wider transition">
              Añadir a la Cesta
            </button>
          </div>
        </div>

        <!-- Producto 2 -->
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
          <div>
            <div class="h-44 bg-stone-100 flex items-center justify-center text-5xl">💿</div>
            <div class="p-4">
              <span class="text-[10px] text-[#8B0000] font-bold uppercase">Música</span>
              <h4 class="font-serif-tuna font-bold text-stone-900 text-base mt-1">CD "25 Años de Ronda"</h4>
              <p class="text-xs text-stone-500 mt-1">Grabación oficial con 16 temas.</p>
              <div class="mt-3 text-lg font-serif-tuna font-bold text-[#8B0000]">12,00 €</div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('CD 25 Años de Ronda', 12.00)" class="w-full py-2 bg-[#8B0000] hover:bg-[#670000] text-white font-bold rounded text-xs uppercase tracking-wider transition">
              Añadir a la Cesta
            </button>
          </div>
        </div>

        <!-- Producto 3 -->
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
          <div>
            <div class="h-44 bg-stone-100 flex items-center justify-center text-5xl">🎖️</div>
            <div class="p-4">
              <span class="text-[10px] text-[#8B0000] font-bold uppercase">Accesorios</span>
              <h4 class="font-serif-tuna font-bold text-stone-900 text-base mt-1">Parche Beca Derecho</h4>
              <p class="text-xs text-stone-500 mt-1">Bordado en hilo de oro para capa.</p>
              <div class="mt-3 text-lg font-serif-tuna font-bold text-[#8B0000]">6,50 €</div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('Parche Beca', 6.50)" class="w-full py-2 bg-[#8B0000] hover:bg-[#670000] text-white font-bold rounded text-xs uppercase tracking-wider transition">
              Añadir a la Cesta
            </button>
          </div>
        </div>

        <!-- Producto 4 -->
        <div class="bg-white rounded-xl border border-stone-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
          <div>
            <div class="h-44 bg-stone-100 flex items-center justify-center text-5xl">📖</div>
            <div class="p-4">
              <span class="text-[10px] text-[#8B0000] font-bold uppercase">Libros</span>
              <h4 class="font-serif-tuna font-bold text-stone-900 text-base mt-1">Cancionero Ilustrado</h4>
              <p class="text-xs text-stone-500 mt-1">Letras completas y acordes.</p>
              <div class="mt-3 text-lg font-serif-tuna font-bold text-[#8B0000]">9,00 €</div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('Cancionero Ilustrado', 9.00)" class="w-full py-2 bg-[#8B0000] hover:bg-[#670000] text-white font-bold rounded text-xs uppercase tracking-wider transition">
              Añadir a la Cesta
            </button>
          </div>
        </div>
      </div>
    </div>


    <!-- SECCIÓN 4.2: CESTA Y TRAMITACIÓN DE PEDIDO -->
    <div id="visitante-cesta" class="visitante-subview hidden max-w-6xl mx-auto px-4 py-16">
      <div class="mb-8">
        <span class="badge-editorial text-[#8B0000]">NODO 4.2</span>
        <h2 class="text-4xl font-serif-tuna text-stone-900 mt-1">Cesta y Tramitación de Pedido</h2>
        <div class="w-12 h-1 bg-[#D4AF37] my-3"></div>
      </div>

      <!-- Diagrama de Flujo según Árbol -->
      <div class="p-3 bg-stone-100 rounded-lg border border-stone-200 mb-6 text-xs flex flex-wrap items-center gap-2">
        <span class="font-bold text-stone-500 uppercase">Flujo del Árbol:</span>
        <span class="px-2.5 py-0.5 rounded bg-[#8B0000] text-white font-bold">4.2 Cesta</span>
        <span>➔</span>
        <span class="px-2.5 py-0.5 rounded bg-white text-stone-700">4.2.1 Inicio Sesión</span>
        <span>➔</span>
        <span class="px-2.5 py-0.5 rounded bg-white text-stone-700">4.2.1.1 Dirección Envío</span>
        <span>➔</span>
        <span class="px-2.5 py-0.5 rounded bg-white text-stone-700">4.2.1.1.1 Pago</span>
        <span>➔</span>
        <span class="px-2.5 py-0.5 rounded bg-white text-stone-700">4.2.1.1.1.1 Recibo</span>
      </div>

      <div class="grid lg:grid-cols-12 gap-8">
        <div class="lg:col-span-7 bg-white rounded-xl border border-stone-200 p-6 shadow-sm">
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-4 pb-2 border-b border-stone-100">Artículos en la Cesta</h3>
          <div class="divide-y divide-stone-100 text-xs">
            <div class="py-3 flex justify-between items-center">
              <div>
                <div class="font-bold text-stone-900">Sudadera Roja Tuna de Derecho (Talla L)</div>
                <div class="text-stone-500">Cantidad: 1</div>
              </div>
              <div class="font-bold text-[#8B0000]">28,00 €</div>
            </div>
            <div class="py-3 flex justify-between items-center">
              <div>
                <div class="font-bold text-stone-900">Parche Beca Derecho Bordado Oro</div>
                <div class="text-stone-500">Cantidad: 1</div>
              </div>
              <div class="font-bold text-[#8B0000]">6,50 €</div>
            </div>
          </div>
          <div class="pt-4 mt-2 border-t border-stone-200 flex justify-between text-sm font-bold text-stone-900">
            <span>Total Artículos:</span>
            <span class="text-lg text-[#8B0000]">34,50 €</span>
          </div>
        </div>

        <div class="lg:col-span-5 bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
          <h3 class="font-serif-tuna font-bold text-lg text-stone-900 mb-4 pb-2 border-b border-stone-100">Datos de Envío y Pago</h3>
          <div class="space-y-3 mb-4">
            <input type="text" placeholder="Calle, número y piso" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            <div class="grid grid-cols-2 gap-2">
              <input type="text" placeholder="Código Postal" class="px-3 py-2 border border-stone-300 rounded outline-none">
              <input type="text" placeholder="Ciudad (Almería)" class="px-3 py-2 border border-stone-300 rounded outline-none">
            </div>
            <div class="p-2.5 bg-stone-50 rounded border border-stone-200 space-y-1">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="radio" name="pay" checked class="text-[#8B0000]">
                <span class="font-semibold text-stone-800">Tarjeta Bancaria / Bizum</span>
              </label>
            </div>
          </div>
          <button onclick="alert('¡Pago completado! Pedido confirmado con número #PED-2026-904.');" class="w-full py-3 bg-[#8B0000] hover:bg-[#670000] text-amber-200 font-bold rounded uppercase tracking-wider text-xs shadow border border-[#D4AF37]">
            Confirmar y Pagar (34,50 €)
          </button>
        </div>
      </div>
    </div>


    <!-- SECCIÓN 5: CANCIONERO (REPERTORIO Y SPOTIFY) -->
    <div id="visitante-cancionero" class="visitante-subview hidden max-w-6xl mx-auto px-4 py-16">
      <div class="mb-10 text-center">
        <span class="badge-editorial text-[#8B0000]">NODO 5</span>
        <h2 class="text-4xl font-serif-tuna text-stone-900 mt-1">Cancionero y Repertorio de Ronda</h2>
        <div class="w-12 h-1 bg-[#D4AF37] mx-auto my-3"></div>
      </div>

      <div class="grid lg:grid-cols-12 gap-8">
        <div class="lg:col-span-7 bg-white rounded-xl border border-stone-200 p-6 shadow-sm">
          <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 5.1</span>
          <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Letras Tradicionales</h3>
          <div class="space-y-4 text-xs text-stone-700">
            <details class="p-3 bg-stone-50 rounded border border-stone-200" open>
              <summary class="font-bold cursor-pointer text-stone-900">🌹 Clavelitos</summary>
              <p class="mt-2 text-stone-600 font-serif-tuna italic">"Mocita dame el clavel, dame el clavel de tu boca..."</p>
            </details>
            <details class="p-3 bg-stone-50 rounded border border-stone-200">
              <summary class="font-bold cursor-pointer text-stone-900">🎓 Fonseca</summary>
              <p class="mt-2 text-stone-600 font-serif-tuna italic">"Adiós villa de Fonseca, ya me marcho de aquí..."</p>
            </details>
          </div>
        </div>

        <div class="lg:col-span-5 bg-[#141414] text-white rounded-xl p-6 border-2 border-green-500 shadow-md flex flex-col justify-between">
          <div>
            <span class="badge-editorial text-green-400">NODO 5.2</span>
            <h3 class="font-serif-tuna font-bold text-xl text-white mt-1 mb-3">Escúchanos en Spotify</h3>
            <p class="text-xs text-stone-300 mb-4">Pistas oficiales grabadas en estudio por la Tuna de Derecho de Almería.</p>
            <div class="p-3 bg-stone-900 rounded border border-stone-800 text-xs space-y-2">
              <div class="flex justify-between"><span>1. Clavelitos</span><span class="font-mono text-stone-400">03:12</span></div>
              <div class="flex justify-between"><span>2. Serenata Almeriense</span><span class="font-mono text-stone-400">04:05</span></div>
            </div>
          </div>
          <a href="https://spotify.com" target="_blank" class="mt-6 w-full py-2.5 bg-green-500 hover:bg-green-400 text-stone-950 font-bold text-xs uppercase tracking-wider text-center rounded transition">
            Abrir en Spotify Oficial
          </a>
        </div>
      </div>
    </div>


    <!-- SECCIÓN 6: ÚNETE (FORMULARIO Y ENSAYOS) -->
    <div id="visitante-unete" class="visitante-subview hidden max-w-6xl mx-auto px-4 py-16">
      <div class="mb-10 text-center">
        <span class="badge-editorial text-[#8B0000]">NODO 6</span>
        <h2 class="text-4xl font-serif-tuna text-stone-900 mt-1">Únete a la Cuadrilla</h2>
        <div class="w-12 h-1 bg-[#D4AF37] mx-auto my-3"></div>
      </div>

      <div class="grid lg:grid-cols-2 gap-8">
        <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm">
          <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 6.1</span>
          <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Formulario para Nuevos Miembros</h3>
          <p class="text-xs text-stone-600 mb-4">Te enseñamos gratis desde cero a tocar bandurria, laúd, guitarra o pandereta.</p>
          <form onsubmit="alert('¡Gracias! El Tuno Mayor te citará para el próximo ensayo.'); return false;" class="space-y-3 text-xs">
            <input type="text" placeholder="Nombre completo" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            <input type="tel" placeholder="Teléfono" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            <input type="text" placeholder="Grado que estudias en la UAL" required class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
            <button type="submit" class="w-full py-2.5 bg-[#8B0000] text-amber-200 font-bold rounded uppercase tracking-wider">Enviar Solicitud</button>
          </form>
        </div>

        <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm flex flex-col justify-between">
          <div>
            <span class="text-xs font-bold text-stone-500 uppercase">Nodo 6.2</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Local de Ensayo</h3>
            <div class="space-y-3 text-xs text-stone-600">
              <div class="p-3 bg-stone-50 rounded border border-stone-200">
                <strong>📍 Facultad de Derecho (Planta Baja):</strong><br>
                Universidad de Almería, Ctra. Sacramento s/n.
              </div>
              <div class="p-3 bg-stone-50 rounded border border-stone-200">
                <strong>🕒 Horarios de Ensayo:</strong><br>
                Martes y Jueves a las 19:30 h.
              </div>
            </div>
          </div>
          <div class="mt-6 p-3 bg-[#670000] text-white rounded text-center text-xs">
            Teléfono de Ensayo: <strong>+34 600 123 456</strong>
          </div>
        </div>
      </div>
    </div>


    <!-- SECCIÓN 7: INICIO DE SESIÓN Y REGISTRO -->
    <div id="visitante-acceso" class="visitante-subview hidden max-w-md mx-auto px-4 py-16">
      <div class="bg-white rounded-2xl border border-stone-200 p-8 shadow-xl">
        <div class="text-center mb-6">
          <div class="w-12 h-12 rounded-full bg-[#8B0000] text-amber-300 font-serif-tuna font-bold flex items-center justify-center text-lg mx-auto mb-2 border-2 border-[#D4AF37]">TD</div>
          <span class="badge-editorial text-[#8B0000]">NODO 7</span>
          <h3 class="font-serif-tuna font-bold text-2xl text-stone-900">Acceso a tu Cuenta</h3>
          <p class="text-xs text-stone-500 mt-1">Inicia sesión como cliente o administrador</p>
        </div>

        <form onsubmit="switchProfile('cliente'); return false;" class="space-y-3 text-xs">
          <div>
            <label class="block font-bold text-stone-700 uppercase mb-1">Correo Electrónico</label>
            <input type="email" value="cliente@almeria.es" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <div>
            <div class="flex justify-between items-center mb-1">
              <label class="block font-bold text-stone-700 uppercase">Contraseña</label>
              <button type="button" onclick="alert('Nodo 7.1: Enlace de recuperación enviado.');" class="text-xs text-[#8B0000] hover:underline">7.1 Recuperar</button>
            </div>
            <input type="password" value="********" class="w-full px-3 py-2 border border-stone-300 rounded outline-none">
          </div>
          <button type="submit" class="w-full py-2.5 bg-[#8B0000] hover:bg-[#670000] text-white font-bold rounded uppercase tracking-wider">
            Iniciar Sesión
          </button>
        </form>

        <div class="mt-6 pt-4 border-t border-stone-100 text-center text-xs text-stone-600">
          Nodo 7.2: ¿No tienes cuenta? <button onclick="alert('Nodo 7.2: Formulario de Registro abierto.');" class="text-[#8B0000] font-bold underline">Regístrate</button>
        </div>
      </div>
    </div>

  </div>


  <!-- ========================================================================= -->
  <!-- 2. PERFIL: CLIENTE (ÁREA PRIVADA SEGÚN WIREFRAMES) -->
  <!-- ========================================================================= -->
  <div id="profile-cliente" class="flex-1 flex flex-col hidden bg-stone-100">
    
    <!-- Barra Superior Cliente -->
    <header class="bg-white border-b border-stone-200 py-3 px-6 sticky top-12 z-30 shadow-sm flex items-center justify-between text-xs">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded bg-blue-800 text-white font-bold flex items-center justify-center">👤</span>
        <div>
          <span class="text-blue-800 font-bold uppercase tracking-wider text-[10px]">ÁREA DE CLIENTE REGISTRADO</span>
          <div class="font-bold text-stone-900 text-sm">José Manuel Martínez</div>
        </div>
      </div>
      <button onclick="switchProfile('visitante')" class="px-3 py-1.5 border border-stone-300 rounded font-semibold text-stone-700 hover:bg-stone-50">
        Cerrar Sesión
      </button>
    </header>

    <div class="max-w-6xl mx-auto w-full px-4 py-8 flex-1 grid lg:grid-cols-4 gap-8">
      <!-- Menú Cliente -->
      <aside class="space-y-2 text-xs">
        <div class="bg-white rounded-xl border border-stone-200 p-3 shadow-sm space-y-1">
          <div class="text-[10px] font-bold text-stone-400 uppercase px-3 py-1">Navegación Cliente</div>
          <button onclick="showClientSection('cliente-dashboard')" id="btn-c-dash" class="client-sidebar-btn active w-full text-left px-3 py-2 rounded-lg font-bold flex items-center gap-2">
            <span>🏠</span> 0. Inicio Cliente
          </button>
          <button onclick="showClientSection('cliente-contratos')" id="btn-c-contratos" class="client-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>📜</span> 1. Historial de Contratos
          </button>
          <button onclick="showClientSection('cliente-pedidos')" id="btn-c-pedidos" class="client-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>🛍️</span> 2. Historial de Pedidos
          </button>
          <button onclick="showClientSection('cliente-cuenta')" id="btn-c-cuenta" class="client-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>⚙️</span> 3. Gestionar Cuenta
          </button>
        </div>

        <div class="bg-[#670000] text-white rounded-xl p-4 text-xs border border-amber-400">
          <span class="text-amber-300 font-bold block mb-1 uppercase text-[10px]">¿Dudas con tu contrato?</span>
          <p class="text-stone-200 text-[11px]">Habla con el Tuno Mayor para coordinar horarios:</p>
          <a href="tel:+34600123456" class="mt-2 block py-1.5 bg-red-900 text-center font-bold text-white rounded">📞 +34 600 123 456</a>
        </div>
      </aside>

      <!-- Panel Cliente -->
      <main class="lg:col-span-3">
        <!-- 0. Inicio Cliente -->
        <div id="cliente-dashboard" class="client-subview space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm">
            <h2 class="font-serif-tuna font-bold text-2xl text-stone-900">Hola, José Manuel</h2>
            <p class="text-xs text-stone-500 mt-1">Accede a tus contratos de actuaciones y pedidos de la tienda.</p>
            <div class="grid sm:grid-cols-2 gap-4 mt-6 text-xs">
              <div class="p-4 rounded-lg bg-amber-50 border border-amber-200">
                <span class="font-bold text-amber-800 uppercase">Contratos</span>
                <div class="text-xl font-bold text-stone-900 mt-1">1 Próximo Evento</div>
                <div class="text-stone-600 mt-0.5">Boda en Roquetas · 18/07/2026</div>
              </div>
              <div class="p-4 rounded-lg bg-blue-50 border border-blue-200">
                <span class="font-bold text-blue-800 uppercase">Pedidos Tienda</span>
                <div class="text-xl font-bold text-stone-900 mt-1">1 Pedido Activo</div>
                <div class="text-stone-600 mt-0.5">#PED-894 · Enviado</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1. Contratos -->
        <div id="cliente-contratos" class="client-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 1</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Historial de Contratos</h3>
            <table class="w-full text-left text-xs">
              <thead class="bg-stone-50 text-stone-500 uppercase border-b border-stone-200">
                <tr>
                  <th class="py-2.5 px-3">Nº Contrato</th>
                  <th class="py-2.5 px-3">Evento</th>
                  <th class="py-2.5 px-3">Fecha</th>
                  <th class="py-2.5 px-3">Estado</th>
                  <th class="py-2.5 px-3 text-right">Detalle (1.1)</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                <tr>
                  <td class="py-2.5 px-3 font-bold">#CTR-042</td>
                  <td class="py-2.5 px-3">Boda Civil & Banquete</td>
                  <td class="py-2.5 px-3">18/07/2026</td>
                  <td class="py-2.5 px-3"><span class="px-2 py-0.5 bg-green-100 text-green-800 font-bold rounded">Confirmado</span></td>
                  <td class="py-2.5 px-3 text-right"><button onclick="alert('Nodo 1.1: Detalle del contrato #CTR-042: 12 Tunos, 450 €.');" class="text-[#8B0000] font-bold">Ver</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 2. Pedidos -->
        <div id="cliente-pedidos" class="client-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 2</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Pedidos de Merchandising</h3>
            <div class="p-4 bg-stone-50 rounded-lg border border-stone-200 text-xs">
              <div class="flex justify-between font-bold text-stone-900 pb-2 border-b border-stone-200">
                <span>Pedido #PED-894 (34,50 €)</span>
                <span class="text-blue-800">Enviado</span>
              </div>
              <div class="py-2 text-stone-600 flex justify-between items-center">
                <span>1x Sudadera Roja (L), 1x Parche Beca</span>
                <div class="space-x-3">
                  <button onclick="alert('Nodo 2.1.1: Editar datos');" class="text-blue-700 font-bold">2.1.1 Editar</button>
                  <button onclick="alert('Nodo 2.1.2: Tramitar devolución');" class="text-red-700 font-bold">2.1.2 Devolución</button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Cuenta -->
        <div id="cliente-cuenta" class="client-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 3</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Gestionar Cuenta</h3>
            <div class="grid sm:grid-cols-2 gap-6">
              <div>
                <h4 class="font-bold text-stone-800 uppercase mb-2">3.1 Modificar Datos</h4>
                <input type="text" value="José Manuel Martínez" class="w-full px-3 py-2 border border-stone-300 rounded mb-2">
                <input type="tel" value="612 345 678" class="w-full px-3 py-2 border border-stone-300 rounded mb-2">
                <button onclick="alert('Nodo 3.1: Datos guardados');" class="px-3 py-1.5 bg-stone-900 text-white rounded font-bold">Guardar</button>
              </div>
              <div>
                <h4 class="font-bold text-stone-800 uppercase mb-2">3.2 Cambiar Contraseña</h4>
                <input type="password" value="********" class="w-full px-3 py-2 border border-stone-300 rounded mb-2">
                <button onclick="alert('Nodo 3.2: Contraseña cambiada');" class="px-3 py-1.5 bg-[#8B0000] text-white rounded font-bold">Actualizar Clave</button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- 3. PERFIL: ADMINISTRADOR (PANEL DE GESTIÓN Y ESTADÍSTICAS) -->
  <!-- ========================================================================= -->
  <div id="profile-admin" class="flex-1 flex flex-col hidden bg-stone-100">
    
    <!-- Header Admin -->
    <header class="bg-[#141414] border-b border-red-800 py-3 px-6 sticky top-12 z-30 shadow-md flex items-center justify-between text-white text-xs">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded bg-[#8B0000] text-amber-300 font-serif-tuna font-bold flex items-center justify-center border border-amber-400">ADM</span>
        <div>
          <span class="text-amber-400 font-bold uppercase tracking-wider text-[10px]">PANEL DE ADMINISTRACIÓN</span>
          <div class="font-bold text-white text-sm">SuperAdmin: Tuno Mayor Javier</div>
        </div>
      </div>
      <button onclick="switchProfile('visitante')" class="px-3 py-1.5 border border-stone-700 rounded font-semibold text-stone-300 hover:bg-stone-800">
        Salir al Portal
      </button>
    </header>

    <div class="max-w-6xl mx-auto w-full px-4 py-8 flex-1 grid lg:grid-cols-4 gap-8">
      <!-- Menú Admin (0 a 7 según Árbol) -->
      <aside class="space-y-2 text-xs">
        <div class="bg-white rounded-xl border border-stone-200 p-3 shadow-sm space-y-1">
          <div class="text-[10px] font-bold text-stone-400 uppercase px-3 py-1">Módulos Admin</div>
          <button onclick="showAdminSection('admin-dashboard')" id="btn-adm-dash" class="admin-sidebar-btn active w-full text-left px-3 py-2 rounded-lg font-bold flex items-center gap-2">
            <span>📊</span> 0. Estadísticas
          </button>
          <button onclick="showAdminSection('admin-contratos')" id="btn-adm-contratos" class="admin-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>📜</span> 1. Gestionar Contratos
          </button>
          <button onclick="showAdminSection('admin-clientes')" id="btn-adm-clientes" class="admin-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>👥</span> 2. Cartera de Clientes
          </button>
          <button onclick="showAdminSection('admin-pedidos')" id="btn-adm-pedidos" class="admin-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>📦</span> 3. Pedidos Tienda
          </button>
          <button onclick="showAdminSection('admin-productos')" id="btn-adm-productos" class="admin-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>🛍️</span> 4. Productos Tienda
          </button>
          <button onclick="showAdminSection('admin-miembros')" id="btn-adm-miembros" class="admin-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>🎸</span> 5. Lista de Miembros
          </button>
          <button onclick="showAdminSection('admin-cuenta')" id="btn-adm-cuenta" class="admin-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>🔑</span> 6. Gestionar Cuenta
          </button>
          <button onclick="showAdminSection('admin-certamenes')" id="btn-adm-certamenes" class="admin-sidebar-btn w-full text-left px-3 py-2 rounded-lg font-semibold text-stone-700 hover:bg-stone-50 flex items-center gap-2">
            <span>🏆</span> 7. Gestionar Certámenes
          </button>
        </div>
      </aside>

      <!-- Panel Central Admin -->
      <main class="lg:col-span-3">
        <!-- 0. Estadísticas -->
        <div id="admin-dashboard" class="admin-subview space-y-6">
          <div class="grid sm:grid-cols-4 gap-4 text-xs">
            <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
              <span class="font-bold text-stone-500 uppercase">Contratos Pendientes</span>
              <div class="text-2xl font-black text-[#8B0000] mt-1">4</div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
              <span class="font-bold text-stone-500 uppercase">Pedidos Tienda</span>
              <div class="text-2xl font-black text-stone-900 mt-1">7</div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
              <span class="font-bold text-stone-500 uppercase">Ingresos Mes</span>
              <div class="text-2xl font-black text-emerald-700 mt-1">1.840 €</div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-stone-200 shadow-sm">
              <span class="font-bold text-stone-500 uppercase">Clientes</span>
              <div class="text-2xl font-black text-blue-800 mt-1">12</div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-xl border border-stone-200 shadow-sm text-xs">
            <h4 class="font-bold text-stone-900 mb-3">Ventas e Ingresos (Últimos 12 meses)</h4>
            <div class="flex items-end gap-2 h-36 border-b border-stone-300 pb-2">
              <div class="flex-1 bg-red-200 h-[40%] rounded-t"></div>
              <div class="flex-1 bg-red-200 h-[55%] rounded-t"></div>
              <div class="flex-1 bg-red-200 h-[35%] rounded-t"></div>
              <div class="flex-1 bg-red-300 h-[70%] rounded-t"></div>
              <div class="flex-1 bg-red-400 h-[60%] rounded-t"></div>
              <div class="flex-1 bg-red-500 h-[85%] rounded-t"></div>
              <div class="flex-1 bg-red-600 h-[95%] rounded-t"></div>
              <div class="flex-1 bg-red-500 h-[80%] rounded-t"></div>
              <div class="flex-1 bg-red-400 h-[65%] rounded-t"></div>
              <div class="flex-1 bg-red-300 h-[50%] rounded-t"></div>
              <div class="flex-1 bg-red-200 h-[45%] rounded-t"></div>
              <div class="flex-1 bg-red-500 h-[75%] rounded-t"></div>
            </div>
          </div>
        </div>

        <!-- 1. Contratos Admin -->
        <div id="admin-contratos" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 1</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Gestión de Contratos de Actuación</h3>
            <table class="w-full text-left">
              <thead class="bg-stone-50 text-stone-500 uppercase border-b border-stone-200">
                <tr>
                  <th class="py-2 px-3">Nº</th>
                  <th class="py-2 px-3">Cliente</th>
                  <th class="py-2 px-3">Fecha</th>
                  <th class="py-2 px-3">Estado</th>
                  <th class="py-2 px-3 text-right">Detalle (1.1)</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                <tr>
                  <td class="py-2 px-3 font-bold">#CTR-042</td>
                  <td class="py-2 px-3">José Manuel Martínez</td>
                  <td class="py-2 px-3">18/07/2026</td>
                  <td class="py-2 px-3"><span class="px-2 py-0.5 bg-green-100 text-green-800 font-bold rounded">Confirmado</span></td>
                  <td class="py-2 px-3 text-right"><button onclick="alert('Nodo 1.1: Ficha completa del contrato');" class="text-[#8B0000] font-bold">Ver</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 2. Cartera Clientes Admin -->
        <div id="admin-clientes" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 2</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Cartera de Clientes</h3>
            <div class="p-3 bg-stone-50 rounded border border-stone-200 flex justify-between items-center">
              <div>
                <strong>José Manuel Martínez</strong> (cliente@almeria.es)
                <div class="text-stone-500">Nodo 2.1 Ficha de Cliente</div>
              </div>
              <div class="space-x-2">
                <button onclick="alert('Nodo 2.1.1: Ver Contratos del cliente');" class="px-2.5 py-1 bg-stone-900 text-white rounded font-bold">2.1.1 Contratos</button>
                <button onclick="alert('Nodo 2.1.2: Ver Pedidos del cliente');" class="px-2.5 py-1 bg-[#8B0000] text-white rounded font-bold">2.1.2 Pedidos</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Pedidos Tienda Admin -->
        <div id="admin-pedidos" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 3</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Gestión de Pedidos de la Tienda</h3>
            <div class="p-3 bg-stone-50 rounded border border-stone-200 flex justify-between items-center">
              <div>
                <strong>#PED-894</strong> · José Manuel Martínez · 34,50 €
                <div class="text-blue-800 font-semibold">Enviado por Correos</div>
              </div>
              <button onclick="alert('Nodo 3.1: Ver Detalle del Pedido');" class="text-[#8B0000] font-bold">3.1 Ver Detalle</button>
            </div>
          </div>
        </div>

        <!-- 4. Productos Admin -->
        <div id="admin-productos" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <div class="flex justify-between items-center mb-4">
              <div>
                <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 4</span>
                <h3 class="font-serif-tuna font-bold text-xl text-stone-900">Catálogo de Productos</h3>
              </div>
              <button onclick="alert('Nodo 4.1: Añadir nuevo producto');" class="px-3 py-1.5 bg-[#8B0000] text-white font-bold rounded">
                + 4.1 Añadir Producto
              </button>
            </div>
            <div class="divide-y divide-stone-100">
              <div class="py-2.5 flex justify-between items-center">
                <span>Sudadera Roja Tuna Derecho (28,00 €)</span>
                <button onclick="alert('Nodo 4.2: Modificar o eliminar');" class="text-blue-700 font-bold">4.2 Modificar/Eliminar</button>
              </div>
              <div class="py-2.5 flex justify-between items-center">
                <span>CD "25 Años de Ronda" (12,00 €)</span>
                <button onclick="alert('Nodo 4.2: Modificar o eliminar');" class="text-blue-700 font-bold">4.2 Modificar/Eliminar</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 5. Miembros Admin -->
        <div id="admin-miembros" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <div class="flex justify-between items-center mb-4">
              <div>
                <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 5</span>
                <h3 class="font-serif-tuna font-bold text-xl text-stone-900">Plantilla de Miembros</h3>
              </div>
              <button onclick="alert('Nodo 5.2: Añadir nuevo miembro');" class="px-3 py-1.5 bg-[#8B0000] text-white font-bold rounded">
                + 5.2 Añadir Miembro
              </button>
            </div>
            <div class="p-3 bg-stone-50 rounded border border-stone-200 flex justify-between items-center">
              <span>Javier "Jurisconsulto" (Tuno Mayor)</span>
              <button onclick="alert('Nodo 5.1: Modificar/Baja');" class="text-blue-700 font-bold">5.1 Modificar</button>
            </div>
          </div>
        </div>

        <!-- 6. Cuenta Admin -->
        <div id="admin-cuenta" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 6</span>
            <h3 class="font-serif-tuna font-bold text-xl text-stone-900 mb-4">Gestión de Cuenta Admin</h3>
            <div class="space-y-3">
              <div class="p-3 bg-stone-50 rounded border border-stone-200">
                <strong>6.1 Información Personal:</strong> Tuno Mayor Javier
                <button onclick="alert('Nodo 6.1 actualizado');" class="block mt-2 px-3 py-1 bg-stone-900 text-white rounded font-bold">Editar</button>
              </div>
              <div class="p-3 bg-stone-50 rounded border border-stone-200">
                <strong>6.2 Contraseña de Seguridad:</strong>
                <button onclick="alert('Nodo 6.2 contraseña cambiada');" class="block mt-2 px-3 py-1 bg-[#8B0000] text-white rounded font-bold">Cambiar Clave</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 7. Certámenes Admin -->
        <div id="admin-certamenes" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-xl border border-stone-200 p-6 shadow-sm text-xs">
            <div class="flex justify-between items-center mb-4">
              <div>
                <span class="text-xs font-bold text-[#8B0000] uppercase">Nodo 7</span>
                <h3 class="font-serif-tuna font-bold text-xl text-stone-900">Gestión de Certámenes</h3>
              </div>
              <button onclick="alert('Nodo 7.2: Crear nuevo certamen');" class="px-3 py-1.5 bg-[#8B0000] text-white font-bold rounded">
                + 7.2 Crear Certamen
              </button>
            </div>
            <div class="p-3 bg-stone-50 rounded border border-stone-200 flex justify-between items-center">
              <span>Certamen Nacional de Tunas de Derecho</span>
              <button onclick="alert('Nodo 7.1: Editar certamen');" class="text-blue-700 font-bold">7.1 Editar</button>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- FOOTER ESTILO TUNASALAMANCA.COM: SOLEMNE, ELEGANTE Y ULTRA CONTACTABLE -->
  <!-- ========================================================================= -->
  <footer class="bg-[#100404] text-stone-300 border-t-2 border-[#D4AF37] pt-14 pb-8 text-xs">
    <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-12 gap-8 mb-12">
      
      <!-- Columna 1: Marca & Eslogan Salamanca-Style -->
      <div class="md:col-span-4">
        <div class="font-serif-tuna font-black text-xl text-amber-200 tracking-wider">
          TUNA DE LA FACULTAD DE DERECHO
        </div>
        <div class="badge-editorial text-[#D4AF37] text-[9px] mt-1">
          Universidad de Almería · Beca Roja
        </div>
        <p class="text-stone-400 mt-4 leading-relaxed text-xs">
          Tradición estudiantil, música y amistad desde 1995. Recorriendo escenarios, certámenes y calles con la alegría de la capa española.
        </p>
      </div>

      <!-- Columna 2: CONTACTO DIRECTO (ULTRA VISIBLE) -->
      <div class="md:col-span-5 bg-[#250707] p-5 rounded-xl border border-[#D4AF37]/50">
        <span class="badge-editorial text-amber-300 block mb-2">CONTACTO Y ACTUACIONES</span>
        <div class="text-stone-300 text-xs mb-3">Cuéntanos dónde y cuándo será tu evento. Te responderemos con disponibilidad y detalles:</div>
        
        <div class="space-y-2">
          <div class="flex items-center gap-2">
            <span class="text-amber-400 font-bold">Javier (Tuno Mayor):</span>
            <a href="tel:+34600123456" class="font-bold text-white hover:text-amber-300">+34 600 123 456</a>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-amber-400 font-bold">Marcos (R. Públicas):</span>
            <a href="tel:+34612345678" class="font-bold text-white hover:text-amber-300">+34 612 345 678</a>
          </div>
          <div class="flex items-center gap-2 pt-1 border-t border-red-950">
            <span class="text-stone-400">Correo Oficial:</span>
            <a href="mailto:tuna.derecho.almeria@gmail.com" class="text-amber-200 hover:underline">tuna.derecho.almeria@gmail.com</a>
          </div>
        </div>
      </div>

      <!-- Columna 3: REDES SOCIALES -->
      <div class="md:col-span-3">
        <span class="badge-editorial text-amber-300 block mb-3">SÍGUENOS EN REDES</span>
        <ul class="space-y-2 text-stone-300">
          <li><a href="https://instagram.com" target="_blank" class="hover:text-amber-300">📷 Instagram: @tunaderechoalmeria</a></li>
          <li><a href="https://tiktok.com" target="_blank" class="hover:text-amber-300">🎵 TikTok: @tunaderechoual</a></li>
          <li><a href="https://facebook.com" target="_blank" class="hover:text-amber-300">👥 Facebook: /TunaDerechoAlmeria</a></li>
          <li><a href="https://youtube.com" target="_blank" class="hover:text-amber-300">▶️ YouTube: @TunaDerechoUAL</a></li>
          <li><a href="https://spotify.com" target="_blank" class="hover:text-amber-300">🟢 Spotify: Tuna Derecho Almería</a></li>
        </ul>
      </div>

    </div>

    <!-- Copyright -->
    <div class="max-w-6xl mx-auto px-4 pt-6 border-t border-stone-800 flex flex-col sm:flex-row items-center justify-between gap-2 text-[11px] text-stone-500">
      <div>© 2026 TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA. TODOS LOS DERECHOS RESERVADOS.</div>
      <div class="flex gap-4">
        <span>Aviso Legal</span>
        <span>Privacidad</span>
        <span>Cookies</span>
      </div>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- BOTÓN FLOTANTE PERMANENTE DE WHATSAPP -->
  <!-- ========================================================================= -->
  <a href="https://wa.me/34600123456" target="_blank" class="fixed bottom-6 right-6 z-50 flex items-center gap-2 px-4 py-3 rounded-full bg-green-700 hover:bg-green-600 text-white font-bold text-xs shadow-2xl transition hover:scale-105 border-2 border-white pulse-contact" title="WhatsApp Inmediato">
    <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347m-5.421 7.403"/></svg>
    <span class="hidden sm:inline">WhatsApp Tuna: +34 600 123 456</span>
  </a>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT DE NAVEGACIÓN Y CARRITO -->
  <!-- ========================================================================= -->
  <script>
    // 1. Alternar entre los 3 perfiles principales
    function switchProfile(profile) {
      document.getElementById('profile-visitante').classList.add('hidden');
      document.getElementById('profile-cliente').classList.add('hidden');
      document.getElementById('profile-admin').classList.add('hidden');

      document.getElementById('tab-visitante').classList.remove('active');
      document.getElementById('tab-cliente').classList.remove('active');
      document.getElementById('tab-admin').classList.remove('active');

      if (profile === 'visitante') {
        document.getElementById('profile-visitante').classList.remove('hidden');
        document.getElementById('tab-visitante').classList.add('active');
      } else if (profile === 'cliente') {
        document.getElementById('profile-cliente').classList.remove('hidden');
        document.getElementById('tab-cliente').classList.add('active');
      } else if (profile === 'admin') {
        document.getElementById('profile-admin').classList.remove('hidden');
        document.getElementById('tab-admin').classList.add('active');
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // 2. Navegación subsecciones de Visitante
    function showVisitanteSection(sectionId) {
      document.querySelectorAll('.visitante-subview').forEach(el => el.classList.add('hidden'));
      const target = document.getElementById(sectionId);
      if (target) {
        target.classList.remove('hidden');
        window.scrollTo({ top: 100, behavior: 'smooth' });
      }
    }

    // 3. Navegación subsecciones de Cliente
    function showClientSection(sectionId) {
      document.querySelectorAll('.client-subview').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.client-sidebar-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(sectionId);
      if (target) target.classList.remove('hidden');

      if (sectionId === 'cliente-dashboard') document.getElementById('btn-c-dash').classList.add('active');
      if (sectionId === 'cliente-contratos') document.getElementById('btn-c-contratos').classList.add('active');
      if (sectionId === 'cliente-pedidos') document.getElementById('btn-c-pedidos').classList.add('active');
      if (sectionId === 'cliente-cuenta') document.getElementById('btn-c-cuenta').classList.add('active');
    }

    // 4. Navegación subsecciones de Administrador
    function showAdminSection(sectionId) {
      document.querySelectorAll('.admin-subview').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.admin-sidebar-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(sectionId);
      if (target) target.classList.remove('hidden');

      if (sectionId === 'admin-dashboard') document.getElementById('btn-adm-dash').classList.add('active');
      if (sectionId === 'admin-contratos') document.getElementById('btn-adm-contratos').classList.add('active');
      if (sectionId === 'admin-clientes') document.getElementById('btn-adm-clientes').classList.add('active');
      if (sectionId === 'admin-pedidos') document.getElementById('btn-adm-pedidos').classList.add('active');
      if (sectionId === 'admin-productos') document.getElementById('btn-adm-productos').classList.add('active');
      if (sectionId === 'admin-miembros') document.getElementById('btn-adm-miembros').classList.add('active');
      if (sectionId === 'admin-cuenta') document.getElementById('btn-adm-cuenta').classList.add('active');
      if (sectionId === 'admin-certamenes') document.getElementById('btn-adm-certamenes').classList.add('active');
    }

    // 5. Carrito de Compras de la Tienda
    let cartTotalItems = 2;
    function addToCart(productName, price) {
      cartTotalItems++;
      document.getElementById('cart-counter').textContent = cartTotalItems;
      const badge = document.getElementById('store-badge-cart');
      if (badge) badge.textContent = cartTotalItems;
      alert('¡Artículo añadido a la cesta! ' + productName + ' (' + price.toFixed(2) + ' €). Total en cesta: ' + cartTotalItems);
    }
  </script>
</body>
</html>
"""

# Guardar en las dos rutas necesarias
paths = [
    r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\mockup-tuna-derecho-almeria.html",
    r"C:\Users\joses\.gemini\antigravity\brain\36451285-1c1b-4cee-abfe-e4f0f4417009\mockup-tuna-derecho-almeria.html"
]

for p in paths:
    with open(p, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Guardado exitosamente en: {p}")

print("Mockup con diseño inspirado en tunasalamanca.com generado al 100%.")

