/**
 * Lógica del Panel de Administración - Tuna de Derecho de Almería
 * Módulo para gestión de Contratos, Miembros, Tienda y Repertorio
 */

const TunaAdmin = (() => {
  let adminUser = null;
  let allContracts = [];
  let currentFilter = 'all';

  async function checkAdminAuth() {
    try {
      const user = await TunaApp.checkAuth();
      if (!user || user.role !== 'admin') {
        window.location.href = '/auth/login.html?redirect=' + encodeURIComponent(window.location.pathname);
        return false;
      }
      adminUser = user;
      renderAdminHeader();
      return true;
    } catch (e) {
      window.location.href = '/auth/login.html';
      return false;
    }
  }

  function renderAdminHeader() {
    if (!adminUser) return;
    const nameEls = document.querySelectorAll('#adminUserName, .user-name');
    nameEls.forEach(el => {
      el.textContent = adminUser.name;
    });
    const avatarEls = document.querySelectorAll('#adminAvatarInitials, .user-avatar, .user-profile-chip .avatar');
    avatarEls.forEach(el => {
      const parts = adminUser.name.split(' ');
      el.textContent = parts.length > 1 ? (parts[0][0] + parts[1][0]).toUpperCase() : parts[0].slice(0, 2).toUpperCase();
    });
  }

  // ============================================================
  // GESTIÓN DE CONTRATOS
  // ============================================================
  async function loadContracts() {
    const isAuthed = await checkAdminAuth();
    if (!isAuthed) return;

    try {
      const res = await TunaApp.apiFetch('/api/contratos');
      allContracts = res.contratos || [];
      renderContractsTable();
      updateContractStats();
    } catch (err) {
      TunaApp.showToast('Error cargando contratos: ' + err.message, 'error');
    }
  }

  function updateContractStats() {
    const total = allContracts.length;
    const pending = allContracts.filter(c => c.status === 'pendiente').length;
    const confirmed = allContracts.filter(c => c.status === 'confirmado').length;
    const cancelled = allContracts.filter(c => c.status === 'cancelado').length;

    const elTotal = document.getElementById('statTotalContratos');
    const elPending = document.getElementById('statPendientes');
    const elConfirmed = document.getElementById('statConfirmados');
    const elCancelled = document.getElementById('statCancelados');

    if (elTotal) elTotal.textContent = total;
    if (elPending) elPending.textContent = pending;
    if (elConfirmed) elConfirmed.textContent = confirmed;
    if (elCancelled) elCancelled.textContent = cancelled;
  }

  function renderContractsTable() {
    const tbody = document.querySelector('#tableContratos tbody');
    if (!tbody) return;

    const q = (document.getElementById('searchInput')?.value || '').toLowerCase().trim();

    const filtered = allContracts.filter(c => {
      const matchesStatus = currentFilter === 'all' || c.status === currentFilter;
      const rowText = `${c.client_name} ${c.client_email} ${c.client_phone} ${c.location} ${c.event_type}`.toLowerCase();
      const matchesQuery = !q || rowText.includes(q);
      return matchesStatus && matchesQuery;
    });

    if (filtered.length === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="7" style="text-align: center; padding: 40px; color: var(--text-subtle);">
            No se encontraron contratos coincidentes con los filtros actuales.
          </td>
        </tr>
      `;
      return;
    }

    let html = '';
    filtered.forEach(c => {
      let badgeClass = 'badge-yellow';
      let statusText = 'Pendiente';

      if (c.status === 'confirmado') {
        badgeClass = 'badge-green';
        statusText = 'Confirmado';
      } else if (c.status === 'cancelado') {
        badgeClass = 'badge-red';
        statusText = 'Cancelado';
      } else if (c.status === 'finalizado') {
        badgeClass = 'badge-blue';
        statusText = 'Finalizado';
      }

      const clientMsg = encodeURIComponent(`Hola ${c.client_name}, nos ponemos en contacto desde la Tuna de Derecho de Almería respecto a tu solicitud para el ${c.event_date} en ${c.location}.`);
      const whatsappClientLink = `https://api.whatsapp.com/send?phone=${c.client_phone.replace(/[^0-9]/g, '')}&text=${clientMsg}`;

      html += `
        <tr data-status="${c.status}">
          <td><span style="font-family:monospace; font-weight:700;">#${c.id}</span></td>
          <td>
            <div style="font-weight: 700; color: var(--text-main);">${TunaApp.escapeHTML(c.client_name)}</div>
            <div style="font-size: 12px; color: var(--text-subtle);">${TunaApp.escapeHTML(c.client_email)} · ${TunaApp.escapeHTML(c.client_phone)}</div>
          </td>
          <td>
            <span class="type-pill" style="padding: 2px 8px; border-radius: 4px; background: var(--bg-alt); border: 1px solid var(--border-color); font-size: 12px; font-weight: 600;">
              ${TunaApp.escapeHTML(c.event_type)}
            </span>
          </td>
          <td>
            <div style="font-weight: 600;">${c.event_date}</div>
            <div style="font-size: 12px; color: var(--text-subtle);">${c.event_time}</div>
          </td>
          <td>
            <div style="max-width: 220px; font-size: 13px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;">
              ${TunaApp.escapeHTML(c.location)}
            </div>
          </td>
          <td>
            <span class="status-badge ${badgeClass}" style="padding: 4px 10px; border-radius: var(--radius-full); font-size: 11px; font-weight: 800; text-transform: uppercase;">
              ${statusText}
            </span>
          </td>
          <td>
            <div style="display: flex; gap: 6px;">
              <button onclick="TunaAdmin.openContractModal(${c.id})" class="btn-action" title="Gestionar y Editar">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
              </button>
              <a href="${whatsappClientLink}" target="_blank" class="btn-action" style="color:#16A34A;" title="Contactar por WhatsApp">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
              </a>
              <button onclick="TunaAdmin.deleteContract(${c.id})" class="btn-action" style="color:var(--primary);" title="Eliminar">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
              </button>
            </div>
          </td>
        </tr>
      `;
    });

    tbody.innerHTML = html;
  }

  function filterContracts(status) {
    currentFilter = status;
    document.querySelectorAll('.filter-pills .pill').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.status === status);
    });
    renderContractsTable();
  }

  function openContractModal(id) {
    const c = allContracts.find(x => x.id === id);
    if (!c) return;

    document.getElementById('editContractId').value = c.id;
    document.getElementById('modalClientName').textContent = c.client_name;
    document.getElementById('modalClientContact').textContent = `${c.client_phone} · ${c.client_email}`;
    document.getElementById('modalEventDetails').textContent = `${c.event_type} - ${c.event_date} a las ${c.event_time} en ${c.location}`;
    document.getElementById('modalAttendees').textContent = `Aforo estimado: ${c.attendees || 'No indicado'} · Transporte: ${c.transport_logistics || 'A cargo de la Tuna'}`;
    
    document.getElementById('editContractStatus').value = c.status;
    document.getElementById('editContractPrice').value = c.price_agreed || '';
    document.getElementById('editContractNotes').value = c.notes || '';

    TunaApp.openModal('modalGestionContrato');
  }

  async function saveContractChanges(e) {
    e.preventDefault();
    const id = document.getElementById('editContractId').value;
    const status = document.getElementById('editContractStatus').value;
    const price_agreed = parseFloat(document.getElementById('editContractPrice').value) || null;
    const notes = document.getElementById('editContractNotes').value.trim();

    try {
      const res = await TunaApp.apiFetch(`/api/contratos/${id}`, {
        method: 'PUT',
        body: { status, price_agreed, notes }
      });
      if (res.success) {
        TunaApp.showToast('Contrato actualizado con éxito.', 'success');
        TunaApp.closeModal('modalGestionContrato');
        loadContracts();
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  async function deleteContract(id) {
    if (!confirm(`¿Estás seguro de eliminar permanentemente la solicitud #${id}?`)) return;

    try {
      const res = await TunaApp.apiFetch(`/api/contratos/${id}`, { method: 'DELETE' });
      if (res.success) {
        TunaApp.showToast(`Contrato #${id} eliminado.`, 'info');
        loadContracts();
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  // ============================================================
  // GESTIÓN DE PRODUCTOS TIENDA
  // ============================================================
  async function loadAdminProducts() {
    const isAuthed = await checkAdminAuth();
    if (!isAuthed) return;

    try {
      const res = await TunaApp.apiFetch('/api/admin/tienda');
      const products = res.products || [];
      renderAdminProductsGrid(products);
    } catch (err) {
      TunaApp.showToast('Error cargando productos: ' + err.message, 'error');
    }
  }

  function renderAdminProductsGrid(products) {
    const grid = document.getElementById('adminProductsGrid');
    if (!grid) return;

    let html = '';
    products.forEach(p => {
      html += `
        <div class="product-card" style="background:#FFF; border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:20px; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
              <span style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-subtle);">${TunaApp.escapeHTML(p.category)}</span>
              <span class="status-badge ${p.is_active ? 'badge-green' : 'badge-red'}" style="font-size:10px; padding:2px 8px; border-radius:4px;">
                ${p.is_active ? 'Activo' : 'Oculto'}
              </span>
            </div>
            <h4 style="font-size:16px; font-weight:700; color:var(--text-main); margin-bottom:6px;">${TunaApp.escapeHTML(p.name)}</h4>
            <p style="font-size:13px; color:var(--text-muted); margin-bottom:12px; line-height:1.4;">${TunaApp.escapeHTML(p.description)}</p>
          </div>
          <div style="border-top:1px solid var(--border-color); padding-top:14px; margin-top:8px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <span style="font-size:20px; font-weight:800; color:var(--primary);">${parseFloat(p.price).toFixed(2)} €</span>
              <span style="font-size:12px; color:var(--text-subtle);">Stock: <strong>${p.stock}</strong></span>
            </div>
            <div style="display:flex; gap:8px;">
              <button onclick="TunaAdmin.openEditProductModal(${p.id}, '${TunaApp.escapeHTML(p.name)}', ${p.price}, ${p.stock})" class="btn btn-secondary" style="flex:1; padding:8px; font-size:12px;">Editar</button>
              <button onclick="TunaAdmin.deactivateProduct(${p.id})" class="btn" style="background:#FEE2E2; color:var(--primary); padding:8px 12px; font-size:12px;" title="Retirar">✕</button>
            </div>
          </div>
        </div>
      `;
    });

    grid.innerHTML = html;
  }

  function openEditProductModal(id, name, price, stock) {
    document.getElementById('editProdId').value = id;
    document.getElementById('editProdName').value = name;
    document.getElementById('editProdPrice').value = price;
    document.getElementById('editProdStock').value = stock;
    TunaApp.openModal('modalEditProduct');
  }

  async function saveProductEdit(e) {
    e.preventDefault();
    const id = document.getElementById('editProdId').value;
    const name = document.getElementById('editProdName').value.trim();
    const price = parseFloat(document.getElementById('editProdPrice').value);
    const stock = parseInt(document.getElementById('editProdStock').value);

    try {
      const res = await TunaApp.apiFetch(`/api/admin/tienda/${id}`, {
        method: 'PUT',
        body: { name, price, stock, is_active: 1 }
      });
      if (res.success) {
        TunaApp.showToast('Producto actualizado correctamente.', 'success');
        TunaApp.closeModal('modalEditProduct');
        loadAdminProducts();
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  async function deactivateProduct(id) {
    if (!confirm('¿Deseas retirar este producto del catálogo público?')) return;
    try {
      const res = await TunaApp.apiFetch(`/api/admin/tienda/${id}`, { method: 'DELETE' });
      if (res.success) {
        TunaApp.showToast('Producto retirado.', 'info');
        loadAdminProducts();
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  // ============================================================
  // GESTIÓN DE MIEMBROS
  // ============================================================
  async function loadAdminMembers() {
    const isAuthed = await checkAdminAuth();
    if (!isAuthed) return;

    try {
      const res = await TunaApp.apiFetch('/api/miembros');
      const members = res.members || [];
      renderAdminMembersGrid(members);
    } catch (err) {
      TunaApp.showToast('Error cargando miembros: ' + err.message, 'error');
    }
  }

  function renderAdminMembersGrid(members) {
    const container = document.getElementById('adminMembersGrid');
    if (!container) return;

    let html = '';
    members.forEach(m => {
      html += `
        <div class="member-admin-card" style="background:#FFF; border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:20px; display:flex; gap:16px; align-items:center;">
          <div style="width:56px; height:56px; border-radius:var(--radius-full); background:var(--primary-light); color:var(--primary); display:flex; align-items:center; justify-content:center; font-weight:800; font-size:18px; flex-shrink:0;">
            ${m.nickname.substring(0, 2).toUpperCase()}
          </div>
          <div style="flex:1;">
            <div style="display:flex; align-items:center; gap:8px;">
              <h4 style="font-size:16px; font-weight:800; color:var(--text-main);">${TunaApp.escapeHTML(m.nickname)}</h4>
              <span style="font-size:11px; padding:2px 8px; border-radius:var(--radius-full); background:var(--bg-alt); font-weight:700; color:var(--text-subtle);">${TunaApp.escapeHTML(m.category)}</span>
            </div>
            <div style="font-size:13px; color:var(--text-muted); font-weight:600;">${TunaApp.escapeHTML(m.real_name)}</div>
            <div style="font-size:12px; color:var(--primary); font-weight:700;">${TunaApp.escapeHTML(m.role_instrument)} · Promoción ${m.generation_year}</div>
          </div>
          <div>
            <button onclick="TunaAdmin.deleteMember(${m.id})" class="btn" style="background:#FEE2E2; color:var(--primary); padding:8px 12px; font-size:12px;" title="Eliminar">✕</button>
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
  }

  async function addMember(e) {
    e.preventDefault();
    const nickname = document.getElementById('newMemberNickname').value.trim();
    const real_name = document.getElementById('newMemberRealName').value.trim();
    const role_instrument = document.getElementById('newMemberRole').value.trim();
    const category = document.getElementById('newMemberCategory').value;
    const generation_year = parseInt(document.getElementById('newMemberYear').value) || 2026;
    const bio = document.getElementById('newMemberBio').value.trim();

    try {
      const res = await TunaApp.apiFetch('/api/admin/miembros', {
        method: 'POST',
        body: { nickname, real_name, role_instrument, category, generation_year, bio }
      });
      if (res.success) {
        TunaApp.showToast(`Miembro "${nickname}" incorporado con éxito.`, 'success');
        TunaApp.closeModal('modalAddMember');
        loadAdminMembers();
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  async function deleteMember(id) {
    if (!confirm('¿Seguro que deseas eliminar este integrante del directorio oficial?')) return;
    try {
      const res = await TunaApp.apiFetch(`/api/admin/miembros/${id}`, { method: 'DELETE' });
      if (res.success) {
        TunaApp.showToast('Miembro eliminado.', 'info');
        loadAdminMembers();
      }
    } catch (err) {
      TunaApp.showToast(err.message, 'error');
    }
  }

  return {
    checkAdminAuth,
    loadContracts,
    filterContracts,
    openContractModal,
    saveContractChanges,
    deleteContract,
    // Tienda
    loadAdminProducts,
    openEditProductModal,
    saveProductEdit,
    deactivateProduct,
    // Miembros
    loadAdminMembers,
    addMember,
    deleteMember
  };
})();

window.TunaAdmin = TunaAdmin;
