# -*- coding: utf-8 -*-
import os
import shutil

print("Generando mockup integral...")

HTML = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería · Mockup Interactivo Oficial</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {
      --rojo-tuna: #B91C1C;
      --rojo-oscuro: #881337;
      --rojo-claro: #DC2626;
      --dorado: #D4A843;
      --dorado-claro: #F6E05E;
      --dorado-oscuro: #B7791F;
      --crema: #FFFBF5;
      --negro: #18181B;
    }
    body {
      background-color: #F8FAFC;
      color: #1E293B;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }
    .hero-pattern {
      background-color: #991B1B;
      background-image: radial-gradient(rgba(220, 38, 38, 0.4) 1px, transparent 1px), radial-gradient(rgba(127, 29, 29, 0.6) 1px, #7F1D1D 1px);
      background-size: 32px 32px;
      background-position: 0 0, 16px 16px;
    }
    .pulse-call {
      animation: pulse-ring 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    @keyframes pulse-ring {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.06); }
    }
    .tab-profile.active {
      background-color: #FFFFFF;
      color: #991B1B;
      font-weight: 700;
      border-bottom: 3px solid #D4A843;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .subnav-link.active {
      color: #B91C1C;
      font-weight: 700;
      border-bottom: 2px solid #B91C1C;
    }
    .admin-menu-item.active {
      background-color: #991B1B;
      color: #FFFFFF;
      font-weight: 600;
    }
    .client-menu-item.active {
      background-color: #991B1B;
      color: #FFFFFF;
      font-weight: 600;
    }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-red-200 selection:text-red-900">

  <!-- ========================================================================= -->
  <!-- 0. SWITCHER DE PERFILES FIJO EN LA PARTE SUPERIOR (VISITANTE / CLIENTE / ADMIN) -->
  <!-- ========================================================================= -->
  <div class="sticky top-0 z-50 bg-slate-900 border-b border-amber-500/40 text-white shadow-xl">
    <div class="max-w-7xl mx-auto px-4 py-2 flex flex-col md:flex-row items-center justify-between gap-2">
      <div class="flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-red-700 text-amber-300 font-serif font-black text-xs border border-amber-400">TD</span>
        <div>
          <span class="text-xs uppercase tracking-widest text-amber-400 font-bold block">SELECTOR DE PERFIL DE USUARIO</span>
          <span class="text-[13px] text-slate-300">Tuna de la Facultad de Derecho de Almería</span>
        </div>
      </div>
      
      <!-- Botones de los 3 Perfiles -->
      <div class="flex items-center bg-slate-800 p-1 rounded-xl border border-slate-700">
        <button onclick="switchProfile('visitante')" id="tab-btn-visitante" class="tab-profile active px-4 py-1.5 rounded-lg text-xs md:text-sm font-medium transition-all flex items-center gap-2">
          <span>🌐</span> Visitante <span class="text-[11px] opacity-75">(Público)</span>
        </button>
        <button onclick="switchProfile('cliente')" id="tab-btn-cliente" class="tab-profile px-4 py-1.5 rounded-lg text-xs md:text-sm font-medium text-slate-300 hover:text-white transition-all flex items-center gap-2">
          <span>👤</span> Cliente <span class="text-[11px] opacity-75">(Registrado)</span>
        </button>
        <button onclick="switchProfile('admin')" id="tab-btn-admin" class="tab-profile px-4 py-1.5 rounded-lg text-xs md:text-sm font-medium text-slate-300 hover:text-white transition-all flex items-center gap-2">
          <span>⚙️</span> Administrador <span class="text-[11px] opacity-75">(Gestión)</span>
        </button>
      </div>

      <!-- Acceso Rápido Teléfono / WhatsApp -->
      <div class="hidden lg:flex items-center gap-3 text-xs">
        <a href="tel:+34600123456" class="flex items-center gap-1.5 px-3 py-1 bg-red-700 hover:bg-red-600 text-white rounded-full font-bold shadow pulse-call border border-amber-400">
          <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          +34 600 123 456
        </a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- BARRA DE CONTACTO CORPORATIVA ULTRA-VISIBLE (GLOBAL) -->
  <!-- ========================================================================= -->
  <div class="bg-red-900 text-white border-b-2 border-amber-500 text-xs py-2 px-4 shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex flex-wrap items-center gap-4 md:gap-6">
        <a href="tel:+34600123456" class="flex items-center gap-2 font-black text-sm text-amber-300 hover:text-amber-200 transition-colors">
          <span class="inline-flex p-1 bg-red-800 rounded-full">📞</span>
          TELÉFONO DIRECTO: +34 600 123 456
        </a>
        <a href="mailto:tuna.derecho.almeria@gmail.com" class="flex items-center gap-1.5 text-slate-200 hover:text-amber-300 transition-colors">
          <span>✉️</span> tuna.derecho.almeria@gmail.com
        </a>
        <span class="hidden xl:inline text-amber-200/60">|</span>
        <span class="hidden xl:inline text-slate-300">📍 Universidad de Almería (Edificio Derecho)</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="font-bold text-amber-300 uppercase tracking-wider text-[11px] hidden sm:inline">¡Redes Sociales Oficiales!:</span>
        <div class="flex items-center gap-3">
          <a href="https://instagram.com" target="_blank" class="p-1 rounded bg-red-800 hover:bg-pink-600 transition-all hover:scale-110" title="Instagram: @tunaderechoalmeria">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </a>
          <a href="https://tiktok.com" target="_blank" class="p-1 rounded bg-red-800 hover:bg-black transition-all hover:scale-110" title="TikTok: @tunaderechoual">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1v-3.5a6.37 6.37 0 00-.79-.05A6.34 6.34 0 003.15 15.2a6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.34-6.34V8.87a8.28 8.28 0 004.76 1.49V6.89a4.85 4.85 0 01-1-.2z"/></svg>
          </a>
          <a href="https://facebook.com" target="_blank" class="p-1 rounded bg-red-800 hover:bg-blue-600 transition-all hover:scale-110" title="Facebook: /TunaDerechoAlmeria">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          </a>
          <a href="https://youtube.com" target="_blank" class="p-1 rounded bg-red-800 hover:bg-red-600 transition-all hover:scale-110" title="YouTube: @TunaDerechoUAL">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </a>
          <a href="https://spotify.com" target="_blank" class="p-1 rounded bg-red-800 hover:bg-green-600 transition-all hover:scale-110" title="Spotify: Tuna Derecho Almería">
            <svg class="w-4 h-4 fill-white" viewBox="0 0 24 24"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.494 17.306c-.215.352-.676.463-1.028.248-2.812-1.718-6.353-2.107-10.523-1.154-.403.092-.807-.16-.899-.562-.092-.403.16-.807.562-.899 4.568-1.044 8.49-.607 11.64 1.339.352.215.463.676.248 1.028zm1.465-3.26c-.27.44-.846.578-1.287.307-3.218-1.977-8.125-2.55-11.93-1.394-.498.151-1.025-.133-1.176-.631-.151-.498.133-1.025.631-1.176 4.354-1.321 9.775-.681 13.455 1.581.441.27.578.846.307 1.287v.026zm.126-3.41c-3.858-2.292-10.228-2.503-13.908-1.385-.591.18-1.22-.162-1.4-.753-.18-.591.162-1.22.753-1.4 4.24-1.288 11.267-1.044 15.688 1.579.531.315.706 1.002.391 1.533-.315.531-1.002.706-1.533.391z"/></svg>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 1. PERFIL: VISITANTE (PÁGINA COMPLETA CON TIENDA Y TODAS LAS SUBSECCIONES) -->
  <!-- ========================================================================= -->
  <div id="profile-visitante" class="flex-1 flex flex-col">

    <!-- Navegación Pública del Visitante (según Wireframe de Visitante) -->
    <header class="bg-white border-b border-slate-200 sticky top-12 z-40 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between gap-4">
        <a href="#visitante-inicio" onclick="showVisitanteSection('visitante-inicio')" class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-full bg-gradient-to-br from-red-700 to-red-950 flex items-center justify-center text-amber-300 font-serif font-black text-xl border-2 border-amber-400 shadow">
            TD
          </div>
          <div>
            <div class="font-serif font-black text-lg md:text-xl text-red-900 leading-tight">TUNA DE DERECHO</div>
            <div class="text-xs font-semibold text-amber-600 tracking-wider">UNIVERSIDAD DE ALMERÍA · DESDE 1995</div>
          </div>
        </a>

        <!-- Enlaces directos según Árbol 1 a 7 -->
        <nav class="hidden lg:flex items-center gap-5 text-sm font-medium text-slate-700">
          <button onclick="showVisitanteSection('visitante-inicio')" class="hover:text-red-700 transition">Inicio</button>
          <button onclick="showVisitanteSection('visitante-conoce')" class="hover:text-red-700 transition">1. Conoce la Tuna</button>
          <button onclick="showVisitanteSection('visitante-contratacion')" class="hover:text-red-700 transition">2. Contratación</button>
          <button onclick="showVisitanteSection('visitante-multimedia')" class="hover:text-red-700 transition">3. Multimedia</button>
          <button onclick="showVisitanteSection('visitante-tienda')" class="px-2.5 py-1 bg-red-50 text-red-700 rounded-md font-bold hover:bg-red-100 border border-red-200 transition flex items-center gap-1.5">
            <span>🛍️</span> 4. Tienda
          </button>
          <button onclick="showVisitanteSection('visitante-cancionero')" class="hover:text-red-700 transition">5. Cancionero</button>
          <button onclick="showVisitanteSection('visitante-unete')" class="hover:text-red-700 transition">6. Únete</button>
        </nav>

        <div class="flex items-center gap-2.5">
          <!-- Cesta Tienda -->
          <button onclick="showVisitanteSection('visitante-cesta')" class="px-3 py-1.5 rounded-lg border border-red-300 bg-red-50 text-red-800 font-semibold text-xs flex items-center gap-1.5 hover:bg-red-100 transition shadow-sm">
            <span>🛒</span> Cesta <span id="cart-counter" class="bg-red-700 text-white rounded-full px-1.5 py-0.2 text-[10px]">2</span>
          </button>

          <!-- Login/Acceso -->
          <button onclick="showVisitanteSection('visitante-acceso')" class="px-3 py-1.5 rounded-lg border border-slate-300 text-slate-700 font-semibold text-xs hover:border-red-600 hover:text-red-700 transition">
            7. Iniciar sesión
          </button>

          <!-- Botón Contratar destacado -->
          <button onclick="showVisitanteSection('visitante-contratacion')" class="px-4 py-2 rounded-lg bg-red-800 hover:bg-red-700 text-white font-bold text-xs shadow-md transition border border-amber-400">
            Contratar
          </button>
        </div>
      </div>
    </header>

    <!-- SUB-BARRA DE NAVEGACIÓN RÁPIDA DE VISITANTE (Para saltar entre las vistas del árbol) -->
    <div class="bg-slate-100 border-b border-slate-200 py-1.5 px-4 text-xs overflow-x-auto whitespace-nowrap">
      <div class="max-w-7xl mx-auto flex items-center gap-2">
        <span class="font-bold text-slate-500 uppercase tracking-wider text-[11px]">Vistas del Visitante:</span>
        <button onclick="showVisitanteSection('visitante-inicio')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">0. Inicio</button>
        <button onclick="showVisitanteSection('visitante-conoce')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">1. Conoce (Historia/Miembros)</button>
        <button onclick="showVisitanteSection('visitante-contratacion')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">2. Contratación</button>
        <button onclick="showVisitanteSection('visitante-multimedia')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">3. Multimedia (Vídeos/Fotos/Certámenes)</button>
        <button onclick="showVisitanteSection('visitante-tienda')" class="px-2.5 py-1 rounded bg-red-700 text-white font-bold border border-red-800">4. TIENDA OFICIAL</button>
        <button onclick="showVisitanteSection('visitante-cesta')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">4.2 Cesta y Checkout</button>
        <button onclick="showVisitanteSection('visitante-cancionero')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">5. Cancionero & Spotify</button>
        <button onclick="showVisitanteSection('visitante-unete')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">6. Únete (Formulario/Ensayo)</button>
        <button onclick="showVisitanteSection('visitante-acceso')" class="px-2.5 py-1 rounded bg-white hover:bg-red-100 text-slate-700 font-medium border border-slate-300">7. Acceso / Registro</button>
      </div>
    </div>

    <!-- ================= CONTENIDOS VISITANTE ================= -->

    <!-- SECCIÓN 0: INICIO VISITANTE (HERO + RESUMEN DE LOS 6 BLOQUES DEL WIREFRAME) -->
    <div id="visitante-inicio" class="visitante-subview">
      <!-- HERO PRINCIPAL -->
      <section class="hero-pattern text-white py-16 lg:py-24 relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
          <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-black/40 border border-amber-400/50 text-amber-300 text-xs font-bold uppercase tracking-widest mb-6">
            <span>✨</span> MÁS DE 25 AÑOS DE HISTORIA Y MÚSICA EN ALMERÍA
          </div>
          <h1 class="text-4xl md:text-6xl lg:text-7xl font-serif font-black mb-6 tracking-tight drop-shadow-md">
            Tuna de la Facultad de Derecho<br>
            <span class="text-amber-300">Universidad de Almería</span>
          </h1>
          <p class="text-lg md:text-xl text-slate-100 max-w-3xl mx-auto mb-8 font-light leading-relaxed">
            Alegría, tradición, pasodobles y serenatas. Amenizamos bodas, eventos de empresa, aniversarios y festivales por toda España.
          </p>

          <!-- DATOS DE CONTACTO DESTACADOS EN HERO -->
          <div class="inline-flex flex-wrap items-center justify-center gap-4 p-4 rounded-2xl bg-black/50 border-2 border-amber-400 backdrop-blur-md shadow-2xl mb-8">
            <div class="flex items-center gap-3">
              <span class="w-10 h-10 rounded-full bg-red-700 flex items-center justify-center text-amber-300 text-xl font-bold">📞</span>
              <div class="text-left">
                <div class="text-[11px] uppercase tracking-wider text-amber-300 font-bold">CONTRATACIONES & INFORMACIÓN</div>
                <a href="tel:+34600123456" class="text-xl md:text-2xl font-black text-white hover:text-amber-300 transition">+34 600 123 456</a>
              </div>
            </div>
            <div class="h-8 w-px bg-slate-600 hidden md:block"></div>
            <div class="flex items-center gap-3">
              <span class="w-10 h-10 rounded-full bg-green-600 flex items-center justify-center text-white text-xl font-bold">💬</span>
              <div class="text-left">
                <div class="text-[11px] uppercase tracking-wider text-green-300 font-bold">WHATSAPP INMEDIATO</div>
                <a href="https://wa.me/34600123456" class="text-base md:text-lg font-bold text-white hover:text-green-300 transition">Enviar Mensaje</a>
              </div>
            </div>
          </div>

          <div class="flex flex-wrap items-center justify-center gap-4">
            <button onclick="showVisitanteSection('visitante-contratacion')" class="px-8 py-3.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-base shadow-lg transition">
              Pedir Presupuesto / Contratar
            </button>
            <button onclick="showVisitanteSection('visitante-tienda')" class="px-8 py-3.5 rounded-xl bg-red-800 hover:bg-red-700 border-2 border-amber-400 text-white font-bold text-base shadow-lg transition flex items-center gap-2">
              <span>🛍️</span> Ver Tienda Oficial
            </button>
          </div>
        </div>
      </section>

      <!-- LOS 6 BLOQUES DEL WIREFRAME VISITANTE (GRID 3 COLUMNAS) -->
      <section class="max-w-7xl mx-auto px-4 py-16">
        <div class="text-center mb-12">
          <span class="text-xs uppercase tracking-widest text-red-800 font-bold">Árbol de navegación</span>
          <h2 class="text-3xl font-serif font-black text-slate-900 mt-1">Explora Nuestra Web Oficial</h2>
          <div class="w-16 h-1 bg-amber-500 mx-auto mt-3"></div>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- 1 Conoce la tuna -->
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition flex flex-col justify-between border-t-4 border-t-red-700">
            <div>
              <div class="h-32 rounded-xl bg-red-100 flex items-center justify-center text-red-800 font-bold mb-4">
                <span class="text-4xl">🏛️</span>
              </div>
              <h3 class="text-xl font-bold text-slate-900 mb-2">1. Conoce la Tuna</h3>
              <p class="text-slate-600 text-sm mb-4">Descubre nuestra historia desde 1995, trajes, becas rojas y la plantilla actual de tunos y novatos.</p>
            </div>
            <button onclick="showVisitanteSection('visitante-conoce')" class="text-red-700 font-bold text-sm hover:text-red-900 flex items-center gap-1">
              Ver Historia y Miembros →
            </button>
          </div>

          <!-- 2 Contratación -->
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition flex flex-col justify-between border-t-4 border-t-amber-500">
            <div>
              <div class="h-32 rounded-xl bg-amber-100 flex items-center justify-center text-amber-800 font-bold mb-4">
                <span class="text-4xl">📜</span>
              </div>
              <h3 class="text-xl font-bold text-slate-900 mb-2">2. Contratación</h3>
              <p class="text-slate-600 text-sm mb-4">Pide presupuesto personalizado para bodas, serenatas, cenas de gala, ferias y congresos.</p>
            </div>
            <button onclick="showVisitanteSection('visitante-contratacion')" class="text-amber-700 font-bold text-sm hover:text-amber-900 flex items-center gap-1">
              Solicitar Contratación →
            </button>
          </div>

          <!-- 3 Multimedia -->
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition flex flex-col justify-between border-t-4 border-t-red-700">
            <div>
              <div class="h-32 rounded-xl bg-red-100 flex items-center justify-center text-red-800 font-bold mb-4">
                <span class="text-4xl">🎬</span>
              </div>
              <h3 class="text-xl font-bold text-slate-900 mb-2">3. Contenido Multimedia</h3>
              <p class="text-slate-600 text-sm mb-4">Galería de vídeos, actuaciones en vivo, fotografías oficiales y premios en certámenes.</p>
            </div>
            <button onclick="showVisitanteSection('visitante-multimedia')" class="text-red-700 font-bold text-sm hover:text-red-900 flex items-center gap-1">
              Ver Vídeos, Fotos y Certámenes →
            </button>
          </div>

          <!-- 4 Tienda -->
          <div class="bg-white rounded-2xl border-2 border-red-600 p-6 shadow-md hover:shadow-lg transition flex flex-col justify-between relative bg-gradient-to-b from-red-50/50 to-white">
            <span class="absolute top-3 right-3 bg-red-700 text-amber-300 text-[10px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider">Destacado</span>
            <div>
              <div class="h-32 rounded-xl bg-red-200/80 flex items-center justify-center text-red-900 font-bold mb-4">
                <span class="text-4xl">🛍️</span>
              </div>
              <h3 class="text-xl font-bold text-red-950 mb-2">4. Tienda Oficial</h3>
              <p class="text-slate-600 text-sm mb-4">Merchandising oficial: camisetas, sudaderas, pines, parches de beca, discos y cancioneros.</p>
            </div>
            <button onclick="showVisitanteSection('visitante-tienda')" class="px-4 py-2 bg-red-800 text-white rounded-lg font-bold text-sm hover:bg-red-700 text-center">
              Entrar al Catálogo Oficial →
            </button>
          </div>

          <!-- 5 Cancionero -->
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition flex flex-col justify-between border-t-4 border-t-amber-500">
            <div>
              <div class="h-32 rounded-xl bg-amber-100 flex items-center justify-center text-amber-800 font-bold mb-4">
                <span class="text-4xl">🎵</span>
              </div>
              <h3 class="text-xl font-bold text-slate-900 mb-2">5. Cancionero</h3>
              <p class="text-slate-600 text-sm mb-4">Letras completas de nuestro repertorio tradicional y enlace a nuestras pistas en Spotify.</p>
            </div>
            <button onclick="showVisitanteSection('visitante-cancionero')" class="text-amber-700 font-bold text-sm hover:text-amber-900 flex items-center gap-1">
              Ver Repertorio y Spotify →
            </button>
          </div>

          <!-- 6 Únete a nosotros -->
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition flex flex-col justify-between border-t-4 border-t-red-700">
            <div>
              <div class="h-32 rounded-xl bg-red-100 flex items-center justify-center text-red-800 font-bold mb-4">
                <span class="text-4xl">🤝</span>
              </div>
              <h3 class="text-xl font-bold text-slate-900 mb-2">6. Únete a Nosotros</h3>
              <p class="text-slate-600 text-sm mb-4">¿Estudias en la UAL y quieres aprender guitarra, laúd o bandurria? Te enseñamos desde cero.</p>
            </div>
            <button onclick="showVisitanteSection('visitante-unete')" class="text-red-700 font-bold text-sm hover:text-red-900 flex items-center gap-1">
              Formulario de Ingreso y Ensayos →
            </button>
          </div>
        </div>
      </section>
    </div>

    <!-- SECCIÓN 1: CONOCE LA TUNA (HISTORIA Y MIEMBROS) -->
    <div id="visitante-conoce" class="visitante-subview hidden max-w-7xl mx-auto px-4 py-12">
      <div class="mb-8">
        <span class="text-xs uppercase tracking-widest text-red-800 font-bold">1. Conoce la Tuna</span>
        <h2 class="text-3xl md:text-4xl font-serif font-black text-slate-900 mt-1">Historia y Hermanos de Capa</h2>
        <div class="w-16 h-1 bg-amber-500 mt-3"></div>
      </div>

      <!-- Subsección 1.1 Historia -->
      <div class="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm mb-12">
        <div class="flex items-center gap-3 mb-6">
          <span class="px-3 py-1 bg-red-100 text-red-800 font-bold text-xs rounded-full">Nodo 1.1</span>
          <h3 class="text-2xl font-serif font-bold text-red-950">Nuestra Historia (Desde 1995)</h3>
        </div>
        <div class="grid md:grid-cols-3 gap-8 items-center">
          <div class="md:col-span-2 text-slate-700 space-y-4 leading-relaxed">
            <p>
              La <strong>Tuna de la Facultad de Derecho de la Universidad de Almería</strong> fue fundada en el curso académico 1995 por un entusiasta grupo de estudiantes de leyes con la ilusión de mantener viva la secular tradición universitaria española.
            </p>
            <p>
              Portamos con orgullo el <strong>color rojo</strong> en nuestras becas, color representativo de la Facultad de Derecho, decoradas con cintas de los certámenes y viajes realizados por toda la península ibérica, Europa e Hispanoamérica.
            </p>
            <div class="p-4 bg-amber-50 border-l-4 border-amber-500 rounded-r-xl text-amber-900 text-sm">
              🏆 <strong>Premios destacados:</strong> Primer premio de Tuna Más Simpática en el Certamen Nacional de Derecho, Mejor Pasacalles en Granada y Mejor Pandereta en el Certamen de Murcia.
            </div>
          </div>
          <div class="h-64 rounded-xl bg-gradient-to-br from-red-900 to-red-950 flex flex-col items-center justify-center text-amber-300 p-6 text-center border-2 border-amber-400">
            <span class="text-5xl mb-2">📜</span>
            <span class="font-serif font-bold text-lg">Beca Roja de Derecho</span>
            <span class="text-xs text-slate-300 mt-1">Símbolo de hermandad, justicia y tradición tunantesca</span>
          </div>
        </div>
      </div>

      <!-- Subsección 1.2 Miembros -->
      <div class="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
        <div class="flex items-center gap-3 mb-6">
          <span class="px-3 py-1 bg-red-100 text-red-800 font-bold text-xs rounded-full">Nodo 1.2</span>
          <h3 class="text-2xl font-serif font-bold text-red-950">Miembros Actuales de la Cuadrilla</h3>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="p-4 rounded-xl border border-slate-200 text-center hover:border-red-600 transition">
            <div class="w-20 h-20 mx-auto rounded-full bg-red-800 text-amber-300 flex items-center justify-center font-bold text-2xl mb-3">JT</div>
            <div class="font-bold text-slate-900">Javier "El Jurisconsulto"</div>
            <div class="text-xs text-red-700 font-semibold">Tuno Mayor · Bandurria</div>
            <div class="text-xs text-slate-500 mt-1">Generación 2018</div>
          </div>
          <div class="p-4 rounded-xl border border-slate-200 text-center hover:border-red-600 transition">
            <div class="w-20 h-20 mx-auto rounded-full bg-red-800 text-amber-300 flex items-center justify-center font-bold text-2xl mb-3">MG</div>
            <div class="font-bold text-slate-900">Marcos "El Notario"</div>
            <div class="text-xs text-red-700 font-semibold">Contador · Guitarra</div>
            <div class="text-xs text-slate-500 mt-1">Generación 2019</div>
          </div>
          <div class="p-4 rounded-xl border border-slate-200 text-center hover:border-red-600 transition">
            <div class="w-20 h-20 mx-auto rounded-full bg-red-800 text-amber-300 flex items-center justify-center font-bold text-2xl mb-3">AP</div>
            <div class="font-bold text-slate-900">Antonio "El Fiscal"</div>
            <div class="text-xs text-red-700 font-semibold">Solista · Laúd</div>
            <div class="text-xs text-slate-500 mt-1">Generación 2020</div>
          </div>
          <div class="p-4 rounded-xl border border-slate-200 text-center hover:border-red-600 transition">
            <div class="w-20 h-20 mx-auto rounded-full bg-red-800 text-amber-300 flex items-center justify-center font-bold text-2xl mb-3">CL</div>
            <div class="font-bold text-slate-900">Carlos "El Pasante"</div>
            <div class="text-xs text-amber-600 font-semibold">Novato · Pandereta</div>
            <div class="text-xs text-slate-500 mt-1">Generación 2023</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SECCIÓN 2: CONTRATACIÓN DE NUESTROS SERVICIOS -->
    <div id="visitante-contratacion" class="visitante-subview hidden max-w-7xl mx-auto px-4 py-12">
      <div class="mb-8">
        <span class="text-xs uppercase tracking-widest text-red-800 font-bold">2. Contratación de Servicios</span>
        <h2 class="text-3xl md:text-4xl font-serif font-black text-slate-900 mt-1">Presupuestos y Peticiones</h2>
        <div class="w-16 h-1 bg-amber-500 mt-3"></div>
      </div>

      <div class="grid lg:grid-cols-3 gap-8">
        <!-- Columna de contacto urgente y teléfono -->
        <div class="bg-gradient-to-br from-red-900 to-red-950 text-white rounded-2xl p-8 border-2 border-amber-400 shadow-xl flex flex-col justify-between">
          <div>
            <span class="inline-block px-3 py-1 rounded-full bg-amber-500 text-slate-950 font-black text-xs uppercase tracking-wider mb-4">Atención Directa</span>
            <h3 class="text-2xl font-serif font-bold text-amber-300 mb-3">¿Tienes fecha fija para tu evento?</h3>
            <p class="text-slate-200 text-sm mb-6 leading-relaxed">
              Para bodas, aniversarios o eventos de última hora recomendamos llamar directamente por teléfono o escribir por WhatsApp para confirmar disponibilidad inmediata de la cuadrilla.
            </p>

            <div class="bg-black/40 rounded-xl p-4 border border-amber-400/40 mb-6">
              <div class="text-xs text-amber-300 font-bold uppercase">Llámanos ahora:</div>
              <a href="tel:+34600123456" class="text-2xl font-black text-white hover:text-amber-300 transition block mt-1">+34 600 123 456</a>
              <div class="text-[11px] text-slate-400 mt-1">Disponibles 24/7 para presupuestos</div>
            </div>

            <a href="https://wa.me/34600123456" target="_blank" class="w-full py-3 bg-green-600 hover:bg-green-500 text-white font-bold rounded-xl text-center flex items-center justify-center gap-2 shadow-md transition">
              <span>💬</span> Escribir por WhatsApp
            </a>
          </div>

          <div class="mt-8 pt-6 border-t border-red-800 text-xs text-slate-300">
            ✉️ tuna.derecho.almeria@gmail.com
          </div>
        </div>

        <!-- Formulario de Contratación según Wireframe (2.1 y 2.1.1) -->
        <div class="lg:col-span-2 bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
          <div class="flex items-center justify-between mb-6 pb-4 border-b border-slate-100">
            <div>
              <span class="text-xs font-bold text-red-700 uppercase">Nodo 2.1.1</span>
              <h3 class="text-xl font-bold text-slate-900">Formulario Oficial de Contratación</h3>
            </div>
            <span class="text-xs text-slate-500">Respuesta en menos de 24h</span>
          </div>

          <form onsubmit="alert('¡Solicitud enviada correctamente! La Tuna de Derecho se pondrá en contacto contigo.'); return false;" class="space-y-4">
            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Nombre y Apellidos *</label>
                <input type="text" required placeholder="Ej. Carmen González" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 focus:ring-1 focus:ring-red-600 outline-none">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Teléfono de Contacto *</label>
                <input type="tel" required placeholder="Ej. 600 000 000" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 focus:ring-1 focus:ring-red-600 outline-none">
              </div>
            </div>

            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Correo Electrónico *</label>
                <input type="email" required placeholder="tu@email.com" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 focus:ring-1 focus:ring-red-600 outline-none">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Tipo de Actuación *</label>
                <select class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none bg-white">
                  <option>Boda (Salida de iglesia / Banquete)</option>
                  <option>Serenata a la novia / balcón</option>
                  <option>Evento corporativo / Congreso</option>
                  <option>Cumpleaños / Aniversario / Jubilación</option>
                  <option>Cena de gala de graduación</option>
                  <option>Otro evento festivo</option>
                </select>
              </div>
            </div>

            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Fecha del Evento *</label>
                <input type="date" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Municipio / Lugar de Almería *</label>
                <input type="text" required placeholder="Ej. Almería capital, Roquetas, El Ejido..." class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none">
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Detalles de la actuación o canciones especiales</label>
              <textarea rows="3" placeholder="Indícanos si quieres alguna canción en particular, duración aproximada o sorpresas..." class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none"></textarea>
            </div>

            <div class="flex items-center justify-between pt-2">
              <span class="text-xs text-slate-500">¿Ya tienes cuenta de cliente? <button type="button" onclick="switchProfile('cliente')" class="text-red-700 font-bold underline">Entra a tu panel</button></span>
              <button type="submit" class="px-6 py-3 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-sm shadow-md transition border border-amber-400">
                Enviar Solicitud de Contrato
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- SECCIÓN 3: CONTENIDO MULTIMEDIA (VÍDEOS, FOTOS Y CERTÁMENES) -->
    <div id="visitante-multimedia" class="visitante-subview hidden max-w-7xl mx-auto px-4 py-12">
      <div class="mb-8">
        <span class="text-xs uppercase tracking-widest text-red-800 font-bold">3. Contenido Multimedia</span>
        <h2 class="text-3xl md:text-4xl font-serif font-black text-slate-900 mt-1">Nuestros Mejores Momentos</h2>
        <div class="w-16 h-1 bg-amber-500 mt-3"></div>
      </div>

      <!-- Pestañas internas multimedia según árbol: 3.1.1 Vídeos, 3.1.2 Fotos, 3.2 Certámenes -->
      <div class="flex gap-2 border-b border-slate-200 pb-3 mb-8">
        <button onclick="filterMedia('todos')" class="px-4 py-1.5 rounded-lg bg-red-700 text-white text-xs font-bold">Todo</button>
        <button onclick="filterMedia('videos')" class="px-4 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-medium">3.1.1 Vídeos</button>
        <button onclick="filterMedia('fotos')" class="px-4 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-medium">3.1.2 Fotos</button>
        <button onclick="filterMedia('certamenes')" class="px-4 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-medium">3.2 Certámenes y Premios</button>
      </div>

      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Vídeo 1 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <div class="h-44 bg-slate-900 flex flex-col items-center justify-center text-white relative group cursor-pointer">
            <span class="text-4xl text-red-500 group-hover:scale-125 transition">▶️</span>
            <span class="text-xs text-slate-400 mt-2 font-mono">03:45 · YouTube</span>
          </div>
          <div class="p-4">
            <span class="text-[11px] font-bold text-red-700 uppercase">Vídeo 3.1.1</span>
            <h4 class="font-bold text-slate-900 mt-0.5">Clavelitos en el Balcón del Ayuntamiento</h4>
            <p class="text-slate-500 text-xs mt-1">Feria de Almería 2024</p>
          </div>
        </div>

        <!-- Vídeo 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <div class="h-44 bg-slate-900 flex flex-col items-center justify-center text-white relative group cursor-pointer">
            <span class="text-4xl text-red-500 group-hover:scale-125 transition">▶️</span>
            <span class="text-xs text-slate-400 mt-2 font-mono">04:12 · YouTube</span>
          </div>
          <div class="p-4">
            <span class="text-[11px] font-bold text-red-700 uppercase">Vídeo 3.1.1</span>
            <h4 class="font-bold text-slate-900 mt-0.5">Ronda y Serenata de Noche</h4>
            <p class="text-slate-500 text-xs mt-1">Casco Histórico de Almería</p>
          </div>
        </div>

        <!-- Foto 1 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <div class="h-44 bg-gradient-to-tr from-red-800 to-amber-700 flex flex-col items-center justify-center text-amber-200">
            <span class="text-4xl mb-1">📸</span>
            <span class="text-xs">Foto Oficial de Cuadrilla</span>
          </div>
          <div class="p-4">
            <span class="text-[11px] font-bold text-amber-700 uppercase">Foto 3.1.2</span>
            <h4 class="font-bold text-slate-900 mt-0.5">Actuación Apertura Curso Académico UAL</h4>
            <p class="text-slate-500 text-xs mt-1">Paraninfo Universidad de Almería</p>
          </div>
        </div>

        <!-- Certamen 1 -->
        <div class="bg-white rounded-2xl border-2 border-amber-300 overflow-hidden shadow-sm hover:shadow-md transition bg-gradient-to-b from-amber-50/40 to-white">
          <div class="h-44 bg-red-950 flex flex-col items-center justify-center text-amber-300 p-4 text-center">
            <span class="text-4xl mb-1">🏆</span>
            <span class="font-serif font-black text-lg">1º Premio Mejor Tuna</span>
            <span class="text-xs text-slate-300">Certamen Nacional de Derecho</span>
          </div>
          <div class="p-4">
            <span class="text-[11px] font-bold text-red-700 uppercase">Certamen 3.2</span>
            <h4 class="font-bold text-slate-900 mt-0.5">XXX Certamen de Tunas de Derecho de España</h4>
            <p class="text-slate-500 text-xs mt-1">Premio al mejor pasacalles y mejor repertorio</p>
          </div>
        </div>

        <!-- Certamen 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <div class="h-44 bg-red-900 flex flex-col items-center justify-center text-amber-200 p-4 text-center">
            <span class="text-4xl mb-1">🥈</span>
            <span class="font-serif font-black text-lg">Premio Mejor Pandereta</span>
            <span class="text-xs text-slate-300">Certamen Ciudad de Granada</span>
          </div>
          <div class="p-4">
            <span class="text-[11px] font-bold text-red-700 uppercase">Certamen 3.2</span>
            <h4 class="font-bold text-slate-900 mt-0.5">Certamen Andaluz de Tunas Universitarias</h4>
            <p class="text-slate-500 text-xs mt-1">Galardón a la destreza acrobática con pandereta</p>
          </div>
        </div>

        <!-- Foto 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <div class="h-44 bg-slate-800 flex flex-col items-center justify-center text-slate-300">
            <span class="text-4xl mb-1">🎸</span>
            <span class="text-xs">Ensayo en la Facultad</span>
          </div>
          <div class="p-4">
            <span class="text-[11px] font-bold text-amber-700 uppercase">Foto 3.1.2</span>
            <h4 class="font-bold text-slate-900 mt-0.5">Tarde de Guitarras y Novatadas</h4>
            <p class="text-slate-500 text-xs mt-1">Local de Ensayos Edificio Derecho</p>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- SECCIÓN 4: TIENDA OFICIAL (CATÁLOGO, PRODUCTOS, CESTA, CHECKOUT) ⭐ -->
    <!-- ========================================================================= -->
    <div id="visitante-tienda" class="visitante-subview hidden max-w-7xl mx-auto px-4 py-12">
      <div class="mb-8 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <span class="text-xs uppercase tracking-widest text-red-800 font-bold">4. Tienda Oficial de la Tuna</span>
          <h2 class="text-3xl md:text-4xl font-serif font-black text-slate-900 mt-1">Catálogo Oficial de Merchandising</h2>
          <div class="w-16 h-1 bg-amber-500 mt-3"></div>
        </div>
        <div class="flex items-center gap-3">
          <button onclick="showVisitanteSection('visitante-cesta')" class="px-5 py-2.5 rounded-xl bg-red-800 hover:bg-red-700 text-white font-bold text-sm shadow-md transition flex items-center gap-2 border border-amber-400">
            <span>🛒</span> Ver Mi Cesta (<span id="shop-cart-badge">2</span> artículos)
          </button>
        </div>
      </div>

      <!-- Banner de la Tienda -->
      <div class="rounded-2xl bg-gradient-to-r from-red-900 via-red-800 to-amber-700 text-white p-6 md:p-8 mb-8 shadow-md flex flex-col md:flex-row items-center justify-between gap-6 border-2 border-amber-400">
        <div>
          <span class="px-3 py-1 bg-amber-400 text-slate-950 font-bold text-xs rounded-full uppercase">Envíos a toda España</span>
          <h3 class="text-2xl font-serif font-bold mt-2">Apoya a la Tuna de Derecho de Almería</h3>
          <p class="text-slate-200 text-sm mt-1 max-w-xl">Todos los beneficios de la tienda se destinan a la compra de instrumentos, viajes a certámenes y mantenimiento de la asociación universitaria.</p>
        </div>
        <div class="text-right">
          <div class="text-xs text-amber-200">¿Dudas con tu talla o envío?</div>
          <div class="text-lg font-black text-white">📞 +34 600 123 456</div>
        </div>
      </div>

      <!-- Filtros según Wireframe Catalogo.html -->
      <div class="bg-white rounded-xl border border-slate-200 p-4 mb-8 shadow-sm flex flex-wrap items-center gap-4">
        <div class="flex-1 min-w-[200px]">
          <label class="block text-[11px] font-bold text-slate-600 uppercase mb-1">Categoría</label>
          <select class="w-full px-3 py-2 border border-slate-300 rounded-lg text-xs bg-white">
            <option>Todas las categorías</option>
            <option>Ropa (Sudaderas, Camisetas)</option>
            <option>Accesorios (Parches, Pines, Llaveros)</option>
            <option>Música (CDs, Cancioneros)</option>
          </select>
        </div>
        <div class="flex-1 min-w-[200px]">
          <label class="block text-[11px] font-bold text-slate-600 uppercase mb-1">Rango de Precio</label>
          <select class="w-full px-3 py-2 border border-slate-300 rounded-lg text-xs bg-white">
            <option>Cualquier precio</option>
            <option>Hasta 10 €</option>
            <option>De 10 € a 25 €</option>
            <option>Más de 25 €</option>
          </select>
        </div>
        <div class="self-end">
          <button class="px-5 py-2 bg-slate-900 text-white rounded-lg text-xs font-bold hover:bg-slate-800 transition">
            Aplicar Filtros
          </button>
        </div>
      </div>

      <!-- CATÁLOGO DE PRODUCTOS (4.1 Catálogo) -->
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
        <!-- Producto 1 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-lg transition flex flex-col justify-between group">
          <div>
            <div class="h-48 bg-slate-100 flex items-center justify-center text-slate-400 group-hover:bg-red-50 transition relative">
              <span class="text-6xl">👕</span>
              <span class="absolute top-2 left-2 px-2 py-0.5 bg-red-700 text-white font-bold text-[10px] rounded">Más Vendido</span>
            </div>
            <div class="p-4">
              <span class="text-[11px] text-red-700 font-semibold uppercase">Ropa Oficial</span>
              <h4 class="font-bold text-slate-900 text-base mt-0.5">Sudadera Roja Tuna de Derecho</h4>
              <p class="text-slate-500 text-xs mt-1">Con escudo bordado de la UAL y lema oficial.</p>
              <div class="mt-3 flex items-baseline gap-2">
                <span class="text-xl font-black text-red-800">28,00 €</span>
                <span class="text-xs text-slate-400 line-through">35,00 €</span>
              </div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('Sudadera Roja Tuna Derecho', 28.00)" class="w-full py-2.5 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-xs shadow transition flex items-center justify-center gap-1.5">
              <span>🛒</span> Añadir a la Cesta
            </button>
          </div>
        </div>

        <!-- Producto 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-lg transition flex flex-col justify-between group">
          <div>
            <div class="h-48 bg-slate-100 flex items-center justify-center text-slate-400 group-hover:bg-red-50 transition">
              <span class="text-6xl">💿</span>
            </div>
            <div class="p-4">
              <span class="text-[11px] text-amber-700 font-semibold uppercase">Música & Grabaciones</span>
              <h4 class="font-bold text-slate-900 text-base mt-0.5">CD "25 Años de Ronda"</h4>
              <p class="text-slate-500 text-xs mt-1">16 temas remasterizados: Clavelitos, Fonseca, La Morena de mi Copla.</p>
              <div class="mt-3">
                <span class="text-xl font-black text-red-800">12,00 €</span>
              </div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('CD 25 Años de Ronda', 12.00)" class="w-full py-2.5 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-xs shadow transition flex items-center justify-center gap-1.5">
              <span>🛒</span> Añadir a la Cesta
            </button>
          </div>
        </div>

        <!-- Producto 3 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-lg transition flex flex-col justify-between group">
          <div>
            <div class="h-48 bg-slate-100 flex items-center justify-center text-slate-400 group-hover:bg-red-50 transition">
              <span class="text-6xl">🎖️</span>
            </div>
            <div class="p-4">
              <span class="text-[11px] text-red-700 font-semibold uppercase">Accesorios Oficiales</span>
              <h4 class="font-bold text-slate-900 text-base mt-0.5">Parche Bordado Beca de Derecho</h4>
              <p class="text-slate-500 text-xs mt-1">Escudo oficial bordado en hilo de oro para capa o chaqueta.</p>
              <div class="mt-3">
                <span class="text-xl font-black text-red-800">6,50 €</span>
              </div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('Parche Bordado Beca', 6.50)" class="w-full py-2.5 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-xs shadow transition flex items-center justify-center gap-1.5">
              <span>🛒</span> Añadir a la Cesta
            </button>
          </div>
        </div>

        <!-- Producto 4 -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-lg transition flex flex-col justify-between group">
          <div>
            <div class="h-48 bg-slate-100 flex items-center justify-center text-slate-400 group-hover:bg-red-50 transition">
              <span class="text-6xl">📖</span>
            </div>
            <div class="p-4">
              <span class="text-[11px] text-amber-700 font-semibold uppercase">Publicaciones</span>
              <h4 class="font-bold text-slate-900 text-base mt-0.5">Cancionero Oficial Ilustrado</h4>
              <p class="text-slate-500 text-xs mt-1">Letras y acordes para guitarra y bandurria de más de 40 canciones.</p>
              <div class="mt-3">
                <span class="text-xl font-black text-red-800">9,00 €</span>
              </div>
            </div>
          </div>
          <div class="p-4 pt-0">
            <button onclick="addToCart('Cancionero Oficial Ilustrado', 9.00)" class="w-full py-2.5 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-xs shadow transition flex items-center justify-center gap-1.5">
              <span>🛒</span> Añadir a la Cesta
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- SECCIÓN 4.2: CESTA Y PROCESO DE COMPRA (CHECKOUT) SEGÚN ÁRBOL -->
    <div id="visitante-cesta" class="visitante-subview hidden max-w-7xl mx-auto px-4 py-12">
      <div class="mb-8">
        <span class="text-xs uppercase tracking-widest text-red-800 font-bold">4.2 Cesta de la Compra y Pasarela</span>
        <h2 class="text-3xl md:text-4xl font-serif font-black text-slate-900 mt-1">Tu Pedido de Merchandising</h2>
        <div class="w-16 h-1 bg-amber-500 mt-3"></div>
      </div>

      <!-- Diagrama de Pasos del Árbol de Tienda -->
      <div class="bg-white p-4 rounded-xl border border-slate-200 mb-8 flex flex-wrap items-center justify-between gap-3 text-xs">
        <span class="font-bold text-slate-500 uppercase">Flujo de Compra:</span>
        <span class="px-3 py-1 bg-red-700 text-white font-bold rounded-full">4.2 Cesta</span>
        <span class="text-slate-400">➔</span>
        <span class="px-3 py-1 bg-slate-100 text-slate-700 rounded-full">4.2.1 Inicio Sesión</span>
        <span class="text-slate-400">➔</span>
        <span class="px-3 py-1 bg-slate-100 text-slate-700 rounded-full">4.2.1.1 Dirección</span>
        <span class="text-slate-400">➔</span>
        <span class="px-3 py-1 bg-slate-100 text-slate-700 rounded-full">4.2.1.1.1 Pago</span>
        <span class="text-slate-400">➔</span>
        <span class="px-3 py-1 bg-slate-100 text-slate-700 rounded-full">4.2.1.1.1.1 Recibo</span>
      </div>

      <div class="grid lg:grid-cols-3 gap-8">
        <!-- Lista de productos en la cesta -->
        <div class="lg:col-span-2 bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
          <h3 class="text-lg font-bold text-slate-900 mb-4 pb-3 border-b border-slate-100">Artículos en la Cesta</h3>
          <div class="divide-y divide-slate-100">
            <div class="py-4 flex items-center justify-between gap-4">
              <div class="flex items-center gap-4">
                <div class="w-16 h-16 rounded-xl bg-red-100 flex items-center justify-center text-2xl">👕</div>
                <div>
                  <h4 class="font-bold text-slate-900 text-sm">Sudadera Roja Tuna de Derecho</h4>
                  <div class="text-xs text-slate-500">Talla: L · Color: Rojo Burdeos</div>
                  <div class="text-xs text-red-700 font-bold mt-1">28,00 €</div>
                </div>
              </div>
              <div class="flex items-center gap-3">
                <span class="text-xs font-bold px-2 py-1 bg-slate-100 rounded">Cant: 1</span>
                <span class="font-bold text-slate-900 text-sm">28,00 €</span>
              </div>
            </div>

            <div class="py-4 flex items-center justify-between gap-4">
              <div class="flex items-center gap-4">
                <div class="w-16 h-16 rounded-xl bg-amber-100 flex items-center justify-center text-2xl">🎖️</div>
                <div>
                  <h4 class="font-bold text-slate-900 text-sm">Parche Bordado Beca de Derecho</h4>
                  <div class="text-xs text-slate-500">Bordado Oro</div>
                  <div class="text-xs text-red-700 font-bold mt-1">6,50 €</div>
                </div>
              </div>
              <div class="flex items-center gap-3">
                <span class="text-xs font-bold px-2 py-1 bg-slate-100 rounded">Cant: 1</span>
                <span class="font-bold text-slate-900 text-sm">6,50 €</span>
              </div>
            </div>
          </div>

          <div class="mt-6 pt-4 border-t border-slate-200 flex justify-between items-center">
            <button onclick="showVisitanteSection('visitante-tienda')" class="text-xs font-bold text-red-700 hover:underline">
              ← Seguir comprando en el catálogo
            </button>
            <button onclick="alert('Cesta vaciada');" class="text-xs text-slate-400 hover:text-red-600">
              Vaciar cesta
            </button>
          </div>
        </div>

        <!-- Formulario Checkout (Dirección + Método de Pago) -->
        <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
          <h3 class="text-lg font-bold text-slate-900 mb-4 pb-3 border-b border-slate-100">Resumen y Tramitación</h3>
          <div class="space-y-3 text-sm mb-6">
            <div class="flex justify-between text-slate-600">
              <span>Subtotal artículos:</span>
              <span class="font-semibold text-slate-900">34,50 €</span>
            </div>
            <div class="flex justify-between text-slate-600">
              <span>Gastos de envío (Península):</span>
              <span class="font-semibold text-green-600">GRATIS</span>
            </div>
            <div class="pt-3 border-t border-slate-200 flex justify-between text-base font-bold text-slate-900">
              <span>Total a pagar:</span>
              <span class="text-xl text-red-800 font-black">34,50 €</span>
            </div>
          </div>

          <!-- Campos de envío mock -->
          <div class="space-y-3 pt-3 border-t border-slate-100 mb-6">
            <div class="text-xs font-bold text-slate-700 uppercase">4.2.1.1 Dirección de Envío</div>
            <input type="text" placeholder="Calle, número, piso..." class="w-full px-3 py-2 border border-slate-300 rounded-lg text-xs outline-none">
            <div class="grid grid-cols-2 gap-2">
              <input type="text" placeholder="Código Postal" class="px-3 py-2 border border-slate-300 rounded-lg text-xs outline-none">
              <input type="text" placeholder="Ciudad (Ej. Almería)" class="px-3 py-2 border border-slate-300 rounded-lg text-xs outline-none">
            </div>

            <div class="text-xs font-bold text-slate-700 uppercase pt-2">4.2.1.1.1 Método de Pago</div>
            <div class="space-y-2 text-xs">
              <label class="flex items-center gap-2 p-2 border border-red-200 bg-red-50 rounded-lg cursor-pointer">
                <input type="radio" name="pago" checked class="text-red-700">
                <span class="font-semibold text-slate-800">Tarjeta de Crédito / Débito (Bizum)</span>
              </label>
              <label class="flex items-center gap-2 p-2 border border-slate-200 rounded-lg cursor-pointer">
                <input type="radio" name="pago" class="text-red-700">
                <span class="font-semibold text-slate-800">Transferencia Bancaria</span>
              </label>
            </div>
          </div>

          <button onclick="alert('¡Pago completado con éxito! Recibo: #PED-2026-894. Te llegará la confirmación al correo.');" class="w-full py-3 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-sm shadow-md transition border border-amber-400">
            Confirmar y Pagar (34,50 €)
          </button>
        </div>
      </div>
    </div>

    <!-- SECCIÓN 5: CANCIONERO (REPERTORIO Y SPOTIFY) -->
    <div id="visitante-cancionero" class="visitante-subview hidden max-w-7xl mx-auto px-4 py-12">
      <div class="mb-8">
        <span class="text-xs uppercase tracking-widest text-red-800 font-bold">5. Cancionero Tradicional</span>
        <h2 class="text-3xl md:text-4xl font-serif font-black text-slate-900 mt-1">Repertorio y Discografía</h2>
        <div class="w-16 h-1 bg-amber-500 mt-3"></div>
      </div>

      <div class="grid lg:grid-cols-3 gap-8">
        <!-- 5.1 Canciones / Letras -->
        <div class="lg:col-span-2 bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
          <div class="flex items-center gap-3 mb-6">
            <span class="px-3 py-1 bg-red-100 text-red-800 font-bold text-xs rounded-full">Nodo 5.1</span>
            <h3 class="text-xl font-bold text-slate-900">Letras y Repertorio de Ronda</h3>
          </div>

          <div class="space-y-4">
            <details class="p-4 rounded-xl border border-slate-200 bg-slate-50 group" open>
              <summary class="font-bold text-slate-900 cursor-pointer flex justify-between items-center">
                <span>🌹 Clavelitos (Canción universal de Tuna)</span>
                <span class="text-red-700 font-bold text-sm">Ver letra ▼</span>
              </summary>
              <div class="mt-4 pt-3 border-t border-slate-200 text-sm text-slate-600 font-serif leading-relaxed italic">
                "Mocita dame el clavel, dame el clavel de tu boca,<br>
                que pa' eso no hay que tener mucha vergüenza ni poca.<br>
                Yo te daré un cascabel, te lo prometo mocita,<br>
                si tú me das ese clavel que llevas en tu boquita..."
              </div>
            </details>

            <details class="p-4 rounded-xl border border-slate-200 bg-slate-50 group">
              <summary class="font-bold text-slate-900 cursor-pointer flex justify-between items-center">
                <span>🎓 Pasacalles de Fonseca</span>
                <span class="text-red-700 font-bold text-sm">Ver letra ▼</span>
              </summary>
              <div class="mt-4 pt-3 border-t border-slate-200 text-sm text-slate-600 font-serif leading-relaxed italic">
                "Adiós villa de Fonseca, ya me marcho de aquí,<br>
                no te olvides de este tuno que suspira por ti..."
              </div>
            </details>

            <details class="p-4 rounded-xl border border-slate-200 bg-slate-50 group">
              <summary class="font-bold text-slate-900 cursor-pointer flex justify-between items-center">
                <span>🌙 Serenata Nocturna a Almería</span>
                <span class="text-red-700 font-bold text-sm">Ver letra ▼</span>
              </summary>
              <div class="mt-4 pt-3 border-t border-slate-200 text-sm text-slate-600 font-serif leading-relaxed italic">
                "Bajo tu ventana canto, tierra de sol y de mar,<br>
                la tuna de leyes llega para hacerte suspirar..."
              </div>
            </details>
          </div>
        </div>

        <!-- 5.2 Spotify Widget Mockup -->
        <div class="bg-gradient-to-br from-green-950 via-slate-900 to-black text-white rounded-2xl p-6 border-2 border-green-500 shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-4">
              <span class="text-3xl text-green-400">🟢</span>
              <div>
                <span class="text-[11px] uppercase tracking-wider text-green-400 font-bold block">Nodo 5.2</span>
                <h4 class="font-bold text-white text-base">Escúchanos en Spotify</h4>
              </div>
            </div>
            <p class="text-xs text-slate-300 mb-6">Álbum oficial de la Tuna de Derecho de la Universidad de Almería disponible en todas las plataformas digitales.</p>

            <div class="bg-slate-800/80 rounded-xl p-4 border border-slate-700 space-y-3">
              <div class="flex items-center justify-between text-xs pb-2 border-b border-slate-700">
                <span class="font-semibold text-slate-200">1. Clavelitos</span>
                <span class="text-slate-400 font-mono">03:12</span>
              </div>
              <div class="flex items-center justify-between text-xs pb-2 border-b border-slate-700">
                <span class="font-semibold text-slate-200">2. Serenata Almeriense</span>
                <span class="text-slate-400 font-mono">04:05</span>
              </div>
              <div class="flex items-center justify-between text-xs">
                <span class="font-semibold text-slate-200">3. La Morena de mi Copla</span>
                <span class="text-slate-400 font-mono">02:58</span>
              </div>
            </div>
          </div>

          <a href="https://spotify.com" target="_blank" class="mt-6 w-full py-3 bg-green-500 hover:bg-green-400 text-slate-950 font-black rounded-xl text-center text-xs uppercase tracking-wider transition">
            Abrir Playlist en Spotify
          </a>
        </div>
      </div>
    </div>

    <!-- SECCIÓN 6: ÚNETE A NOSOTROS (FORMULARIO Y LOCAL DE ENSAYO) -->
    <div id="visitante-unete" class="visitante-subview hidden max-w-7xl mx-auto px-4 py-12">
      <div class="mb-8">
        <span class="text-xs uppercase tracking-widest text-red-800 font-bold">6. Únete a Nosotros</span>
        <h2 class="text-3xl md:text-4xl font-serif font-black text-slate-900 mt-1">Forma Parte de la Hermandad</h2>
        <div class="w-16 h-1 bg-amber-500 mt-3"></div>
      </div>

      <div class="grid lg:grid-cols-2 gap-8">
        <!-- 6.1 Formulario para unirse -->
        <div class="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
          <div class="flex items-center gap-3 mb-6">
            <span class="px-3 py-1 bg-red-100 text-red-800 font-bold text-xs rounded-full">Nodo 6.1</span>
            <h3 class="text-xl font-bold text-slate-900">Formulario de Inscripción para Nuevos Miembros</h3>
          </div>
          <p class="text-slate-600 text-sm mb-6">¿Estudias en la Universidad de Almería? No hace falta que sepas tocar ningún instrumento, te enseñamos gratis desde cero (guitarra, laúd, bandurria o pandereta).</p>

          <form onsubmit="alert('¡Gracias por tu interés! El Tuno Mayor te contactará para invitarte al próximo ensayo.'); return false;" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Nombre Completo *</label>
              <input type="text" required placeholder="Tu nombre" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none">
            </div>
            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Teléfono Móvil *</label>
                <input type="tel" required placeholder="600 000 000" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Titulación en la UAL *</label>
                <input type="text" required placeholder="Ej. Grado en Derecho, ADE..." class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none">
              </div>
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase mb-1">¿Tienes experiencia musical?</label>
              <select class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none bg-white">
                <option>Ninguna (quiero aprender de cero)</option>
                <option>Toco algo de guitarra o ukelele</option>
                <option>Toco bandurria o laúd</option>
                <option>Toco percusión / pandereta</option>
                <option>Canto en coros o solista</option>
              </select>
            </div>
            <button type="submit" class="w-full py-3 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-sm shadow-md transition border border-amber-400">
              Enviar Solicitud de Entrada
            </button>
          </form>
        </div>

        <!-- 6.2 Local de Ensayo -->
        <div class="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-6">
              <span class="px-3 py-1 bg-amber-100 text-amber-800 font-bold text-xs rounded-full">Nodo 6.2</span>
              <h3 class="text-xl font-bold text-slate-900">Dónde y Cuándo Ensayamos</h3>
            </div>
            <div class="space-y-4 text-sm text-slate-600">
              <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                <strong class="text-slate-900 block mb-1">📍 Ubicación del Local:</strong>
                Facultad de Derecho, Planta Baja (Junto al Aula Magna y Sala de Asociaciones).<br>
                Universidad de Almería, Ctra. Sacramento s/n, La Cañada de San Urbano.
              </div>
              <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                <strong class="text-slate-900 block mb-1">🕒 Horarios de Ensayos:</strong>
                Martes y Jueves: 19:30 h a 21:30 h.<br>
                Viernes de ronda: A partir de las 22:00 h en el centro de Almería.
              </div>
            </div>
          </div>

          <div class="mt-8 p-4 rounded-xl bg-red-900 text-white text-center">
            <span class="text-xs text-amber-300 font-bold uppercase block">Contacto con el Maestre de Novatos</span>
            <a href="tel:+34600123456" class="text-lg font-black text-white hover:text-amber-300 transition">+34 600 123 456</a>
          </div>
        </div>
      </div>
    </div>

    <!-- SECCIÓN 7: INICIO DE SESIÓN / REGISTRO / RECUPERAR CONTRASEÑA -->
    <div id="visitante-acceso" class="visitante-subview hidden max-w-md mx-auto px-4 py-16">
      <div class="bg-white rounded-2xl border border-slate-200 p-8 shadow-xl">
        <div class="text-center mb-6">
          <div class="w-14 h-14 rounded-full bg-red-800 text-amber-300 flex items-center justify-center font-bold text-2xl mx-auto mb-3 border-2 border-amber-400">
            TD
          </div>
          <span class="text-xs uppercase tracking-widest text-red-800 font-bold">Nodo 7</span>
          <h3 class="text-2xl font-serif font-black text-slate-900 mt-1">Acceso a la Plataforma</h3>
          <p class="text-slate-500 text-xs mt-1">Inicia sesión como cliente o como administrador</p>
        </div>

        <form onsubmit="switchProfile('cliente'); return false;" class="space-y-4">
          <div>
            <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Correo Electrónico</label>
            <input type="email" value="cliente@almeria.es" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none">
          </div>
          <div>
            <div class="flex justify-between items-center mb-1">
              <label class="block text-xs font-bold text-slate-700 uppercase">Contraseña</label>
              <button type="button" onclick="alert('Nodo 7.1: Se ha enviado un enlace para restablecer tu contraseña a tu email.');" class="text-xs text-red-700 hover:underline">
                7.1 ¿Olvidaste tu contraseña?
              </button>
            </div>
            <input type="password" value="********" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-red-600 outline-none">
          </div>
          <button type="submit" class="w-full py-3 bg-red-800 hover:bg-red-700 text-white font-bold rounded-xl text-sm shadow-md transition border border-amber-400">
            Iniciar Sesión
          </button>
        </form>

        <div class="mt-6 pt-6 border-t border-slate-100 text-center space-y-3">
          <div class="text-xs text-slate-600">
            Nodo 7.2: ¿No tienes cuenta? <button onclick="alert('Nodo 7.2: Formulario de Registro de Nuevo Cliente abierto.');" class="text-red-700 font-bold underline">Regístrate aquí</button>
          </div>
          <div class="p-3 bg-amber-50 rounded-xl text-left text-xs text-amber-900 border border-amber-200">
            <strong>💡 Consejo del Mockup:</strong><br>
            Puedes usar el selector superior para saltar directamente a la vista de <strong>Cliente</strong> o de <strong>Administrador</strong>.
          </div>
        </div>
      </div>
    </div>

  </div>


  <!-- ========================================================================= -->
  <!-- 2. PERFIL: CLIENTE (HISTORIAL DE CONTRATOS, PEDIDOS, GESTIÓN DE CUENTA) -->
  <!-- ========================================================================= -->
  <div id="profile-cliente" class="flex-1 flex flex-col hidden bg-slate-50">

    <!-- Header del Área de Cliente -->
    <header class="bg-white border-b border-slate-200 py-3 px-6 sticky top-12 z-30 shadow-sm flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="w-9 h-9 rounded-lg bg-blue-700 text-white font-bold flex items-center justify-center text-sm">👤</span>
        <div>
          <span class="text-xs text-blue-700 font-bold uppercase tracking-wider">ÁREA PRIVADA DEL CLIENTE</span>
          <div class="text-base font-bold text-slate-900 leading-tight">Bienvenido, José Manuel Martínez</div>
        </div>
      </div>

      <div class="flex items-center gap-3">
        <span class="text-xs text-slate-500 hidden sm:inline">Cliente ID: #CLI-0412</span>
        <button onclick="switchProfile('visitante')" class="px-3 py-1.5 rounded-lg border border-slate-300 text-slate-700 text-xs font-semibold hover:bg-slate-100">
          Cerrar Sesión
        </button>
      </div>
    </header>

    <!-- Layout Cliente (Sidebar + Contenido) -->
    <div class="max-w-7xl mx-auto w-full px-4 py-8 flex-1 grid lg:grid-cols-4 gap-8">
      
      <!-- Menú Lateral Cliente (según Árbol de Cliente 1, 2, 3) -->
      <aside class="space-y-2">
        <div class="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-1">
          <div class="text-[11px] font-bold text-slate-400 uppercase px-3 py-1">Navegación Cliente</div>
          
          <button onclick="showClientSection('cliente-dashboard')" id="btn-c-dash" class="client-menu-item active w-full text-left px-3 py-2.5 rounded-xl text-xs font-bold flex items-center gap-2 transition">
            <span>🏠</span> 0. Inicio de Cliente
          </button>
          
          <button onclick="showClientSection('cliente-contratos')" id="btn-c-contratos" class="client-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>📜</span> 1. Historial de Contratos
          </button>
          
          <button onclick="showClientSection('cliente-pedidos')" id="btn-c-pedidos" class="client-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>🛍️</span> 2. Historial de Pedidos
          </button>
          
          <button onclick="showClientSection('cliente-cuenta')" id="btn-c-cuenta" class="client-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>⚙️</span> 3. Gestionar Cuenta
          </button>
        </div>

        <!-- Tarjeta de Contacto Directo para el Cliente -->
        <div class="bg-red-900 text-white rounded-2xl p-5 border border-amber-400 shadow-md text-xs">
          <span class="text-amber-300 font-bold uppercase tracking-wider text-[10px] block">¿Incidencias con tu actuación?</span>
          <p class="mt-1 text-slate-200">Contacta con el Tuno Mayor directamente para coordinar horas y canciones:</p>
          <a href="tel:+34600123456" class="mt-3 block p-2 bg-red-800 text-white rounded-lg font-black text-center text-sm hover:bg-red-700">
            📞 +34 600 123 456
          </a>
        </div>
      </aside>

      <!-- Panel Principal Cliente -->
      <main class="lg:col-span-3">

        <!-- SUBVISTA CLIENTE 0: DASHBOARD RESUMEN -->
        <div id="cliente-dashboard" class="client-subview space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <h2 class="text-2xl font-serif font-bold text-slate-900">Panel de Control de tu Cuenta</h2>
            <p class="text-slate-500 text-xs mt-1">Gestiona tus peticiones de contratación para eventos y las compras de merchandising.</p>

            <div class="grid sm:grid-cols-2 gap-4 mt-6">
              <div class="p-4 rounded-xl bg-amber-50 border border-amber-200">
                <span class="text-xs text-amber-800 font-bold uppercase">Contratos Activos</span>
                <div class="text-2xl font-black text-amber-950 mt-1">1 Próximo Evento</div>
                <div class="text-xs text-amber-700 mt-1">Boda en Roquetas de Mar · 18 de Julio</div>
              </div>
              <div class="p-4 rounded-xl bg-blue-50 border border-blue-200">
                <span class="text-xs text-blue-800 font-bold uppercase">Pedidos en Tienda</span>
                <div class="text-2xl font-black text-blue-950 mt-1">2 Pedidos Realizados</div>
                <div class="text-xs text-blue-700 mt-1">Último: #PED-894 (Enviado)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- SUBVISTA CLIENTE 1: HISTORIAL DE CONTRATOS & DETALLE (Nodos 1 y 1.1) -->
        <div id="cliente-contratos" class="client-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div>
                <span class="text-xs font-bold text-red-700 uppercase">Nodo 1</span>
                <h3 class="text-xl font-bold text-slate-900">Historial de Contratos de Servicios</h3>
              </div>
              <button onclick="switchProfile('visitante'); showVisitanteSection('visitante-contratacion');" class="px-3 py-1.5 bg-red-800 text-white font-bold rounded-lg text-xs">
                + Nueva Contratación
              </button>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 text-slate-500 uppercase font-bold border-b border-slate-200">
                  <tr>
                    <th class="py-3 px-4">Nº Contrato</th>
                    <th class="py-3 px-4">Tipo Evento</th>
                    <th class="py-3 px-4">Fecha Evento</th>
                    <th class="py-3 px-4">Lugar</th>
                    <th class="py-3 px-4">Estado</th>
                    <th class="py-3 px-4 text-right">Acción (1.1)</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100">
                  <tr>
                    <td class="py-3 px-4 font-bold">#CTR-2026-042</td>
                    <td class="py-3 px-4">Boda Civil & Banquete</td>
                    <td class="py-3 px-4">18/07/2026 (21:00h)</td>
                    <td class="py-3 px-4">Finca Almería Costa</td>
                    <td class="py-3 px-4"><span class="px-2 py-0.5 rounded-full bg-green-100 text-green-800 font-bold">Confirmado</span></td>
                    <td class="py-3 px-4 text-right">
                      <button onclick="alert('Nodo 1.1 Detalle del Contrato:\\n\\nNº: #CTR-2026-042\\nCuadrilla: 12 Tunos\\nRepertorio acordado: 8 canciones + pasacalles\\nImporte: 450,00 € (Señal abonada: 150 €)');" class="text-red-700 font-bold hover:underline">Ver Detalle</button>
                    </td>
                  </tr>
                  <tr>
                    <td class="py-3 px-4 font-bold">#CTR-2025-118</td>
                    <td class="py-3 px-4">Serenata Balcón</td>
                    <td class="py-3 px-4">14/02/2025 (23:30h)</td>
                    <td class="py-3 px-4">Almería Centro</td>
                    <td class="py-3 px-4"><span class="px-2 py-0.5 rounded-full bg-slate-100 text-slate-700 font-bold">Completado</span></td>
                    <td class="py-3 px-4 text-right">
                      <button onclick="alert('Nodo 1.1: Contrato histórico completado.');" class="text-red-700 font-bold hover:underline">Ver Detalle</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- SUBVISTA CLIENTE 2: HISTORIAL DE PEDIDOS, EDITAR & DEVOLUCIÓN (Nodos 2, 2.1, 2.1.1, 2.1.2) -->
        <div id="cliente-pedidos" class="client-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-red-700 uppercase">Nodo 2</span>
            <h3 class="text-xl font-bold text-slate-900 mb-4">Historial de Pedidos de la Tienda</h3>

            <div class="space-y-4">
              <!-- Tarjeta Pedido 1 -->
              <div class="border border-slate-200 rounded-xl p-4 bg-slate-50">
                <div class="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-200 text-xs">
                  <div>
                    <span class="font-bold text-slate-900">Pedido #PED-2026-894</span>
                    <span class="text-slate-500 ml-2">Realizado el 02/03/2026</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800 font-bold">Enviado por Correos</span>
                    <span class="font-bold text-slate-900">34,50 €</span>
                  </div>
                </div>
                <div class="py-3 text-xs text-slate-600 flex items-center justify-between">
                  <span>1x Sudadera Roja (L), 1x Parche Beca Derecho</span>
                  <div class="flex items-center gap-3">
                    <button onclick="alert('Nodo 2.1.1: Permitido modificar dirección de entrega antes de reparto final.');" class="text-blue-700 font-bold hover:underline">2.1.1 Editar Datos</button>
                    <button onclick="alert('Nodo 2.1.2: Trámite de Devolución iniciado. Te contactaremos con la etiqueta prepagada.');" class="text-red-700 font-bold hover:underline">2.1.2 Tramitar Devolución</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- SUBVISTA CLIENTE 3: GESTIONAR CUENTA (Nodos 3, 3.1, 3.2) -->
        <div id="cliente-cuenta" class="client-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-red-700 uppercase">Nodo 3</span>
            <h3 class="text-xl font-bold text-slate-900 mb-6">Gestionar Datos de la Cuenta</h3>

            <div class="grid md:grid-cols-2 gap-8">
              <!-- 3.1 Modificar Información Personal -->
              <div>
                <h4 class="text-sm font-bold text-slate-800 uppercase mb-4 flex items-center gap-2">
                  <span>👤</span> 3.1 Información Personal
                </h4>
                <form onsubmit="alert('Información personal actualizada'); return false;" class="space-y-3 text-xs">
                  <div>
                    <label class="block font-semibold text-slate-600 mb-1">Nombre Completo</label>
                    <input type="text" value="José Manuel Martínez" class="w-full px-3 py-2 border border-slate-300 rounded-lg outline-none">
                  </div>
                  <div>
                    <label class="block font-semibold text-slate-600 mb-1">Teléfono</label>
                    <input type="tel" value="612 345 678" class="w-full px-3 py-2 border border-slate-300 rounded-lg outline-none">
                  </div>
                  <div>
                    <label class="block font-semibold text-slate-600 mb-1">Correo Electrónico</label>
                    <input type="email" value="cliente@almeria.es" class="w-full px-3 py-2 border border-slate-300 rounded-lg outline-none">
                  </div>
                  <button type="submit" class="px-4 py-2 bg-slate-900 text-white rounded-lg font-bold">Guardar Cambios</button>
                </form>
              </div>

              <!-- 3.2 Cambiar Contraseña -->
              <div class="border-t md:border-t-0 md:border-l border-slate-200 pt-6 md:pt-0 md:pl-8">
                <h4 class="text-sm font-bold text-slate-800 uppercase mb-4 flex items-center gap-2">
                  <span>🔒</span> 3.2 Cambiar Contraseña
                </h4>
                <form onsubmit="alert('Contraseña cambiada con éxito'); return false;" class="space-y-3 text-xs">
                  <div>
                    <label class="block font-semibold text-slate-600 mb-1">Contraseña Actual</label>
                    <input type="password" value="********" class="w-full px-3 py-2 border border-slate-300 rounded-lg outline-none">
                  </div>
                  <div>
                    <label class="block font-semibold text-slate-600 mb-1">Nueva Contraseña</label>
                    <input type="password" placeholder="Mínimo 8 caracteres" class="w-full px-3 py-2 border border-slate-300 rounded-lg outline-none">
                  </div>
                  <button type="submit" class="px-4 py-2 bg-red-800 text-white rounded-lg font-bold">Actualizar Contraseña</button>
                </form>
              </div>
            </div>
          </div>
        </div>

      </main>
    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- 3. PERFIL: ADMINISTRADOR (PANEL DE GESTIÓN INTEGRAL CON ESTADÍSTICAS) -->
  <!-- ========================================================================= -->
  <div id="profile-admin" class="flex-1 flex flex-col hidden bg-slate-100">

    <!-- Header Administrador -->
    <header class="bg-slate-900 border-b border-red-700 py-3 px-6 sticky top-12 z-30 shadow-md flex items-center justify-between text-white">
      <div class="flex items-center gap-3">
        <span class="w-9 h-9 rounded-lg bg-red-700 text-amber-300 font-serif font-black flex items-center justify-center text-sm border border-amber-400">ADM</span>
        <div>
          <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">PANEL DE ADMINISTRACIÓN</span>
          <div class="text-base font-bold text-white leading-tight">Administrador: Tuno Mayor Javier</div>
        </div>
      </div>

      <div class="flex items-center gap-3">
        <span class="px-2.5 py-1 bg-red-800/80 text-amber-300 border border-amber-400/40 rounded-md text-xs font-bold">Rol: SuperAdmin</span>
        <button onclick="switchProfile('visitante')" class="px-3 py-1.5 rounded-lg border border-slate-700 hover:bg-slate-800 text-slate-300 text-xs font-semibold">
          Salir al Portal
        </button>
      </div>
    </header>

    <!-- Layout Admin: Sidebar de los 7 Nodos + Contenido -->
    <div class="max-w-7xl mx-auto w-full px-4 py-8 flex-1 grid lg:grid-cols-4 gap-8">
      
      <!-- Menú Lateral Admin según Árbol: 0 a 7 -->
      <aside class="space-y-2">
        <div class="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-1">
          <div class="text-[11px] font-bold text-slate-400 uppercase px-3 py-1">Módulos Administrativos</div>
          
          <button onclick="showAdminSection('admin-dashboard')" id="btn-adm-dash" class="admin-menu-item active w-full text-left px-3 py-2.5 rounded-xl text-xs font-bold flex items-center gap-2 transition">
            <span>📊</span> 0. Estadísticas Generales
          </button>
          
          <button onclick="showAdminSection('admin-contratos')" id="btn-adm-contratos" class="admin-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>📜</span> 1. Gestionar Contratos
          </button>
          
          <button onclick="showAdminSection('admin-clientes')" id="btn-adm-clientes" class="admin-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>👥</span> 2. Cartera de Clientes
          </button>
          
          <button onclick="showAdminSection('admin-pedidos')" id="btn-adm-pedidos" class="admin-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>📦</span> 3. Pedidos de la Tienda
          </button>
          
          <button onclick="showAdminSection('admin-productos')" id="btn-adm-productos" class="admin-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>🛍️</span> 4. Productos de la Tienda
          </button>
          
          <button onclick="showAdminSection('admin-miembros')" id="btn-adm-miembros" class="admin-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>🎸</span> 5. Lista de Miembros
          </button>
          
          <button onclick="showAdminSection('admin-cuenta')" id="btn-adm-cuenta" class="admin-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>🔑</span> 6. Gestionar Cuenta
          </button>
          
          <button onclick="showAdminSection('admin-certamenes')" id="btn-adm-certamenes" class="admin-menu-item w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 flex items-center gap-2 transition">
            <span>🏆</span> 7. Gestionar Certámenes
          </button>
        </div>
      </aside>

      <!-- Contenido Principal Admin -->
      <main class="lg:col-span-3">

        <!-- 0. PANEL CON ESTADÍSTICAS (según wireframe admin/index.html) -->
        <div id="admin-dashboard" class="admin-subview space-y-6">
          <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
              <span class="text-xs text-slate-500 font-bold uppercase">Contratos Pendientes</span>
              <div class="text-3xl font-black text-red-700 mt-2">4</div>
              <span class="text-[11px] text-green-600 font-semibold">↑ +2 esta semana</span>
            </div>
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
              <span class="text-xs text-slate-500 font-bold uppercase">Pedidos Tienda</span>
              <div class="text-3xl font-black text-slate-900 mt-2">7</div>
              <span class="text-[11px] text-amber-600 font-semibold">3 por empaquetar</span>
            </div>
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
              <span class="text-xs text-slate-500 font-bold uppercase">Ingresos del Mes</span>
              <div class="text-3xl font-black text-emerald-700 mt-2">1.840 €</div>
              <span class="text-[11px] text-slate-400">Contratos + Merchandising</span>
            </div>
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
              <span class="text-xs text-slate-500 font-bold uppercase">Clientes Nuevos</span>
              <div class="text-3xl font-black text-blue-700 mt-2">12</div>
              <span class="text-[11px] text-slate-400">En el último mes</span>
            </div>
          </div>

          <!-- Gráficos de barras según wireframe admin/index.html -->
          <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
              <h4 class="font-bold text-slate-900 text-sm mb-4">Contratos por Mes (Últimos 12 meses)</h4>
              <div class="flex items-end gap-2 h-40 border-b border-slate-300 pb-2 px-2">
                <div class="flex-1 bg-red-200 rounded-t h-[40%] hover:bg-red-400 transition" title="Ene: 4"></div>
                <div class="flex-1 bg-red-200 rounded-t h-[55%] hover:bg-red-400 transition" title="Feb: 6"></div>
                <div class="flex-1 bg-red-200 rounded-t h-[35%] hover:bg-red-400 transition" title="Mar: 3"></div>
                <div class="flex-1 bg-red-200 rounded-t h-[70%] hover:bg-red-400 transition" title="Abr: 8"></div>
                <div class="flex-1 bg-red-300 rounded-t h-[60%] hover:bg-red-400 transition" title="May: 7"></div>
                <div class="flex-1 bg-red-500 rounded-t h-[80%] hover:bg-red-600 transition" title="Jun: 10"></div>
                <div class="flex-1 bg-red-600 rounded-t h-[95%] hover:bg-red-700 transition" title="Jul: 12"></div>
                <div class="flex-1 bg-red-600 rounded-t h-[90%] hover:bg-red-700 transition" title="Ago: 11"></div>
                <div class="flex-1 bg-red-400 rounded-t h-[75%] hover:bg-red-500 transition" title="Sep: 9"></div>
                <div class="flex-1 bg-red-300 rounded-t h-[50%] hover:bg-red-400 transition" title="Oct: 5"></div>
                <div class="flex-1 bg-red-200 rounded-t h-[40%] hover:bg-red-400 transition" title="Nov: 4"></div>
                <div class="flex-1 bg-red-400 rounded-t h-[65%] hover:bg-red-500 transition" title="Dic: 7"></div>
              </div>
              <div class="flex justify-between text-[10px] text-slate-400 mt-2 font-mono">
                <span>Ene</span><span>Jun</span><span>Dic</span>
              </div>
            </div>

            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
              <h4 class="font-bold text-slate-900 text-sm mb-4">Ventas Tienda por Mes</h4>
              <div class="flex items-end gap-2 h-40 border-b border-slate-300 pb-2 px-2">
                <div class="flex-1 bg-amber-200 rounded-t h-[30%] hover:bg-amber-400 transition"></div>
                <div class="flex-1 bg-amber-200 rounded-t h-[45%] hover:bg-amber-400 transition"></div>
                <div class="flex-1 bg-amber-200 rounded-t h-[60%] hover:bg-amber-400 transition"></div>
                <div class="flex-1 bg-amber-300 rounded-t h-[40%] hover:bg-amber-400 transition"></div>
                <div class="flex-1 bg-amber-300 rounded-t h-[55%] hover:bg-amber-400 transition"></div>
                <div class="flex-1 bg-amber-400 rounded-t h-[70%] hover:bg-amber-500 transition"></div>
                <div class="flex-1 bg-amber-500 rounded-t h-[65%] hover:bg-amber-600 transition"></div>
                <div class="flex-1 bg-amber-300 rounded-t h-[50%] hover:bg-amber-400 transition"></div>
                <div class="flex-1 bg-amber-400 rounded-t h-[60%] hover:bg-amber-500 transition"></div>
                <div class="flex-1 bg-amber-500 rounded-t h-[80%] hover:bg-amber-600 transition"></div>
                <div class="flex-1 bg-amber-500 rounded-t h-[70%] hover:bg-amber-600 transition"></div>
                <div class="flex-1 bg-amber-600 rounded-t h-[95%] hover:bg-amber-700 transition"></div>
              </div>
              <div class="flex justify-between text-[10px] text-slate-400 mt-2 font-mono">
                <span>Ene</span><span>Jun</span><span>Dic (Pico Navidad)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 1. GESTIONAR CONTRATOS (Nodo 1 y 1.1) -->
        <div id="admin-contratos" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-red-700 uppercase">Nodo 1</span>
            <h3 class="text-xl font-bold text-slate-900 mb-4">Gestión Central de Contratos de Actuación</h3>
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-50 text-slate-500 uppercase font-bold border-b border-slate-200">
                <tr>
                  <th class="py-3 px-4">Contrato</th>
                  <th class="py-3 px-4">Cliente</th>
                  <th class="py-3 px-4">Teléfono</th>
                  <th class="py-3 px-4">Evento</th>
                  <th class="py-3 px-4">Estado</th>
                  <th class="py-3 px-4 text-right">Detalle (1.1)</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr>
                  <td class="py-3 px-4 font-bold">#CTR-042</td>
                  <td class="py-3 px-4">José Manuel Martínez</td>
                  <td class="py-3 px-4 font-mono">612 345 678</td>
                  <td class="py-3 px-4">Boda Roquetas</td>
                  <td class="py-3 px-4"><span class="px-2 py-0.5 rounded-full bg-green-100 text-green-800 font-bold">Aceptado</span></td>
                  <td class="py-3 px-4 text-right">
                    <button onclick="alert('Nodo 1.1 Ver Contrato en Detalle:\\n\\nCliente: José Manuel Martínez\\nFecha: 18/07/2026\\nPresupuesto: 450 €\\nTunos asignados: 12');" class="text-red-700 font-bold hover:underline">Ver Ficha</button>
                  </td>
                </tr>
                <tr>
                  <td class="py-3 px-4 font-bold">#CTR-043</td>
                  <td class="py-3 px-4">Colegio de Abogados Almería</td>
                  <td class="py-3 px-4 font-mono">950 123 456</td>
                  <td class="py-3 px-4">Gala Anual</td>
                  <td class="py-3 px-4"><span class="px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 font-bold">Pendiente</span></td>
                  <td class="py-3 px-4 text-right">
                    <button onclick="alert('Nodo 1.1: Ficha de contrato pendiente.');" class="text-red-700 font-bold hover:underline">Ver Ficha</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 2. GESTIONAR CARTERA DE CLIENTES (Nodo 2, 2.1, 2.1.1, 2.1.2) -->
        <div id="admin-clientes" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-red-700 uppercase">Nodo 2</span>
            <h3 class="text-xl font-bold text-slate-900 mb-4">Cartera de Clientes Registrados</h3>
            <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 flex items-center justify-between">
              <div>
                <span class="text-xs font-bold text-slate-500">Nodo 2.1 Ficha de Cliente</span>
                <div class="font-bold text-slate-900 text-sm mt-0.5">José Manuel Martínez (cliente@almeria.es)</div>
                <div class="text-xs text-slate-500">Registrado desde 2025 · Almería</div>
              </div>
              <div class="flex gap-2">
                <button onclick="alert('Nodo 2.1.1: Ver Contratos del cliente José Manuel (Total: 2 contratos)');" class="px-3 py-1.5 bg-slate-900 text-white rounded-lg text-xs font-bold">2.1.1 Contratos</button>
                <button onclick="alert('Nodo 2.1.2: Ver Pedidos del cliente José Manuel (Total: 1 pedido tienda)');" class="px-3 py-1.5 bg-red-800 text-white rounded-lg text-xs font-bold">2.1.2 Pedidos</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. GESTIONAR PEDIDOS DE LA TIENDA (Nodo 3 y 3.1) -->
        <div id="admin-pedidos" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-red-700 uppercase">Nodo 3</span>
            <h3 class="text-xl font-bold text-slate-900 mb-4">Pedidos de la Tienda de la Tuna</h3>
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-50 text-slate-500 uppercase font-bold border-b border-slate-200">
                <tr>
                  <th class="py-3 px-4">Nº Pedido</th>
                  <th class="py-3 px-4">Cliente</th>
                  <th class="py-3 px-4">Artículos</th>
                  <th class="py-3 px-4">Total</th>
                  <th class="py-3 px-4">Estado</th>
                  <th class="py-3 px-4 text-right">Detalle (3.1)</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr>
                  <td class="py-3 px-4 font-bold">#PED-894</td>
                  <td class="py-3 px-4">José Manuel Martínez</td>
                  <td class="py-3 px-4">1x Sudadera (L), 1x Parche Beca</td>
                  <td class="py-3 px-4 font-bold">34,50 €</td>
                  <td class="py-3 px-4"><span class="px-2 py-0.5 rounded-full bg-blue-100 text-blue-800 font-bold">Enviado</span></td>
                  <td class="py-3 px-4 text-right">
                    <button onclick="alert('Nodo 3.1 Detalle de Pedido:\\n\\nDirección: Avda del Mediterráneo 120, Almería\\nTracking: ES983748291\\nTotal pagado: 34,50 € (Tarjeta)');" class="text-red-700 font-bold hover:underline">Ver Detalle</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 4. GESTIONAR PRODUCTOS DE LA TIENDA (Nodo 4, 4.1, 4.2) -->
        <div id="admin-productos" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div>
                <span class="text-xs font-bold text-red-700 uppercase">Nodo 4</span>
                <h3 class="text-xl font-bold text-slate-900">Catálogo de Productos y Merchandising</h3>
              </div>
              <button onclick="alert('Nodo 4.1: Modal Añadir Nuevo Producto (Nombre, precio, stock, foto, tallas)');" class="px-3 py-1.5 bg-red-800 text-white rounded-lg text-xs font-bold">
                + 4.1 Añadir Producto
              </button>
            </div>

            <div class="divide-y divide-slate-100 text-xs">
              <div class="py-3 flex items-center justify-between">
                <div>
                  <span class="font-bold text-slate-900 text-sm">Sudadera Roja Tuna de Derecho</span>
                  <div class="text-slate-500">Precio: 28,00 € · Stock: 42 unidades</div>
                </div>
                <button onclick="alert('Nodo 4.2: Modificar o Eliminar este producto');" class="text-blue-700 font-bold hover:underline">4.2 Modificar / Eliminar</button>
              </div>
              <div class="py-3 flex items-center justify-between">
                <div>
                  <span class="font-bold text-slate-900 text-sm">CD "25 Años de Ronda"</span>
                  <div class="text-slate-500">Precio: 12,00 € · Stock: 80 unidades</div>
                </div>
                <button onclick="alert('Nodo 4.2: Modificar o Eliminar este producto');" class="text-blue-700 font-bold hover:underline">4.2 Modificar / Eliminar</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 5. GESTIONAR LISTA DE MIEMBROS (Nodo 5, 5.1, 5.2) -->
        <div id="admin-miembros" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div>
                <span class="text-xs font-bold text-red-700 uppercase">Nodo 5</span>
                <h3 class="text-xl font-bold text-slate-900">Lista Oficial de Miembros de la Tuna</h3>
              </div>
              <button onclick="alert('Nodo 5.2: Añadir nuevo miembro / novato a la plantilla oficial');" class="px-3 py-1.5 bg-red-800 text-white rounded-lg text-xs font-bold">
                + 5.2 Añadir Nuevo Miembro
              </button>
            </div>

            <div class="divide-y divide-slate-100 text-xs">
              <div class="py-3 flex items-center justify-between">
                <div>
                  <span class="font-bold text-slate-900">Javier "El Jurisconsulto"</span>
                  <div class="text-slate-500">Rango: Tuno Mayor · Instrumento: Bandurria</div>
                </div>
                <button onclick="alert('Nodo 5.1: Modificar o eliminar miembro existente');" class="text-blue-700 font-bold hover:underline">5.1 Modificar / Baja</button>
              </div>
              <div class="py-3 flex items-center justify-between">
                <div>
                  <span class="font-bold text-slate-900">Carlos "El Pasante"</span>
                  <div class="text-slate-500">Rango: Novato · Instrumento: Pandereta</div>
                </div>
                <button onclick="alert('Nodo 5.1: Modificar o ascender a Tuno');" class="text-blue-700 font-bold hover:underline">5.1 Modificar / Ascenso</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 6. GESTIONAR CUENTA ADMIN (Nodo 6, 6.1, 6.2) -->
        <div id="admin-cuenta" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <span class="text-xs font-bold text-red-700 uppercase">Nodo 6</span>
            <h3 class="text-xl font-bold text-slate-900 mb-4">Cuenta de Administrador</h3>
            <div class="space-y-4 text-xs">
              <div class="p-4 rounded-xl border border-slate-200">
                <span class="font-bold text-slate-800 block mb-1">6.1 Modificar Información Personal</span>
                <p class="text-slate-500 mb-2">Administrador actual: Tuno Mayor Javier (tuna.derecho.almeria@gmail.com)</p>
                <button onclick="alert('Nodo 6.1: Datos de admin actualizados');" class="px-3 py-1.5 bg-slate-900 text-white rounded-lg font-bold">Guardar Cambios</button>
              </div>
              <div class="p-4 rounded-xl border border-slate-200">
                <span class="font-bold text-slate-800 block mb-1">6.2 Cambiar Contraseña del Administrador</span>
                <button onclick="alert('Nodo 6.2: Contraseña de administrador actualizada');" class="px-3 py-1.5 bg-red-800 text-white rounded-lg font-bold">Cambiar Contraseña</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 7. GESTIONAR CERTÁMENES (Nodo 7, 7.1, 7.2) -->
        <div id="admin-certamenes" class="admin-subview hidden space-y-6">
          <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div>
                <span class="text-xs font-bold text-red-700 uppercase">Nodo 7</span>
                <h3 class="text-xl font-bold text-slate-900">Gestión de Certámenes y Festivales</h3>
              </div>
              <button onclick="alert('Nodo 7.2: Formulario de Creación de Nuevo Certamen (Ciudad, fecha, premios ganados, fotos)');" class="px-3 py-1.5 bg-red-800 text-white rounded-lg text-xs font-bold">
                + 7.2 Crear Nuevo Certamen
              </button>
            </div>

            <div class="space-y-3 text-xs">
              <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 flex items-center justify-between">
                <div>
                  <span class="font-bold text-slate-900 text-sm">Certamen Nacional de Tunas de Derecho</span>
                  <div class="text-slate-500">Lugar: Salamanca · Fecha: Noviembre 2024 · Premios: 1º Mejor Tuna</div>
                </div>
                <button onclick="alert('Nodo 7.1: Modificar o eliminar este certamen');" class="text-blue-700 font-bold hover:underline">7.1 Editar Certamen</button>
              </div>
            </div>
          </div>
        </div>

      </main>
    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- FOOTER CORPORATIVO CON CONTACTO ULTRA-VISIBLE -->
  <!-- ========================================================================= -->
  <footer class="bg-slate-950 text-white border-t-4 border-amber-500 mt-auto pt-12 pb-8">
    <div class="max-w-7xl mx-auto px-4 grid md:grid-cols-4 gap-8 mb-8 text-xs">
      
      <!-- Columna 1: Marca & Lema -->
      <div>
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-full bg-red-800 text-amber-300 font-serif font-black flex items-center justify-center text-lg border border-amber-400">TD</div>
          <div>
            <div class="font-serif font-black text-sm text-amber-300">TUNA DE DERECHO</div>
            <div class="text-[10px] text-slate-400">Universidad de Almería</div>
          </div>
        </div>
        <p class="text-slate-400 leading-relaxed mb-4">
          Tradición estudiantil, música y alegría desde 1995. Amenizamos tus momentos más especiales por toda España.
        </p>
        <div class="p-2.5 rounded-lg bg-red-950/80 border border-red-800 text-amber-300 text-[11px] font-bold">
          Color Corporativo: Rojo Derecho (#B91C1C)
        </div>
      </div>

      <!-- Columna 2: CONTACTO PRINCIPAL (ULTRA-VISIBLE) -->
      <div class="p-4 rounded-xl bg-red-950 border border-amber-500/50">
        <h4 class="font-bold text-amber-300 uppercase tracking-wider mb-3 text-sm">📞 CONTACTO INMEDIATO</h4>
        <div class="space-y-3">
          <div>
            <div class="text-[10px] uppercase text-slate-400 font-bold">Teléfono / Contrataciones:</div>
            <a href="tel:+34600123456" class="text-base font-black text-white hover:text-amber-300 transition block">+34 600 123 456</a>
          </div>
          <div>
            <div class="text-[10px] uppercase text-slate-400 font-bold">Correo Electrónico:</div>
            <a href="mailto:tuna.derecho.almeria@gmail.com" class="text-xs text-slate-200 hover:text-amber-300 transition block">tuna.derecho.almeria@gmail.com</a>
          </div>
          <div>
            <div class="text-[10px] uppercase text-slate-400 font-bold">Dirección de Ensayo:</div>
            <span class="text-xs text-slate-300 block">Facultad de Derecho, Planta Baja · Univ. de Almería</span>
          </div>
        </div>
      </div>

      <!-- Columna 3: REDES SOCIALES OFICIALES -->
      <div>
        <h4 class="font-bold text-amber-300 uppercase tracking-wider mb-3 text-sm">🌐 SÍGUENOS EN REDES</h4>
        <div class="space-y-2">
          <a href="https://instagram.com" target="_blank" class="flex items-center gap-2 text-slate-300 hover:text-amber-300 transition">
            <span class="text-pink-500">●</span> Instagram: <strong>@tunaderechoalmeria</strong>
          </a>
          <a href="https://tiktok.com" target="_blank" class="flex items-center gap-2 text-slate-300 hover:text-amber-300 transition">
            <span class="text-white">●</span> TikTok: <strong>@tunaderechoual</strong>
          </a>
          <a href="https://facebook.com" target="_blank" class="flex items-center gap-2 text-slate-300 hover:text-amber-300 transition">
            <span class="text-blue-500">●</span> Facebook: <strong>/TunaDerechoAlmeria</strong>
          </a>
          <a href="https://youtube.com" target="_blank" class="flex items-center gap-2 text-slate-300 hover:text-amber-300 transition">
            <span class="text-red-500">●</span> YouTube: <strong>@TunaDerechoUAL</strong>
          </a>
          <a href="https://spotify.com" target="_blank" class="flex items-center gap-2 text-slate-300 hover:text-amber-300 transition">
            <span class="text-green-500">●</span> Spotify: <strong>Tuna Derecho Almería</strong>
          </a>
        </div>
      </div>

      <!-- Columna 4: NAVEGACIÓN RÁPIDA DE ÁRBOL -->
      <div>
        <h4 class="font-bold text-amber-300 uppercase tracking-wider mb-3 text-sm">MAPA DEL SITIO</h4>
        <ul class="space-y-1.5 text-slate-400">
          <li><button onclick="switchProfile('visitante'); showVisitanteSection('visitante-conoce');" class="hover:text-white">1. Conoce la Tuna (Historia/Miembros)</button></li>
          <li><button onclick="switchProfile('visitante'); showVisitanteSection('visitante-contratacion');" class="hover:text-white">2. Contratación de Servicios</button></li>
          <li><button onclick="switchProfile('visitante'); showVisitanteSection('visitante-multimedia');" class="hover:text-white">3. Multimedia & Certámenes</button></li>
          <li><button onclick="switchProfile('visitante'); showVisitanteSection('visitante-tienda');" class="hover:text-amber-300 font-bold text-slate-200">4. Tienda Oficial de la Tuna</button></li>
          <li><button onclick="switchProfile('visitante'); showVisitanteSection('visitante-cancionero');" class="hover:text-white">5. Cancionero & Spotify</button></li>
          <li><button onclick="switchProfile('visitante'); showVisitanteSection('visitante-unete');" class="hover:text-white">6. Únete a Nosotros</button></li>
          <li><button onclick="switchProfile('visitante'); showVisitanteSection('visitante-acceso');" class="hover:text-white">7. Acceso a Cuenta</button></li>
        </ul>
      </div>

    </div>

    <!-- Copyright -->
    <div class="max-w-7xl mx-auto px-4 pt-6 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-500">
      <div>© 2026 Tuna de la Facultad de Derecho de Almería. Todos los derechos reservados.</div>
      <div class="flex gap-4">
        <span>Aviso Legal</span>
        <span>Política de Privacidad</span>
        <span>Cookies</span>
      </div>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- BOTÓN FLOTANTE PERMANENTE DE WHATSAPP -->
  <!-- ========================================================================= -->
  <a href="https://wa.me/34600123456" target="_blank" class="fixed bottom-6 right-6 z-50 flex items-center gap-2.5 px-4 py-3 rounded-full bg-green-600 hover:bg-green-500 text-white font-bold text-xs shadow-2xl transition hover:scale-105 border-2 border-white pulse-call" title="WhatsApp Directo con la Tuna">
    <svg class="w-6 h-6 fill-white" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347m-5.421 7.403"/></svg>
    <span class="hidden sm:inline">WhatsApp Tuna: +34 600 123 456</span>
  </a>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT DE INTERACTIVIDAD PARA SWITCH ENTRE PERFILES Y SUBVISTAS -->
  <!-- ========================================================================= -->
  <script>
    // 1. Selector de perfil principal
    function switchProfile(profile) {
      // Ocultar todos los perfiles
      document.getElementById('profile-visitante').classList.add('hidden');
      document.getElementById('profile-cliente').classList.add('hidden');
      document.getElementById('profile-admin').classList.add('hidden');

      // Desactivar botones de tabs
      document.getElementById('tab-btn-visitante').classList.remove('active');
      document.getElementById('tab-btn-cliente').classList.remove('active');
      document.getElementById('tab-btn-admin').classList.remove('active');

      // Mostrar perfil elegido
      if (profile === 'visitante') {
        document.getElementById('profile-visitante').classList.remove('hidden');
        document.getElementById('tab-btn-visitante').classList.add('active');
      } else if (profile === 'cliente') {
        document.getElementById('profile-cliente').classList.remove('hidden');
        document.getElementById('tab-btn-cliente').classList.add('active');
      } else if (profile === 'admin') {
        document.getElementById('profile-admin').classList.remove('hidden');
        document.getElementById('tab-btn-admin').classList.add('active');
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // 2. Navegación entre secciones de Visitante
    function showVisitanteSection(sectionId) {
      document.querySelectorAll('.visitante-subview').forEach(el => el.classList.add('hidden'));
      const target = document.getElementById(sectionId);
      if (target) {
        target.classList.remove('hidden');
        window.scrollTo({ top: 120, behavior: 'smooth' });
      }
    }

    // 3. Navegación entre secciones de Cliente
    function showClientSection(sectionId) {
      document.querySelectorAll('.client-subview').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.client-menu-item').forEach(el => el.classList.remove('active'));
      
      const target = document.getElementById(sectionId);
      if (target) {
        target.classList.remove('hidden');
      }
      // Marcar botón activo
      if (sectionId === 'cliente-dashboard') document.getElementById('btn-c-dash').classList.add('active');
      if (sectionId === 'cliente-contratos') document.getElementById('btn-c-contratos').classList.add('active');
      if (sectionId === 'cliente-pedidos') document.getElementById('btn-c-pedidos').classList.add('active');
      if (sectionId === 'cliente-cuenta') document.getElementById('btn-c-cuenta').classList.add('active');
    }

    // 4. Navegación entre secciones de Admin
    function showAdminSection(sectionId) {
      document.querySelectorAll('.admin-subview').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.admin-menu-item').forEach(el => el.classList.remove('active'));
      
      const target = document.getElementById(sectionId);
      if (target) {
        target.classList.remove('hidden');
      }
      // Marcar botón activo
      if (sectionId === 'admin-dashboard') document.getElementById('btn-adm-dash').classList.add('active');
      if (sectionId === 'admin-contratos') document.getElementById('btn-adm-contratos').classList.add('active');
      if (sectionId === 'admin-clientes') document.getElementById('btn-adm-clientes').classList.add('active');
      if (sectionId === 'admin-pedidos') document.getElementById('btn-adm-pedidos').classList.add('active');
      if (sectionId === 'admin-productos') document.getElementById('btn-adm-productos').classList.add('active');
      if (sectionId === 'admin-miembros') document.getElementById('btn-adm-miembros').classList.add('active');
      if (sectionId === 'admin-cuenta') document.getElementById('btn-adm-cuenta').classList.add('active');
      if (sectionId === 'admin-certamenes') document.getElementById('btn-adm-certamenes').classList.add('active');
    }

    // 5. Carrito de Compras Mockup
    let cartCount = 2;
    function addToCart(productName, price) {
      cartCount++;
      document.getElementById('cart-counter').textContent = cartCount;
      document.getElementById('shop-cart-badge').textContent = cartCount;
      alert('¡Añadido a la cesta! ' + productName + ' (' + price.toFixed(2) + ' €). Total artículos en cesta: ' + cartCount);
    }

    // 6. Filtros multimedia mock
    function filterMedia(type) {
      alert('Filtro multimedia aplicado: ' + type);
    }
  </script>
</body>
</html>
"""

dest1 = r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\mockup-tuna-derecho-almeria.html"
dest2 = r"C:\Users\joses\.gemini\antigravity\brain\36451285-1c1b-4cee-abfe-e4f0f4417009\mockup-tuna-derecho-almeria.html"

with open(dest1, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Escrito en {dest1}")

with open(dest2, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Escrito en {dest2}")

print("Completado con éxito.")

