/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Módulo Administración (admin.js)
 * Conectado a la base de datos oficial
 */

const TunaAdmin = {
  clientName(userId, fallback) {
    const user = userId ? TunaDB.users.getById(userId) : null;
    return user ? `${user.nombre} ${user.apellidos || ''}`.trim() : (fallback || 'Cliente web');
  },

  contractRows(list) {
    const f = TunaApp.format;
    return list.map((c) => `
      <tr>
        <td><strong>${f.esc(c.id)}</strong></td>
        <td>${f.esc(this.clientName(c.userId, c.clientName))}</td>
        <td>${f.esc(c.service)}</td>
        <td>${f.esc(f.date(c.date))}</td>
        <td>${f.contractBadge(c.status)}</td>
        <td><a href="ContratoDetalle.html?id=${encodeURIComponent(c.id)}">Ver detalle</a></td>
      </tr>
    `).join('');
  },

  orderRows(list) {
    const f = TunaApp.format;
    return list.map((o) => `
      <tr>
        <td><strong>${f.esc(o.id)}</strong></td>
        <td>${f.esc(this.clientName(o.userId))}</td>
        <td>${f.esc(f.date(o.date))}</td>
        <td>${f.money(o.total)}</td>
        <td>${f.orderBadge(o.status)}</td>
        <td><a href="PedidoDetalle.html?id=${encodeURIComponent(o.id)}">Ver detalle</a></td>
      </tr>
    `).join('');
  },

  renderContractsList(tbody) {
    const list = TunaDB.contracts.getAll();
    TunaApp.format.setCount('admin-contracts-count', list.length, 'contrato', 'contratos');
    tbody.innerHTML = this.contractRows(list) || TunaApp.format.emptyRow(6, 'No hay contratos registrados.');
  },

  renderOrdersList(tbody) {
    const list = TunaDB.orders.getAll();
    TunaApp.format.setCount('admin-orders-count', list.length, 'pedido', 'pedidos');
    tbody.innerHTML = this.orderRows(list) || TunaApp.format.emptyRow(6, 'No hay pedidos registrados.');
  },

  // Panel: últimos contratos y pedidos
  renderDashboard() {
    const f = TunaApp.format;
    document.getElementById('admin-last-contracts').innerHTML = TunaDB.contracts.getAll().slice(0, 3).map((c) => `
      <tr>
        <td><strong>${f.esc(c.id)}</strong></td>
        <td>${f.esc(this.clientName(c.userId, c.clientName))}</td>
        <td>${f.contractBadge(c.status)}</td>
        <td><a href="ContratoDetalle.html?id=${encodeURIComponent(c.id)}">Ver</a></td>
      </tr>
    `).join('') || f.emptyRow(4, 'Sin contratos.');
    document.getElementById('admin-last-orders').innerHTML = TunaDB.orders.getAll().slice(0, 3).map((o) => `
      <tr>
        <td><strong>${f.esc(o.id)}</strong></td>
        <td>${f.esc(this.clientName(o.userId))}</td>
        <td>${f.orderBadge(o.status)}</td>
        <td><a href="PedidoDetalle.html?id=${encodeURIComponent(o.id)}">Ver</a></td>
      </tr>
    `).join('') || f.emptyRow(4, 'Sin pedidos.');
  },

  renderClientsList(tbody) {
    const f = TunaApp.format;
    const clients = TunaDB.users.getAll().filter((u) => u.rol === 'cliente');
    f.setCount('admin-clients-count', clients.length, 'cliente', 'clientes');
    tbody.innerHTML = clients.map((u) => `
      <tr>
        <td>${f.esc(`${u.nombre} ${u.apellidos || ''}`.trim())}</td>
        <td>${f.esc(u.email)}</td>
        <td>${f.esc(u.telefono)}</td>
        <td>${TunaDB.contracts.getByUser(u.id).length}</td>
        <td>${TunaDB.orders.getByUser(u.id).length}</td>
        <td><a href="FichaCliente.html?id=${encodeURIComponent(u.id)}">Ver ficha</a></td>
      </tr>
    `).join('') || f.emptyRow(6, 'No hay clientes registrados.');
  },

  // El identificador de usuario de la URL es numérico; sin cliente válido se avisa en vez de inventar datos
  getClientFromUrl() {
    const client = TunaDB.users.getById(Number(TunaApp.format.queryId()));
    if (!client || client.rol !== 'cliente') {
      TunaApp.format.notFound('Cliente no encontrado', 'Este cliente no existe.', 'Clientes.html', 'Volver a la cartera');
      return null;
    }
    return client;
  },

  renderClientFile() {
    const f = TunaApp.format;
    const client = this.getClientFromUrl();
    if (!client) return;
    f.fill({
      name: `${client.nombre} ${client.apellidos || ''}`.trim(),
      email: client.email,
      phone: client.telefono,
      since: f.date(client.fechaRegistro),
      contracts: TunaDB.contracts.getByUser(client.id).length,
      orders: TunaDB.orders.getByUser(client.id).length
    });
    const query = `?id=${encodeURIComponent(client.id)}`;
    document.querySelector('main a[href="ContratosCliente.html"]').href = `ContratosCliente.html${query}`;
    document.querySelector('main a[href="PedidosCliente.html"]').href = `PedidosCliente.html${query}`;
  },

  renderClientContracts(tbody) {
    const f = TunaApp.format;
    const client = this.getClientFromUrl();
    if (!client) return;
    f.fill({ name: `${client.nombre} ${client.apellidos || ''}`.trim() });
    document.querySelector('main a[href="FichaCliente.html"]').href = `FichaCliente.html?id=${encodeURIComponent(client.id)}`;
    tbody.innerHTML = TunaDB.contracts.getByUser(client.id).map((c) => `
      <tr>
        <td><strong>${f.esc(c.id)}</strong></td>
        <td>${f.esc(c.service)}</td>
        <td>${f.esc(f.date(c.date))}</td>
        <td>${f.contractBadge(c.status)}</td>
        <td><a href="ContratoDetalle.html?id=${encodeURIComponent(c.id)}">Ver contrato en detalle</a></td>
      </tr>
    `).join('') || f.emptyRow(5, 'Este cliente no tiene contratos.');
  },

  renderClientOrders(tbody) {
    const f = TunaApp.format;
    const client = this.getClientFromUrl();
    if (!client) return;
    f.fill({ name: `${client.nombre} ${client.apellidos || ''}`.trim() });
    document.querySelector('main a[href="FichaCliente.html"]').href = `FichaCliente.html?id=${encodeURIComponent(client.id)}`;
    tbody.innerHTML = TunaDB.orders.getByUser(client.id).map((o) => `
      <tr>
        <td><strong>${f.esc(o.id)}</strong></td>
        <td>${f.esc(f.date(o.date))}</td>
        <td>${f.money(o.total)}</td>
        <td>${f.orderBadge(o.status)}</td>
        <td><a href="PedidoDetalle.html?id=${encodeURIComponent(o.id)}">Ver pedido en detalle</a></td>
      </tr>
    `).join('') || f.emptyRow(5, 'Este cliente no tiene pedidos.');
  },

  // Enlace a la ficha del cliente, o solo su nombre si la solicitud se hizo sin cuenta
  fillClientLink(userId, fallback) {
    const link = document.querySelector('[data-field="client"]');
    link.textContent = this.clientName(userId, fallback);
    if (userId && TunaDB.users.getById(userId)) {
      link.href = `FichaCliente.html?id=${encodeURIComponent(userId)}`;
    } else {
      link.removeAttribute('href');
    }
  },

  // Selector de estado de los detalles: guarda en la base de datos y muestra confirmación
  bindStatusForm(currentStatus, save, label) {
    const select = document.getElementById('detail-status');
    select.value = currentStatus;
    document.getElementById('detail-status-save').addEventListener('click', () => {
      if (save(select.value)) {
        TunaApp.showToast(`${label} marcado como «${select.value}»`, 'success');
      }
    });
  },

  renderContractDetail() {
    const f = TunaApp.format;
    const contract = TunaDB.contracts.getById(f.queryId());
    if (!contract) {
      f.notFound('Contrato no encontrado', 'Este contrato no existe.', 'Contratos.html', 'Volver al listado');
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
    this.fillClientLink(contract.userId, contract.clientName);
    this.bindStatusForm(contract.status, (status) => TunaDB.contracts.updateStatus(contract.id, status), `Contrato ${contract.id}`);
  },

  renderOrderDetail() {
    const f = TunaApp.format;
    const order = TunaDB.orders.getById(f.queryId());
    if (!order) {
      f.notFound('Pedido no encontrado', 'Este pedido no existe.', 'Pedidos.html', 'Volver al listado');
      return;
    }
    f.fill({ title: `Pedido ${order.id}`, date: f.date(order.date), address: order.address });
    this.fillClientLink(order.userId);
    document.getElementById('detail-items').innerHTML = f.orderItemRows(order);

    const request = order.returnRequest;
    const returnInfo = document.getElementById('detail-return');
    if (request) {
      returnInfo.hidden = false;
      returnInfo.textContent = `Devolución solicitada: ${request.items.join(', ')}. Motivo: ${request.reason}.${request.comments ? ` Comentarios: ${request.comments}` : ''}`;
    }
    this.bindStatusForm(order.status, (status) => TunaDB.orders.updateStatus(order.id, status), `Pedido ${order.id}`);
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const el = (id) => document.getElementById(id);
  const page = window.location.pathname.split('/').pop();

  if (el('admin-contracts-tbody')) TunaAdmin.renderContractsList(el('admin-contracts-tbody'));
  if (el('admin-orders-tbody')) TunaAdmin.renderOrdersList(el('admin-orders-tbody'));
  if (el('admin-last-contracts')) TunaAdmin.renderDashboard();
  if (el('admin-clients-tbody')) TunaAdmin.renderClientsList(el('admin-clients-tbody'));
  if (el('admin-client-contracts-tbody')) TunaAdmin.renderClientContracts(el('admin-client-contracts-tbody'));
  if (el('admin-client-orders-tbody')) TunaAdmin.renderClientOrders(el('admin-client-orders-tbody'));
  if (page === 'FichaCliente.html') TunaAdmin.renderClientFile();
  if (page === 'ContratoDetalle.html') TunaAdmin.renderContractDetail();
  if (page === 'PedidoDetalle.html') TunaAdmin.renderOrderDetail();
});
