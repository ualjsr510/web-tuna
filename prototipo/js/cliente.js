/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Módulo Área de Cliente (cliente.js)
 * Cada cliente solo ve y modifica sus propios contratos y pedidos
 */

const TunaCliente = {
  EDITABLE_ORDER_STATUSES: ['Pendiente', 'En preparación'],
  ORDER_STEPS: ['Recibido', 'En preparación', 'Enviado', 'Entregado'],
  ORDER_STEP_BY_STATUS: { Pendiente: 0, 'En preparación': 1, Enviado: 2, Entregado: 3 },

  getOwnContract(user) {
    const contract = TunaDB.contracts.getById(TunaApp.format.queryId());
    return contract && contract.userId === user.id ? contract : null;
  },

  getOwnOrder(user) {
    const order = TunaDB.orders.getById(TunaApp.format.queryId());
    return order && order.userId === user.id ? order : null;
  },

  renderEmptyCard(card, title, text, href, cta) {
    card.innerHTML = `
      <h2 class="client-card-title">${title}</h2>
      <p class="client-card-text">${text}</p>
      <a href="${href}" class="btn btn-outline client-card-link">${cta}</a>
    `;
  },

  // Inicio: próxima actuación (o la última, si no hay ninguna por venir)
  renderNextEvent(card, user) {
    const f = TunaApp.format;
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const contracts = TunaDB.contracts.getByUser(user.id)
      .filter((c) => c.status !== 'Rechazado' && !Number.isNaN(f.parseDay(c.date).getTime()))
      .sort((a, b) => a.date.localeCompare(b.date));
    const upcoming = contracts.filter((c) => c.status !== 'Realizado' && f.parseDay(c.date) >= today);
    const contract = upcoming[0] || contracts[contracts.length - 1];

    if (!contract) {
      this.renderEmptyCard(card, 'Próxima actuación', 'Todavía no tienes ninguna actuación contratada.', '../visitante/Contratacion.html', 'Contratar a la tuna');
      return;
    }

    const isUpcoming = contract === upcoming[0];
    const days = Math.round((f.parseDay(contract.date) - today) / 86400000);
    const countdown = days === 0 ? '<strong>¡Es hoy!</strong>'
      : days === 1 ? '<strong>Mañana</strong>'
      : `<span>Faltan</span><strong>${days}</strong><span>días</span>`;

    card.innerHTML = `
      <div class="client-card-head">
        <h2 class="client-card-title">${isUpcoming ? 'Próxima actuación' : 'Última actuación'}</h2>
        ${f.contractBadge(contract.status)}
      </div>
      <div class="client-event">
        ${isUpcoming ? `<div class="client-countdown">${countdown}</div>` : ''}
        <div class="client-event-info">
          <h3>${f.esc(contract.service)}</h3>
          <p>${f.esc(f.longDate(contract.date))}${contract.time ? ` · ${f.esc(contract.time)} h` : ''}</p>
          <p>${f.esc(contract.location)}</p>
        </div>
      </div>
      <a href="ContratoDetalle.html?id=${encodeURIComponent(contract.id)}" class="btn btn-outline client-card-link">Ver contrato</a>
    `;
  },

  // Inicio: seguimiento del último pedido (los pedidos nuevos se guardan al principio de la lista)
  renderLastOrder(card, user) {
    const f = TunaApp.format;
    const order = TunaDB.orders.getByUser(user.id)[0];

    if (!order) {
      this.renderEmptyCard(card, 'Tu último pedido', 'Todavía no has hecho ningún pedido.', '../visitante/Tienda.html', 'Ir a la tienda');
      return;
    }

    const step = this.ORDER_STEP_BY_STATUS[order.status];
    // Estados fuera del recorrido normal (devoluciones): solo se muestra la etiqueta
    const tracking = step === undefined
      ? `<p class="client-card-text">Estado actual: ${f.orderBadge(order.status)}</p>`
      : `<ol class="order-tracker">${this.ORDER_STEPS.map((label, i) => `
          <li class="${i < step ? 'is-done' : ''}${i === step ? 'is-current' : ''}"${i === step ? ' aria-current="step"' : ''}>${label}</li>
        `).join('')}</ol>`;
    const items = (order.items || []).map((item) => f.esc(item.name)).join(', ');

    card.innerHTML = `
      <div class="client-card-head">
        <h2 class="client-card-title">Tu último pedido</h2>
        <strong class="client-order-total">${f.money(order.total)}</strong>
      </div>
      <p class="client-card-text">${f.esc(order.id)} · ${f.esc(f.longDate(order.date))}</p>
      ${tracking}
      ${items ? `<p class="client-card-text">${items}</p>` : ''}
      <a href="PedidoDetalle.html?id=${encodeURIComponent(order.id)}" class="btn btn-outline client-card-link">Ver pedido</a>
    `;
  },

  renderContractsList(tbody, user) {
    const f = TunaApp.format;
    const contracts = TunaDB.contracts.getByUser(user.id);
    f.setCount('client-contracts-count', contracts.length, 'contrato', 'contratos');
    tbody.innerHTML = contracts.map((c) => `
      <tr>
        <td><strong>${f.esc(c.id)}</strong></td>
        <td>${f.esc(c.service)}</td>
        <td>${f.esc(f.date(c.date))}</td>
        <td>${f.contractBadge(c.status)}</td>
        <td><a href="ContratoDetalle.html?id=${encodeURIComponent(c.id)}">Ver detalle</a></td>
      </tr>
    `).join('') || f.emptyRow(5, 'Todavía no has solicitado ninguna actuación.');
  },

  renderOrdersList(tbody, user) {
    const f = TunaApp.format;
    const orders = TunaDB.orders.getByUser(user.id);
    f.setCount('client-orders-count', orders.length, 'pedido', 'pedidos');
    tbody.innerHTML = orders.map((o) => `
      <tr>
        <td><strong>${f.esc(o.id)}</strong></td>
        <td>${f.esc(f.date(o.date))}</td>
        <td>${f.money(o.total)}</td>
        <td>${f.orderBadge(o.status)}</td>
        <td><a href="PedidoDetalle.html?id=${encodeURIComponent(o.id)}">Ver detalle</a></td>
      </tr>
    `).join('') || f.emptyRow(5, 'Todavía no has hecho ningún pedido.');
  },

  renderContractDetail(user) {
    const f = TunaApp.format;
    const contract = this.getOwnContract(user);
    if (!contract) {
      f.notFound('Contrato no encontrado', 'Este contrato no existe o no pertenece a tu cuenta.', 'Contratos.html', 'Volver al historial');
      return;
    }
    f.fill({
      title: `Contrato ${contract.id}`,
      service: contract.service,
      datetime: `${f.date(contract.date)} ${contract.time || ''}`.trim(),
      location: contract.location,
      guests: contract.guests,
      notes: contract.notes || 'Sin observaciones',
      price: contract.price
    });
    document.querySelector('[data-field="status"]').innerHTML = f.contractBadge(contract.status);
  },

  renderOrderDetail(user) {
    const f = TunaApp.format;
    const order = this.getOwnOrder(user);
    if (!order) {
      f.notFound('Pedido no encontrado', 'Este pedido no existe o no pertenece a tu cuenta.', 'Pedidos.html', 'Volver al historial');
      return;
    }
    f.fill({ title: `Pedido ${order.id}`, date: f.date(order.date), address: order.address });
    document.querySelector('[data-field="status"]').innerHTML = f.orderBadge(order.status);
    document.getElementById('detail-items').innerHTML = f.orderItemRows(order);

    // Cada acción solo aparece cuando el estado del pedido la permite
    const query = `?id=${encodeURIComponent(order.id)}`;
    const setAction = (page, allowed) => {
      const link = document.querySelector(`main a[href="${page}"]`);
      link.href = page + query;
      link.parentElement.style.display = allowed ? '' : 'none';
    };
    setAction('PedidoEditar.html', this.EDITABLE_ORDER_STATUSES.includes(order.status));
    setAction('PedidoDevolucion.html', order.status === 'Entregado');
  },

  // Los enlaces fijos a "PedidoDetalle.html" (barra de retorno, migas, cancelar) deben llevar al pedido actual
  linkOrderDetail(order) {
    const detailUrl = `PedidoDetalle.html?id=${encodeURIComponent(order.id)}`;
    document.querySelectorAll('a[href="PedidoDetalle.html"]').forEach((link) => {
      link.href = detailUrl;
      if (link.hasAttribute('onclick')) {
        link.setAttribute('onclick', `TunaApp.goBack('${detailUrl}')`);
      }
    });
  },

  // Formularios de pedido: mensaje común si el pedido ya no admite la acción
  blockOrderForm(title, order, message) {
    TunaApp.format.notFound(title, message, `PedidoDetalle.html?id=${encodeURIComponent(order.id)}`, 'Volver al pedido');
  },

  renderOrderEdit(user) {
    const f = TunaApp.format;
    const order = this.getOwnOrder(user);
    if (!order) {
      f.notFound('Pedido no encontrado', 'Este pedido no existe o no pertenece a tu cuenta.', 'Pedidos.html', 'Volver al historial');
      return;
    }
    this.linkOrderDetail(order);
    if (!this.EDITABLE_ORDER_STATUSES.includes(order.status)) {
      this.blockOrderForm('Editar datos del pedido', order, `El pedido está «${order.status}» y ya no se puede editar.`);
      return;
    }

    const detailUrl = `PedidoDetalle.html?id=${encodeURIComponent(order.id)}`;
    f.fill({ title: `Pedido ${order.id}` });

    // La dirección se guarda como un solo texto: "calle, 04001 Ciudad"
    const parts = /^(.*),\s*(\d{5})\s+(.+)$/.exec(order.address || '');
    const field = (id) => document.getElementById(id);
    field('edit-name').value = order.recipient || `${user.nombre} ${user.apellidos || ''}`.trim();
    field('edit-address').value = parts ? parts[1] : order.address || '';
    field('edit-postcode').value = parts ? parts[2] : '';
    field('edit-city').value = parts ? parts[3] : '';
    field('edit-phone').value = order.phone || user.telefono || '';

    field('edit-save').addEventListener('click', () => {
      const address = field('edit-address').value.trim();
      const city = field('edit-city').value.trim();
      const postcode = field('edit-postcode').value.trim();
      if (!address || !city || !/^\d{5}$/.test(postcode)) {
        TunaApp.showToast('Indica la dirección, la ciudad y un código postal de 5 cifras.', 'error');
        return;
      }
      TunaDB.orders.update(order.id, {
        recipient: field('edit-name').value.trim(),
        phone: field('edit-phone').value.trim(),
        address: `${address}, ${postcode} ${city}`
      });
      TunaApp.showToast('Datos del pedido actualizados', 'success');
      setTimeout(() => { window.location.href = detailUrl; }, 600);
    });
  },

  renderOrderReturn(user) {
    const f = TunaApp.format;
    const order = this.getOwnOrder(user);
    if (!order) {
      f.notFound('Pedido no encontrado', 'Este pedido no existe o no pertenece a tu cuenta.', 'Pedidos.html', 'Volver al historial');
      return;
    }
    this.linkOrderDetail(order);
    if (order.status !== 'Entregado') {
      this.blockOrderForm('Tramitar devolución', order, `El pedido está «${order.status}»: solo se pueden devolver pedidos entregados.`);
      return;
    }

    const detailUrl = `PedidoDetalle.html?id=${encodeURIComponent(order.id)}`;
    f.fill({ title: `Pedido ${order.id}` });
    document.getElementById('return-items').innerHTML = (order.items || []).map((item, i) => `
      <label class="return-item"><input type="checkbox" value="${i}"> ${f.esc(item.name)} × ${f.esc(item.qty)}</label>
    `).join('');

    document.getElementById('return-submit').addEventListener('click', () => {
      const selected = [...document.querySelectorAll('#return-items input:checked')].map((box) => order.items[Number(box.value)].name);
      const reason = document.getElementById('return-reason').value;
      if (selected.length === 0 || !reason) {
        TunaApp.showToast('Selecciona al menos un producto y el motivo.', 'error');
        return;
      }
      TunaDB.orders.update(order.id, {
        status: 'Devolución solicitada',
        returnRequest: { items: selected, reason, comments: document.getElementById('return-comments').value.trim() }
      });
      TunaApp.showToast('Devolución solicitada', 'success');
      setTimeout(() => { window.location.href = detailUrl; }, 600);
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const user = TunaDB.auth.getCurrentUser();
  if (!user) return; // la protección de rutas ya redirige al acceso

  const el = (id) => document.getElementById(id);
  const page = window.location.pathname.split('/').pop();

  if (el('client-next-event')) {
    el('client-greeting').textContent = `Hola, ${user.nombre}`;
    TunaCliente.renderNextEvent(el('client-next-event'), user);
    TunaCliente.renderLastOrder(el('client-last-order'), user);
  }
  if (el('client-contracts-tbody')) TunaCliente.renderContractsList(el('client-contracts-tbody'), user);
  if (el('client-orders-tbody')) TunaCliente.renderOrdersList(el('client-orders-tbody'), user);
  if (page === 'ContratoDetalle.html') TunaCliente.renderContractDetail(user);
  if (page === 'PedidoDetalle.html') TunaCliente.renderOrderDetail(user);
  if (page === 'PedidoEditar.html') TunaCliente.renderOrderEdit(user);
  if (page === 'PedidoDevolucion.html') TunaCliente.renderOrderReturn(user);
});
