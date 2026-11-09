/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Módulo Principal (main.js)
 * Control de cabecera dinámica, protección de rutas y notificaciones
 */

const TunaApp = {
  // Sincronizar estado de sesión en la cabecera
  updateHeaderAuth() {
    const user = TunaDB.auth.getCurrentUser();
    const loginBtn = document.querySelector('.btn-header-login');
    const headerActions = document.querySelector('.header-actions');

    if (!headerActions) return;

    // Determinar ruta relativa según la carpeta actual
    const isRoot = !window.location.pathname.includes('/visitante/') && 
                   !window.location.pathname.includes('/cliente/') && 
                   !window.location.pathname.includes('/admin/');
    const pathPrefix = isRoot ? '' : '../';

    if (user) {
      // Eliminar botón de inicio de sesión si existe
      if (loginBtn) loginBtn.remove();

      // Comprobar si ya existe el contenedor de usuario
      let userBox = document.getElementById('header-user-status');
      if (!userBox) {
        userBox = document.createElement('div');
        userBox.id = 'header-user-status';
        userBox.style.cssText = 'display: flex; align-items: center; gap: 10px;';
        headerActions.appendChild(userBox);
      }

      if (user.rol === 'admin') {
        userBox.innerHTML = `
          <a href="${pathPrefix}admin/index.html" class="btn btn-outline" style="font-size: 12.5px; padding: 6px 12px; border-color: var(--gold); color: var(--gold-dark); font-weight: 700;">
            Panel Admin
          </a>
          <button type="button" onclick="TunaDB.auth.logout()" class="btn btn-outline" style="font-size: 12px; padding: 6px 10px; color: var(--muted);" title="Cerrar sesión">
            Cerrar sesión
          </button>
        `;
      } else {
        userBox.innerHTML = `
          <a href="${pathPrefix}cliente/index.html" class="btn btn-outline" style="font-size: 12.5px; padding: 6px 12px; font-weight: 600;" title="Ver mi cuenta">
            Hola, ${user.nombre}
          </a>
          <button type="button" onclick="TunaDB.auth.logout()" class="btn btn-outline" style="font-size: 12px; padding: 6px 10px; color: var(--muted);" title="Cerrar sesión">
            Salir
          </button>
        `;
      }
    }
  },

  // Enlaces "Cerrar sesión" de cliente y admin: borra la sesión y el propio enlace navega a la portada
  logout() {
    localStorage.removeItem('tuna_db_session');
  },

  // Protección de rutas: comprueba si la página exige autenticación y rol adecuado
  enforceRouteGuard() {
    const path = window.location.pathname.replace(/\\/g, '/').toLowerCase();
    const user = TunaDB.auth.getCurrentUser();
    
    if (path.includes('/cliente/')) {
      if (!user) {
        alert('Esta sección es privada. Por favor, inicia sesión con tu cuenta de cliente.');
        window.location.href = '../visitante/Acceso.html';
      }
    } else if (path.includes('/admin/')) {
      if (!user) {
        alert('Acceso restringido: Esta sección requiere una cuenta de Administrador. Por favor, inicia sesión.');
        window.location.href = '../visitante/Acceso.html';
      } else if (user.rol !== 'admin') {
        alert(`Acceso denegado: Tu cuenta actual (${user.email}) tiene rol de "cliente". El panel de administración está reservado exclusivamente para administradores.`);
        window.location.href = '../cliente/index.html';
      }
    }
  },

  showToast(message, type = 'info') {
    let container = document.getElementById('toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toast-container';
      document.body.appendChild(container);
    }
    const toast = document.createElement('div');
    toast.className = 'toast-message';
    const icon = type === 'success' ? '✓' : (type === 'error' ? '!' : 'ℹ');
    toast.innerHTML = `<span style="color:var(--gold); font-size:18px; font-weight:bold;">${icon}</span> <span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  },

  goBack(fallbackUrl) {
    if (window.history.length > 1) {
      window.history.back();
    } else if (fallbackUrl) {
      window.location.href = fallbackUrl;
    }
  },

  // Menú lateral de administración: única navegación del panel
  renderAdminSidebar() {
    const sidebar = document.querySelector('.admin-sidebar');
    if (!sidebar) return;

    const MENU = [
      { label: 'Panel de estadísticas', href: 'index.html' },
      { label: 'Contratos', href: 'Contratos.html', pages: ['ContratoDetalle.html'] },
      { label: 'Cartera de clientes', href: 'Clientes.html', pages: ['FichaCliente.html', 'ContratosCliente.html', 'PedidosCliente.html'] },
      { label: 'Pedidos de la tienda', href: 'Pedidos.html', pages: ['PedidoDetalle.html'] },
      { label: 'Productos de la tienda', pages: ['Productos.html'], options: [
        { label: 'Añadir producto', href: 'ProductoNuevo.html' },
        { label: 'Modificar o eliminar producto', href: 'ProductosGestion.html' }
      ] },
      { label: 'Lista de miembros', pages: ['Miembros.html'], options: [
        { label: 'Añadir nuevos miembros', href: 'MiembroNuevo.html' },
        { label: 'Modificar o eliminar miembro', href: 'MiembrosGestion.html' }
      ] },
      { label: 'Cuenta', pages: ['Cuenta.html'], options: [
        { label: 'Modificar información personal', href: 'CuentaDatos.html' },
        { label: 'Cambiar contraseña', href: 'CuentaPassword.html' }
      ] },
      { label: 'Certámenes', pages: ['Certamenes.html'], options: [
        { label: 'Crear nuevo certamen', href: 'CertamenNuevo.html' },
        { label: 'Modificar o eliminar certamen', href: 'CertamenesGestion.html' }
      ] }
    ];

    const current = window.location.pathname.split('/').pop() || 'index.html';
    const items = MENU.map((item) => {
      if (!item.options) {
        const active = item.href === current || (item.pages || []).includes(current);
        return `<a href="${item.href}" class="admin-menu-link${active ? ' is-active' : ''}"${active ? ' aria-current="page"' : ''}>${item.label}</a>`;
      }
      const inSection = item.pages.includes(current) || item.options.some((o) => o.href === current);
      const links = item.options.map((o) =>
        `<a href="${o.href}"${o.href === current ? ' class="is-active" aria-current="page"' : ''}>${o.label}</a>`
      ).join('');
      return `<details class="admin-menu-section${inSection ? ' is-active' : ''}" name="admin-menu"${inSection ? ' open' : ''}>
        <summary>${item.label}</summary>
        <div class="admin-submenu">${links}</div>
      </details>`;
    }).join('');

    sidebar.innerHTML = `
      <div class="admin-sidebar-top">
        <a href="index.html" class="admin-sidebar-logo">
          <img src="../assets/img/logo_corporativo.svg" alt="Tuna de Derecho Almería Logo">
        </a>
        <button type="button" class="admin-sidebar-toggle" aria-expanded="false">Menú</button>
      </div>
      <div class="admin-sidebar-body">
        <nav class="admin-menu">${items}</nav>
        <div class="admin-sidebar-actions">
          <a href="../visitante/index.html">Ver web</a>
          <a href="../visitante/index.html" onclick="TunaApp.logout()">Cerrar sesión</a>
        </div>
      </div>
    `;

    const toggle = sidebar.querySelector('.admin-sidebar-toggle');
    toggle.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', sidebar.classList.toggle('is-open'));
    });
  },

  // Botón flotante interactivo de máxima elegancia (Contacta a la tuna)
  renderFloatingContact() {
    if (document.querySelector('.floating-tuna-contact')) return;

    const path = window.location.pathname.replace(/\\/g, '/').toLowerCase();
    const isRoot = !path.includes('/visitante/') && !path.includes('/cliente/') && !path.includes('/admin/');
    const spotifyUrl = isRoot ? 'visitante/Spotify.html' : (path.includes('/visitante/') ? 'Spotify.html' : '../visitante/Spotify.html');

    const widget = document.createElement('aside');
    widget.className = 'floating-tuna-contact';
    widget.setAttribute('aria-label', 'Contacta a la tuna');
    widget.innerHTML = `
      <button type="button" class="floating-contact-toggle" aria-label="Mostrar opciones de contacto" title="Contacta a la tuna">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="display:block;">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
        </svg>
      </button>
      <div class="floating-contact-panel"><div class="floating-contact-panel-inner">
      <div class="contact-badge-label">
        <span class="sub">Contacta a la tuna</span>
        <a href="tel:685995510" class="phone-num" title="Llamar directamente a la Tuna">📞 685 99 55 10</a>
      </div>
      <div class="floating-sep"></div>
      <div class="floating-icons-group">
        <a href="https://wa.me/34685995510" target="_blank" rel="noopener noreferrer" class="floating-btn-icon floating-wa" title="Escribir por WhatsApp al 685 99 55 10">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="#ffffff" aria-hidden="true" style="display:block;">
            <path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24zm4.52 11.66c-.25.7-.99 1.27-1.74 1.43-.51.11-1.18.2-3.41-.72-2.85-1.18-4.68-4.08-4.82-4.27-.14-.19-1.16-1.54-1.16-2.94 0-1.4.73-2.09 1-2.37.26-.28.57-.35.76-.35.19 0 .38 0 .55.01.18.01.42-.07.66.5.25.59.85 2.07.92 2.22.08.15.13.33.03.53-.1.2-.15.33-.3.51-.15.18-.32.39-.45.53-.15.15-.31.32-.13.63.17.31.78 1.28 1.67 2.08 1.15 1.02 2.11 1.34 2.41 1.49.3.15.48.13.66-.08.18-.21.76-.89.97-1.19.2-.3.41-.25.68-.15.28.1 1.77.88 1.77.88.21.1.35.15.4.24.06.09.06.51-.19 1.21z"/>
          </svg>
        </a>
        <a href="${spotifyUrl}" class="floating-btn-icon floating-spotify" title="Escuchar a la Tuna en Spotify">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="#ffffff" aria-hidden="true" style="display:block;">
            <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.586 14.424c-.18.295-.563.387-.857.207-2.348-1.435-5.304-1.76-8.785-.963-.335.077-.67-.133-.746-.469-.077-.334.132-.67.467-.746 3.809-.871 7.077-.496 9.714 1.115.294.18.386.563.207.856zm1.223-2.724c-.227.369-.714.484-1.083.257-2.688-1.652-6.785-2.131-9.965-1.166-.413.126-.849-.108-.975-.521-.126-.413.108-.849.521-.975 3.632-1.102 8.147-.568 11.246 1.339.368.226.483.713.256 1.082zm.106-2.835C14.692 8.95 8.082 8.73 4.247 9.894c-.494.15-1.02-.133-1.17-.627-.15-.494.133-1.02.627-1.17 4.403-1.336 11.69-1.08 16.082 1.528.444.263.589.84.326 1.284-.263.444-.84.59-1.284.326z"/>
          </svg>
        </a>
        <a href="https://instagram.com/tunaderechoalmeria" target="_blank" rel="noopener noreferrer" class="floating-btn-icon floating-ig" title="Ver Instagram oficial @tunaderechoalmeria">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="#ffffff" aria-hidden="true" style="display:block;">
            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
          </svg>
        </a>
      </div>
      </div></div>
    `;
    document.body.appendChild(widget);

    // En pantallas táctiles no hay hover: se abre y se cierra con un toque
    const toggle = widget.querySelector('.floating-contact-toggle');
    const setOpen = (open) => {
      widget.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open);
    };
    toggle.addEventListener('click', () => {
      if (window.matchMedia('(hover: none)').matches) setOpen(!widget.classList.contains('is-open'));
    });
    document.addEventListener('click', (e) => {
      if (!widget.contains(e.target)) setOpen(false);
    });
  }
};

// Inicialización de la aplicación
document.addEventListener('DOMContentLoaded', () => {
  // 0. Barra "Volver" fija justo debajo de la cabecera (altura real, también en móvil)
  const siteHeader = document.querySelector('.site-header');
  if (siteHeader) {
    const syncHeaderHeight = () =>
      document.documentElement.style.setProperty('--header-h', siteHeader.offsetHeight + 'px');
    syncHeaderHeight();
    window.addEventListener('resize', syncHeaderHeight);
  }

  // 1. Verificar seguridad de rutas
  TunaApp.enforceRouteGuard();

  // 2. Actualizar estado de autenticación en cabecera
  TunaApp.updateHeaderAuth();
  TunaApp.renderAdminSidebar();

  // 3. Renderizar botón flotante elegante de contacto (Contacta a la tuna)
  TunaApp.renderFloatingContact();
  
  // 4. Actualizar contador del carrito
  const cart = JSON.parse(localStorage.getItem('tuna_cart') || '[]');
  const totalCount = cart.reduce((acc, item) => acc + (item.qty || 1), 0);
  document.querySelectorAll('.cart-counter-val').forEach(el => {
    el.textContent = totalCount;
    el.classList.toggle('is-empty', totalCount === 0);
  });
  
  // 5. Soporte para modales de imágenes (Lightbox)
  document.querySelectorAll('.lightbox-trigger').forEach(imgEl => {
    imgEl.style.cursor = 'pointer';
    imgEl.addEventListener('click', () => {
      openLightbox(imgEl.getAttribute('src') || imgEl.querySelector('img')?.getAttribute('src'), imgEl.getAttribute('alt') || 'Tuna de la Facultad de Derecho de Almería');
    });
  });
});

function openLightbox(src, caption) {
  if (!src) return;
  let modal = document.getElementById('global-lightbox-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'global-lightbox-modal';
    modal.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.88);z-index:99999;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;cursor:pointer;';
    modal.innerHTML = `
      <div style="position:relative;max-width:92vw;max-height:88vh;cursor:default;" onclick="event.stopPropagation()">
        <button type="button" style="position:absolute;top:-42px;right:0;background:none;border:none;color:#fff;font-size:32px;cursor:pointer;" onclick="closeLightbox()">✕</button>
        <img id="lightbox-img" src="" style="max-width:100%;max-height:82vh;border-radius:8px;box-shadow:0 12px 48px rgba(0,0,0,0.6);border:2px solid var(--gold);">
        <p id="lightbox-caption" style="color:#eed793;text-align:center;margin-top:12px;font-family:var(--serif);font-size:15px;"></p>
      </div>
    `;
    modal.addEventListener('click', closeLightbox);
    document.body.appendChild(modal);
  }
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-caption').textContent = caption || 'Tuna de la Facultad de Derecho de Almería';
  modal.style.display = 'flex';
}

function closeLightbox() {
  const modal = document.getElementById('global-lightbox-modal');
  if (modal) modal.style.display = 'none';
}
