# -*- coding: utf-8 -*-
import os
import re

files_and_active = [
    (r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\visitante.html", "visitante"),
    (r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\cliente.html", "cliente"),
    (r"c:\Users\joses\OneDrive\Documentos\Ingeniería Informática\4º\TW\mockup\admin.html", "admin"),
]

def make_profile_bar(active_profile):
    v_cls = 'bg-white text-[#8B0000] font-bold border-b-2 border-[#D4AF37] shadow' if active_profile == 'visitante' else 'text-slate-300 hover:text-white'
    c_cls = 'bg-white text-[#8B0000] font-bold border-b-2 border-[#D4AF37] shadow' if active_profile == 'cliente' else 'text-slate-300 hover:text-white'
    a_cls = 'bg-white text-[#8B0000] font-bold border-b-2 border-[#D4AF37] shadow' if active_profile == 'admin' else 'text-slate-300 hover:text-white'

    return f'''
  <!-- ========================================================================= -->
  <!-- SELECTOR DE PERFILES EN CABECERA SUPERIOR (OCULTABLE) -->
  <!-- ========================================================================= -->
  <div id="global-profile-bar" class="sticky top-0 z-50 bg-[#121212] border-b border-amber-500/40 text-white shadow-xl transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 py-2 flex flex-col md:flex-row items-center justify-between gap-2 text-xs">
      <div class="flex items-center gap-2.5">
        <span class="w-6 h-6 rounded bg-red-900 text-amber-300 font-serif-tuna font-black flex items-center justify-center border border-amber-500 text-xs">TD</span>
        <div>
          <span class="text-amber-400 font-bold tracking-wider uppercase text-[10px] block">SELECTOR DE PERFILES</span>
          <span class="text-slate-300 text-[11px]">Tuna de la Facultad de Derecho de Almería · Perfil actual: <strong class="text-white uppercase">{active_profile}</strong></span>
        </div>
      </div>

      <!-- Selector para cambiar de mockup -->
      <div class="flex items-center bg-[#1f1f1f] p-1 rounded-xl border border-slate-700">
        <a href="visitante.html" class="px-3.5 py-1.5 rounded-lg text-xs {v_cls} transition flex items-center gap-1.5">
          <span>🌐</span> Visitante <span class="text-[10px] opacity-75">(Público)</span>
        </a>
        <a href="cliente.html" class="px-3.5 py-1.5 rounded-lg text-xs {c_cls} transition flex items-center gap-1.5">
          <span>👤</span> Cliente <span class="text-[10px] opacity-75">(Registrado)</span>
        </a>
        <a href="admin.html" class="px-3.5 py-1.5 rounded-lg text-xs {a_cls} transition flex items-center gap-1.5">
          <span>⚙️</span> Administrador <span class="text-[10px] opacity-75">(Gestión)</span>
        </a>
      </div>

      <!-- Botón para ocultar la barra superior -->
      <div class="flex items-center gap-2">
        <button onclick="toggleProfileBar()" class="px-3 py-1 bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white rounded-lg text-[11px] font-semibold flex items-center gap-1.5 border border-stone-600 transition" title="Ocultar esta barra de control">
          <span>✕</span> Ocultar barra
        </button>
      </div>
    </div>
  </div>

  <!-- Botón flotante para restaurar la barra cuando esté oculta -->
  <button id="btn-restore-bar" onclick="toggleProfileBar()" class="hidden fixed top-2 right-2 z-50 px-3.5 py-1.5 bg-[#121212]/95 hover:bg-[#121212] text-amber-300 rounded-full border border-amber-500/70 text-xs font-bold shadow-2xl backdrop-blur flex items-center gap-1.5 transition hover:scale-105" title="Mostrar de nuevo el selector de perfiles">
    <span>⚙️</span> Cambiar Perfil
  </button>
'''

script_func = '''
    function toggleProfileBar() {
      const bar = document.getElementById('global-profile-bar');
      const restoreBtn = document.getElementById('btn-restore-bar');
      if (bar.classList.contains('hidden')) {
        bar.classList.remove('hidden');
        restoreBtn.classList.add('hidden');
      } else {
        bar.classList.add('hidden');
        restoreBtn.classList.remove('hidden');
      }
    }
'''

for file_path, profile in files_and_active:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Reemplazar la barra superior antigua
        # Buscamos desde <body hasta el header o primer bloque
        old_bar_regex = r'<div class="sticky top-0 z-50 bg-\[#121212\].*?</div>\s*</div>\s*</div>'
        new_bar = make_profile_bar(profile)

        if re.search(old_bar_regex, html, re.S):
            html = re.sub(old_bar_regex, new_bar.strip(), html, count=1, flags=re.S)
            print(f"Reemplazada barra en {os.path.basename(file_path)}")
        else:
            print(f"Regex no coincidió en {os.path.basename(file_path)}, buscando alternativo...")
            # Reemplazar entre <body ...> y la barra roja de contacto
            idx_body = html.find('<body')
            idx_body_end = html.find('>', idx_body) + 1
            idx_red_bar = html.find('<!-- ===', idx_body_end)
            if idx_red_bar != -1:
                html = html[:idx_body_end] + "\n" + new_bar + "\n" + html[idx_red_bar:]
                print(f"Insertado por posición en {os.path.basename(file_path)}")

        # Agregar script al final si no está
        if 'toggleProfileBar' not in html:
            idx_script = html.rfind('</script>')
            if idx_script != -1:
                html = html[:idx_script] + script_func + "\n  " + html[idx_script:]
            else:
                html = html.replace('</body>', f'<script>{script_func}</script>\n</body>')
            print(f"Script toggle añadido en {os.path.basename(file_path)}")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)

print("Proceso completado.")

