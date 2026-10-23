/**
 * Lógica del Portal de Cliente - Tuna de Derecho de Almería
 * Conexión segura con la API REST y Base de Datos SQLite
 */

const TunaClient = (() => {
  let currentUser = null;

  async function initClientPage(requiredPage = '') {
    try {
      const auth = await TunaApp.checkAuth();
      if (!auth) {
        window.location.href = '/auth/login.html?redirect=' + encodeURIComponent(window.location.pathname);
        return null;
      }
      currentUser = auth;
      renderUserPill();
      return currentUser;
    } catch (e) {
      window.location.href = '/auth/login.html';
      return null;
    }
  }

  function renderUserPill() {
    if (!currentUser) return;

    // Elementos de saludo
    const nameEls = document.querySelectorAll('#user-display-name, .client-user-name');
    nameEls.forEach(el => el.textContent = currentUser.name);

    const firstNameEls = document.querySelectorAll('#hero-user-name, .client-first-name');
    firstNameEls.forEach(el => el.textContent = currentUser.name.split(' ')[0]);

    const emailEls = document.querySelectorAll('#profile-email, .client-email');
    emailEls.forEach(el => {
      if (el.tagName === 'INPUT') el.value = currentUser.email;
      else el.textContent = currentUser.email;
    });

    const phoneEls = document.querySelectorAll('#profile-phone, .client-phone');
    phoneEls.forEach(el => {
      if (el.tagName === 'INPUT') el.value = currentUser.phone || '';
      else el.textContent = currentUser.phone || 'No especificado';
    });

    const nameInput = document.getElementById('profile-name');
    if (nameInput) nameInput.value = currentUser.name;

    // Iniciales para el avatar
    const initials = currentUser.name
      .split(' ')
      .map(n => n[0])
      .join('')
      .substring(0, 2)
      .toUpperCase();

    const avatars = document.querySelectorAll('#user-avatar, .client-avatar');
    avatars.forEach(av => av.textContent = initials || 'CL');
  }

  /**
   * Cargar y renderizar el historial de pedidos en pedidos.html
   */
  async function loadOrders() {
    const listContainer = document.getElementById('ordersListContainer');
    if (!listContainer) return;

    try {
      listContainer.innerHTML = '<div style="text-align:center; padding: 40px; color: var(--text-subtle);">Cargando tus pedidos...</div>';
      const res = await TunaApp.apiFetch('/api/pedidos');
      const orders = res.orders || [];

      if (orders.length === 0) {
        listContainer.innerHTML = `
          <div style="text-align: center; padding: 60px 20px; background: #FFF; border-radius: var(--radius-lg); border: 1px solid var(--border-color);">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin: 0 auto 12px; color: #CBD5E1;"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
            <h3 style="font-size: 18px; font-weight: 700; color: var(--text-main); margin-bottom: 6px;">No tienes pedidos registrados</h3>
            <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 20px;">Visita nuestra tienda para adquirir camisetas, becas o discos oficiales.</p>
            <a href="/visitante/tienda.html" class="btn btn-primary">Ir a la Tienda Oficial</a>
          </div>
        `;
        return;
      }

      let html = '';
      orders.forEach(o => {
        let badgeClass = 'badge-blue';
        let statusLabel = 'En proceso';
        if (o.status === 'enviado') {
          badgeClass = 'badge-green';
          statusLabel = 'Enviado';
        } else if (o.status === 'entregado') {
          badgeClass = 'badge-green';
          statusLabel = 'Entregado';
        } else if (o.status === 'cancelado') {
          badgeClass = 'badge-red';
          statusLabel = 'Cancelado';
        }

        const itemsSummary = (o.items || []).map(i => `${i.quantity}x ${TunaApp.escapeHTML(i.product_name)} (${(i.price * i.quantity).toFixed(2)} €)`).join(' · ');

        html += `
          <div class="order-card" style="background:#FFF; border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:24px; margin-bottom:20px; box-shadow:var(--shadow-sm);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; border-bottom:1px solid var(--border-color); padding-bottom:16px; margin-bottom:16px;">
              <div>
                <span style="font-size:12px; font-weight:700; color:var(--text-subtle); text-transform:uppercase;">Código de Pedido</span>
                <div style="font-size:17px; font-weight:800; color:var(--text-main);">${TunaApp.escapeHTML(o.order_code)}</div>
              </div>
              <div>
                <span style="font-size:12px; font-weight:700; color:var(--text-subtle); text-transform:uppercase;">Fecha</span>
                <div style="font-size:14px; font-weight:600; color:var(--text-muted);">${o.created_at.split(' ')[0]}</div>
              </div>
              <div>
                <span style="font-size:12px; font-weight:700; color:var(--text-subtle); text-transform:uppercase;">Importe</span>
                <div style="font-size:18px; font-weight:800; color:var(--primary);">${parseFloat(o.total_amount).toFixed(2)} €</div>
              </div>
              <div>
                <span class="status-pill ${badgeClass}" style="padding:4px 12px; border-radius:var(--radius-full); font-size:12px; font-weight:700; text-transform:uppercase;">${statusLabel}</span>
              </div>
            </div>

            <div style="font-size:14px; color:var(--text-muted); margin-bottom:12px;">
              <strong>Artículos:</strong> ${itemsSummary || 'Sin detalles'}
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; font-size:13px; color:var(--text-subtle); flex-wrap:wrap; gap:8px;">
              <div>
                <span>Envío a: <strong>${TunaApp.escapeHTML(o.shipping_city)}</strong> (${TunaApp.escapeHTML(o.shipping_address)})</span>
                ${o.tracking_number ? ` · Seguimiento: <strong>${TunaApp.escapeHTML(o.tracking_number)}</strong>` : ''}
              </div>
              <div style="font-weight:600; color:var(--accent-blue);">Pago: ${TunaApp.escapeHTML(o.payment_method)}</div>
            </div>
          </div>
        `;
      });

      listContainer.innerHTML = html;
    } catch (err) {
      listContainer.innerHTML = `<div style="color:var(--primary); padding:20px;">Error al cargar pedidos: ${err.message}</div>`;
    }
  }

  /**
   * Guardar datos del perfil en datos.html
   */
  async function saveProfile(e) {
    e.preventDefault();
    const name = document.getElementById('profile-name').value.trim();
    const phone = document.getElementById('profile-phone').value.trim();
    const email = document.getElementById('profile-email').value.trim();

    try {
      const res = await TunaApp.apiFetch('/api/auth/update-profile', {
        method: 'POST',
        body: { name, phone, email }
      });
      if (res.success) {
        currentUser.name = name;
        currentUser.phone = phone;
        currentUser.email = email;
        renderUserPill();
        TunaApp.showToast('Datos de perfil guardados en la base de datos.', 'success');
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  /**
   * Cambiar contraseña en gestionar-cuenta.html
   */
  async function changePassword(e) {
    e.preventDefault();
    const current = document.getElementById('currentPassword').value;
    const newPass = document.getElementById('newPassword').value;
    const confirm = document.getElementById('confirmPassword').value;

    if (newPass !== confirm) {
      TunaApp.showToast('Las contraseñas nuevas no coinciden', 'error');
      return;
    }

    if (newPass.length < 8) {
      TunaApp.showToast('La nueva contraseña debe tener mínimo 8 caracteres', 'error');
      return;
    }

    try {
      const res = await TunaApp.apiFetch('/api/auth/change-password', {
        method: 'POST',
        body: {
          current_password: current,
          new_password: newPass
        }
      });
      if (res.success) {
        TunaApp.showToast('Contraseña actualizada con éxito.', 'success');
        document.getElementById('currentPassword').value = '';
        document.getElementById('newPassword').value = '';
        document.getElementById('confirmPassword').value = '';
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  /**
   * Enviar solicitud de contratación desde el área privada
   */
  async function submitContract(e) {
    e.preventDefault();
    const event_type = document.getElementById('contractEventType').value;
    const event_date = document.getElementById('contractDate').value;
    const event_time = document.getElementById('contractTime').value;
    const location = document.getElementById('contractLocation').value.trim();
    const attendees = document.getElementById('contractAttendees').value.trim();
    const transport_logistics = document.getElementById('contractTransport').value;
    const notes = document.getElementById('contractNotes').value.trim();

    const client_name = currentUser ? currentUser.name : document.getElementById('contractClientName').value.trim();
    const client_phone = currentUser ? currentUser.phone : document.getElementById('contractClientPhone').value.trim();
    const client_email = currentUser ? currentUser.email : document.getElementById('contractClientEmail').value.trim();

    try {
      const res = await TunaApp.apiFetch('/api/contratos', {
        method: 'POST',
        body: {
          client_name,
          client_phone,
          client_email,
          event_type,
          event_date,
          event_time,
          location,
          attendees,
          transport_logistics,
          notes
        }
      });

      if (res.success) {
        TunaApp.showToast('Solicitud registrada correctamente en la base de datos.', 'success');
        
        // Modal de éxito con opción de abrir WhatsApp
        const modalMsg = document.getElementById('contractSuccessModal');
        if (modalMsg) {
          document.getElementById('whatsappDirectLink').href = res.whatsapp_link;
          TunaApp.openModal('contractSuccessModal');
        } else {
          // Si no hay modal especial, abrir enlace WhatsApp en pestaña
          if (confirm('Solicitud guardada. ¿Deseas abrir WhatsApp para enviar los datos directamente a Popeye?')) {
            window.open(res.whatsapp_link, '_blank');
          }
        }
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  return {
    initClientPage,
    loadOrders,
    saveProfile,
    changePassword,
    submitContract
  };
})();

window.TunaClient = TunaClient;
