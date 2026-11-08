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
            ⚙️ Panel Admin
          </a>
          <button type="button" onclick="TunaDB.auth.logout()" class="btn btn-outline" style="font-size: 12px; padding: 6px 10px; color: var(--muted);" title="Cerrar sesión">
            Cerrar sesión
          </button>
        `;
      } else {
        userBox.innerHTML = `
          <a href="${pathPrefix}cliente/index.html" class="btn btn-outline" style="font-size: 12.5px; padding: 6px 12px; font-weight: 600;" title="Ver mi cuenta">
            👤 Hola, ${user.nombre}
          </a>
          <button type="button" onclick="TunaDB.auth.logout()" class="btn btn-outline" style="font-size: 12px; padding: 6px 10px; color: var(--muted);" title="Cerrar sesión">
            Salir
          </button>
        `;
      }
    }
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
    const icon = type === 'success' ? '✓' : (type === 'error' ? '⚠' : 'ℹ');
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
  }
};

// Inicialización de la aplicación
document.addEventListener('DOMContentLoaded', () => {
  // 1. Verificar seguridad de rutas
  TunaApp.enforceRouteGuard();

  // 2. Actualizar estado de autenticación en cabecera
  TunaApp.updateHeaderAuth();
  
  // 3. Actualizar contador del carrito
  const cart = JSON.parse(localStorage.getItem('tuna_cart') || '[]');
  const totalCount = cart.reduce((acc, item) => acc + (item.qty || 1), 0);
  document.querySelectorAll('.cart-counter-val').forEach(el => {
    el.textContent = totalCount;
  });
  
  // 4. Soporte para modales de imágenes (Lightbox)
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
