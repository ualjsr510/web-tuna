# -*- coding: utf-8 -*-
"""
Generador del Índice Principal de Mockups (mockup/index.html)
Presenta con máxima elegancia corporativa los 3 perfiles de usuario:
1. Visitante (visitante.html)
2. Cliente (cliente.html)
3. Administrador (admin.html)
"""

def get_index_html():
    return """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuna de la Facultad de Derecho de Almería · Mockups Oficiales</title>
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
      letter-spacing: 0.2em;
      text-transform: uppercase;
      font-size: 0.7rem;
      font-weight: 700;
    }
    .hero-salamanca {
      background: linear-gradient(180deg, #180505 0%, #3B0A0A 60%, #5C0E0E 100%);
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

  <!-- BARRA DE CONTACTO CORPORATIVA SUPERIOR -->
  <div class="bg-[#5C0000] text-white border-b-2 border-[#D4AF37] py-2.5 px-4 text-xs shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex flex-wrap items-center gap-4 sm:gap-6">
        <a href="tel:+34600123456" class="flex items-center gap-2 font-black text-sm text-amber-300 hover:text-amber-200 transition">
          <span class="p-1 bg-red-950 rounded-full">📞</span>
          TELÉFONOS OFICIALES: +34 600 123 456 · +34 612 345 678
        </a>
        <a href="mailto:tuna.derecho.almeria@gmail.com" class="flex items-center gap-1.5 text-slate-200 hover:text-amber-300 transition">
          <span>✉️</span> tuna.derecho.almeria@gmail.com
        </a>
      </div>

      <div class="flex items-center gap-2 sm:gap-3">
        <span class="badge-editorial text-amber-300 hidden md:inline">Redes Oficiales:</span>
        <a href="https://instagram.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-pink-700 transition text-[11px] font-bold text-white">Instagram</a>
        <a href="https://tiktok.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-black transition text-[11px] font-bold text-white">TikTok</a>
        <a href="https://facebook.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-blue-700 transition text-[11px] font-bold text-white">Facebook</a>
        <a href="https://spotify.com" target="_blank" class="px-2 py-0.5 rounded bg-red-950 hover:bg-green-700 transition text-[11px] font-bold text-white">Spotify</a>
      </div>
    </div>
  </div>

  <!-- CABECERA PRINCIPAL -->
  <header class="bg-white border-b border-stone-200 shadow-sm py-4 px-6">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-12 h-12 rounded-full bg-[#8B0000] border-2 border-[#D4AF37] flex items-center justify-center text-amber-300 font-serif-tuna font-black text-xl shadow">
          TD
        </div>
        <div>
          <div class="font-serif-tuna font-black text-xl text-[#5C0000] leading-none">TUNA DE LA FACULTAD DE DERECHO</div>
          <div class="badge-editorial text-[#8B0000] text-[9px] mt-1 font-bold">Universidad de Almería · Beca Roja · Desde 1995</div>
        </div>
      </div>

      <div class="hidden sm:flex items-center gap-2 text-xs">
        <span class="text-stone-500">Inspiración estética:</span>
        <a href="https://tunasalamanca.com/" target="_blank" class="px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-800 font-bold rounded border border-stone-300">
          tunasalamanca.com ↗
        </a>
      </div>
    </div>
  </header>

  <!-- HERO DE PRESENTACIÓN DE LOS 3 MOCKUPS -->
  <section class="hero-salamanca text-white py-16 px-4 text-center border-b-2 border-[#D4AF37]">
    <div class="max-w-4xl mx-auto">
      <span class="badge-editorial text-[#D4AF37] mb-2 block">PROTOTIPOS DE ALTA FIDELIDAD (MOCKUPS FINALES)</span>
      <h1 class="text-4xl sm:text-6xl font-serif-tuna font-normal text-stone-100 leading-tight">
        Los 3 Perfiles de Usuario<br>
        <span class="italic text-amber-200">Fieles a los Árboles de Contenido y Wireframes</span>
      </h1>
      <p class="text-stone-300 text-sm sm:text-base mt-4 max-w-2xl mx-auto font-light leading-relaxed">
        Selecciona cualquiera de los 3 mockups para explorar la interfaz completa de cada perfil con todos sus componentes funcionales, datos reales y diseño editorial en rojo corporativo.
      </p>
    </div>
  </section>

  <!-- GRID DE ACCESO A LOS 3 MOCKUPS -->
  <main class="flex-1 max-w-7xl mx-auto w-full p-6 sm:p-10">
    <div class="grid md:grid-cols-3 gap-8">
      
      <!-- CARD 1: VISITANTE -->
      <div class="bg-white rounded-2xl border-2 border-stone-200 hover:border-[#8B0000] transition shadow-lg flex flex-col justify-between overflow-hidden group">
        <div>
          <div class="bg-gradient-to-r from-red-950 to-red-800 text-amber-200 p-6 border-b border-amber-600/40">
            <span class="text-4xl block mb-2 group-hover:scale-110 transition origin-left">🌐</span>
            <span class="badge-editorial text-[#D4AF37]">PERFIL PÚBLICO</span>
            <h2 class="font-serif-tuna font-bold text-2xl text-white mt-1">1. Visitante</h2>
            <p class="text-stone-300 text-xs mt-1">26 Pantallas del Árbol de Contenidos</p>
          </div>

          <div class="p-6 text-xs text-stone-600 space-y-3">
            <p>Portal web abierto al público para conocer la tuna y contratar actuaciones:</p>
            <ul class="space-y-1.5 list-disc pl-4 text-stone-700">
              <li><strong>0. Portada:</strong> Hero estilo Salamanca con lema y franja de hitos.</li>
              <li><strong>1. Conoce la Tuna:</strong> 1.1 Historia y 1.2 Miembros.</li>
              <li><strong>2. Contratación:</strong> 2.1.1 Formulario oficial de petición.</li>
              <li><strong>3. Multimedia:</strong> 3.1.1 Vídeos, 3.1.2 Fotos y 3.2 Certámenes.</li>
              <li><strong>4. Tienda:</strong> ⭐ 4.1 Catálogo interactivo con filtros, 4.2 Cesta y 4.2.1.1 Pasarela de pago/envío.</li>
              <li><strong>5. Cancionero:</strong> Letras de ronda y widget de Spotify.</li>
              <li><strong>6. Únete:</strong> Formulario de novatos y local de ensayo UAL.</li>
              <li><strong>7. Acceso:</strong> Login, registro y recuperación de clave.</li>
            </ul>
          </div>
        </div>

        <div class="p-6 pt-0">
          <a href="visitante.html" class="w-full py-3 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded-xl text-xs uppercase tracking-wider text-center block shadow transition border border-[#D4AF37]">
            Abrir Mockup Visitante →
          </a>
        </div>
      </div>

      <!-- CARD 2: CLIENTE -->
      <div class="bg-white rounded-2xl border-2 border-stone-200 hover:border-[#8B0000] transition shadow-lg flex flex-col justify-between overflow-hidden group">
        <div>
          <div class="bg-gradient-to-r from-stone-900 to-red-950 text-amber-200 p-6 border-b border-amber-600/40">
            <span class="text-4xl block mb-2 group-hover:scale-110 transition origin-left">👤</span>
            <span class="badge-editorial text-[#D4AF37]">ÁREA PRIVADA</span>
            <h2 class="font-serif-tuna font-bold text-2xl text-white mt-1">2. Cliente</h2>
            <p class="text-stone-300 text-xs mt-1">10 Pantallas del Árbol de Contenidos</p>
          </div>

          <div class="p-6 text-xs text-stone-600 space-y-3">
            <p>Área privada del usuario registrado para gestionar sus eventos y compras:</p>
            <ul class="space-y-1.5 list-disc pl-4 text-stone-700">
              <li><strong>0. Inicio Cliente:</strong> Saludo personalizado y accesos rápidos.</li>
              <li><strong>1. Contratos:</strong> Historial de actuaciones solicitadas.</li>
              <li><strong>1.1 Detalle Contrato:</strong> Ficha formal con repertorio e importe.</li>
              <li><strong>2. Pedidos:</strong> Compras realizadas en la tienda.</li>
              <li><strong>2.1 Detalle Pedido:</strong> Estado de entrega y seguimiento.</li>
              <li><strong>2.1.1 Editar Pedido:</strong> Modificar dirección de envío.</li>
              <li><strong>2.1.2 Tramitar Devolución:</strong> Formulario de cambio/reembolso.</li>
              <li><strong>3. Cuenta:</strong> 3.1 Datos personales y 3.2 Cambiar contraseña.</li>
            </ul>
          </div>
        </div>

        <div class="p-6 pt-0">
          <a href="cliente.html" class="w-full py-3 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded-xl text-xs uppercase tracking-wider text-center block shadow transition border border-[#D4AF37]">
            Abrir Mockup Cliente →
          </a>
        </div>
      </div>

      <!-- CARD 3: ADMINISTRADOR -->
      <div class="bg-white rounded-2xl border-2 border-stone-200 hover:border-[#8B0000] transition shadow-lg flex flex-col justify-between overflow-hidden group">
        <div>
          <div class="bg-gradient-to-r from-stone-950 to-stone-900 text-amber-200 p-6 border-b border-amber-600/40">
            <span class="text-4xl block mb-2 group-hover:scale-110 transition origin-left">⚙️</span>
            <span class="badge-editorial text-[#D4AF37]">PANEL DE GESTIÓN</span>
            <h2 class="font-serif-tuna font-bold text-2xl text-white mt-1">3. Administrador</h2>
            <p class="text-stone-300 text-xs mt-1">21 Pantallas del Árbol de Contenidos</p>
          </div>

          <div class="p-6 text-xs text-stone-600 space-y-3">
            <p>Panel integral para la junta de gobierno y Tuno Mayor:</p>
            <ul class="space-y-1.5 list-disc pl-4 text-stone-700">
              <li><strong>0. Estadísticas:</strong> KPIs, gráficos de barras de 12 meses y tablas.</li>
              <li><strong>1. Contratos:</strong> Gestión y aprobación de presupuestos.</li>
              <li><strong>2. Cartera Clientes:</strong> Fichas, contratos y pedidos de clientes.</li>
              <li><strong>3. Pedidos Tienda:</strong> Gestión de envíos y tracking de Correos.</li>
              <li><strong>4. Productos:</strong> 4.1 Añadir y 4.2 Modificar/eliminar catálogo.</li>
              <li><strong>5. Miembros:</strong> Plantilla, altas de novatos y rangos.</li>
              <li><strong>6. Cuenta Admin:</strong> Datos de perfil y seguridad.</li>
              <li><strong>7. Certámenes:</strong> Creación y palmarés de festivales.</li>
            </ul>
          </div>
        </div>

        <div class="p-6 pt-0">
          <a href="admin.html" class="w-full py-3 bg-[#8B0000] hover:bg-[#5C0000] text-amber-200 font-bold rounded-xl text-xs uppercase tracking-wider text-center block shadow transition border border-[#D4AF37]">
            Abrir Mockup Administrador →
          </a>
        </div>
      </div>

    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-[#120404] text-stone-300 border-t-2 border-[#D4AF37] py-8 text-xs text-center mt-auto">
    <div class="max-w-7xl mx-auto px-4 space-y-2">
      <div class="font-serif-tuna font-bold text-amber-300 text-base">TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA</div>
      <p class="text-stone-400">Universidad de Almería · Campus de La Cañada de San Urbano · Tel: +34 600 123 456</p>
      <p class="text-stone-600 text-[11px] pt-2">© 2026 Todos los derechos reservados.</p>
    </div>
  </footer>

</body>
</html>
"""

if __name__ == '__main__':
    content = get_index_html()
    target = r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\index.html"
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Guardado:", target)

