/**
 * Tuna de la Facultad de Derecho de Almería
 * Módulo Central de JavaScript: API, Autenticación, Carrito, Notificaciones Toast y Modales
 */

const TunaApp = (() => {
  // Estado global en memoria
  let currentUser = null;
  let csrfToken = null;
  let isAuthChecked = false;

  // Clave del carrito en localStorage
  const CART_KEY = 'tuna_cart_v1';

  /**
   * Petición unificada a la API con protección CSRF e interceptores
   */
  async function apiFetch(url, options = {}) {
    options.headers = options.headers || {};

    // Si hay un CSRF token en memoria o en meta tag, adjuntarlo
    const token = csrfToken || getCsrfTokenFromDOM();
    if (token && ['POST', 'PUT', 'DELETE'].includes((options.method || 'GET').toUpperCase())) {
      options.headers['X-CSRF-Token'] = token;
    }

    if (options.body && typeof options.body === 'object' && !(options.body instanceof FormData)) {
      options.headers['Content-Type'] = 'application/json';
      options.body = JSON.stringify(options.body);
    }

    try {
      const response = await fetch(url, options);
      const data = await response.json().catch(() => ({ success: false, error: 'Respuesta no válida del servidor' }));

      if (!response.ok) {
        throw new Error(data.error || `Error HTTP ${response.status}`);
      }
      return data;
    } catch (err) {
      console.error(`[TunaApp API Error] en ${url}:`, err);
      throw err;
    }
  }

  function getCsrfTokenFromDOM() {
    const meta = document.querySelector('meta[name="csrf-token"]');
    return meta ? meta.getAttribute('content') : null;
  }

  /**
   * Comprueba la sesión actual del usuario
   */
  async function checkAuth() {
    try {
      const res = await apiFetch('/api/auth/me');
      if (res.authenticated && res.user) {
        currentUser = res.user;
        csrfToken = res.csrf_token;
      } else {
        currentUser = null;
        csrfToken = null;
      }
    } catch (e) {
      currentUser = null;
      csrfToken = null;
    }
    isAuthChecked = true;
    updateHeaderUI();
    return currentUser;
  }

  /**
   * Actualiza los elementos del encabezado según si el usuario es Visitante, Cliente o Admin
   */
  function updateHeaderUI() {
    const actionsArea = document.getElementById('headerUserActions');
    if (!actionsArea) return;

    if (currentUser) {
      if (currentUser.role === 'admin') {
        actionsArea.innerHTML = `
          <a href="/admin/contratos.html" class="btn-admin-pill" title="Ir al Panel de Administración">
            <span class="badge-dot"></span>
            <span>Panel Admin</span>
          </a>
          <button onclick="TunaApp.logout()" class="btn-logout" title="Cerrar Sesión">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
            <span>Salir</span>
          </button>
        `;
      } else {
        // Rol cliente
        actionsArea.innerHTML = `
          <a href="/cliente/pedidos.html" class="btn-client-user" title="Ir a mi área privada">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            <span>${escapeHTML(currentUser.name.split(' ')[0])}</span>
          </a>
          <button onclick="TunaApp.logout()" class="btn-logout" title="Cerrar Sesión">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
          </button>
        `;
      }
    } else {
      actionsArea.innerHTML = `
        <a href="/auth/login.html" class="btn-login-header" title="Iniciar Sesión">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
            <polyline points="10 17 15 12 10 7"></polyline>
            <line x1="15" y1="12" x2="3" y2="12"></line>
          </svg>
          <span>Iniciar Sesión</span>
        </a>
      `;
    }
  }

  /**
   * Cierre de sesión seguro
   */
  async function logout() {
    try {
      await apiFetch('/api/auth/logout', { method: 'POST' });
      currentUser = null;
      csrfToken = null;
      showToast('Sesión cerrada correctamente', 'info');
      setTimeout(() => {
        window.location.href = '/visitante/inicio.html';
      }, 700);
    } catch (e) {
      window.location.href = '/visitante/inicio.html';
    }
  }

  // ============================================================
  // CARRITO DE MERCHANDISING
  // ============================================================
  function getCart() {
    try {
      return JSON.parse(localStorage.getItem(CART_KEY)) || [];
    } catch (e) {
      return [];
    }
  }

  function saveCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartBadge();
  }

  function addToCart(product) {
    const cart = getCart();
    const existing = cart.find(item => item.id === product.id);
    if (existing) {
      existing.quantity += 1;
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        price: parseFloat(product.price),
        image_url: product.image_url,
        quantity: 1
      });
    }
    saveCart(cart);
    showToast(`"${product.name}" añadido al carrito`, 'success');
  }

  function removeFromCart(productId) {
    let cart = getCart();
    cart = cart.filter(item => item.id !== productId);
    saveCart(cart);
    renderCartModal();
  }

  function updateItemQuantity(productId, delta) {
    const cart = getCart();
    const item = cart.find(i => i.id === productId);
    if (item) {
      item.quantity += delta;
      if (item.quantity <= 0) {
        removeFromCart(productId);
        return;
      }
      saveCart(cart);
      renderCartModal();
    }
  }

  function clearCart() {
    localStorage.removeItem(CART_KEY);
    updateCartBadge();
  }

  function updateCartBadge() {
    const cart = getCart();
    const totalCount = cart.reduce((acc, item) => acc + item.quantity, 0);
    const badges = document.querySelectorAll('.cart-count, #cartCountBadge');
    badges.forEach(badge => {
      badge.textContent = totalCount;
      badge.style.display = totalCount > 0 ? 'flex' : 'none';
    });
  }

  function renderCartModal() {
    const cart = getCart();
    const container = document.getElementById('cartItemsList');
    const totalEl = document.getElementById('cartTotalPrice');
    if (!container) return;

    if (cart.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 40px 20px; color: var(--text-muted);">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin: 0 auto 12px; color: #CBD5E1;"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
          <p style="font-weight: 600; font-size: 15px;">Tu carrito está vacío</p>
          <p style="font-size: 13px; margin-top: 4px;">Explora la tienda oficial y adquiere recuerdos de la Tuna.</p>
        </div>
      `;
      if (totalEl) totalEl.textContent = '0.00 €';
      const checkoutBtn = document.getElementById('btnStartCheckout');
      if (checkoutBtn) checkoutBtn.disabled = true;
      return;
    }

    let total = 0;
    let html = '';
    cart.forEach(item => {
      const itemSubtotal = item.price * item.quantity;
      total += itemSubtotal;
      html += `
        <div class="cart-item-row" style="display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid var(--border-color); gap: 12px;">
          <div style="flex: 1;">
            <div style="font-weight: 600; font-size: 14px; color: var(--text-main);">${escapeHTML(item.name)}</div>
            <div style="font-size: 13px; color: var(--primary); font-weight: 700;">${item.price.toFixed(2)} €</div>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <button onclick="TunaApp.updateItemQuantity(${item.id}, -1)" class="cart-qty-btn">-</button>
            <span style="font-size: 14px; font-weight: 600; min-width: 20px; text-align: center;">${item.quantity}</span>
            <button onclick="TunaApp.updateItemQuantity(${item.id}, 1)" class="cart-qty-btn">+</button>
          </div>
          <div style="font-weight: 700; font-size: 14px; min-width: 60px; text-align: right;">${itemSubtotal.toFixed(2)} €</div>
          <button onclick="TunaApp.removeFromCart(${item.id})" class="cart-del-btn" title="Eliminar">&times;</button>
        </div>
      `;
    });

    container.innerHTML = html;
    if (totalEl) totalEl.textContent = `${total.toFixed(2)} €`;
    const checkoutBtn = document.getElementById('btnStartCheckout');
    if (checkoutBtn) checkoutBtn.disabled = false;
  }

  function openCart() {
    renderCartModal();
    openModal('modalCarrito');
  }

  // ============================================================
  // NOTIFICACIONES TOAST & MODALES
  // ============================================================
  function showToast(message, type = 'info') {
    let container = document.getElementById('toastContainer');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toastContainer';
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `tuna-toast toast-${type}`;
    
    let iconSvg = '';
    if (type === 'success') {
      iconSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>';
    } else if (type === 'error') {
      iconSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>';
    } else {
      iconSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>';
    }

    toast.innerHTML = `
      <div class="toast-icon">${iconSvg}</div>
      <div class="toast-body">${escapeHTML(message)}</div>
    `;

    container.appendChild(toast);
    setTimeout(() => { toast.classList.add('visible'); }, 10);
    setTimeout(() => {
      toast.classList.remove('visible');
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }

  function openModal(id) {
    const m = document.getElementById(id);
    if (m) {
      m.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeModal(id) {
    const m = document.getElementById(id);
    if (m) {
      m.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  function escapeHTML(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Inicialización al cargar el DOM
  document.addEventListener('DOMContentLoaded', () => {
    checkAuth();
    updateCartBadge();

    // Cerrar modales con Escape y backdrop click
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
        document.body.style.overflow = '';
      }
    });

    document.querySelectorAll('.modal-overlay').forEach(modal => {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.remove('active');
          document.body.style.overflow = '';
        }
      });
    });
  });

  return {
    apiFetch,
    checkAuth,
    getCurrentUser: () => currentUser,
    getCsrfToken: () => csrfToken,
    logout,
    showToast,
    openModal,
    closeModal,
    escapeHTML,
    // Carrito
    getCart,
    addToCart,
    removeFromCart,
    updateItemQuantity,
    clearCart,
    openCart,
    renderCartModal
  };
})();

window.TunaApp = TunaApp;
