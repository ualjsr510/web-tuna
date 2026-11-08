/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Módulo Administración (admin.js)
 * Conectado a la base de datos oficial
 */

const TunaAdmin = {
  renderContractsTable() {
    const tbody = document.getElementById('admin-contracts-tbody');
    if (!tbody) return;
    const list = TunaDB.contracts.getAll();
    
    if (list.length === 0) {
      tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:20px; color:var(--muted);">No hay contratos registrados en la base de datos.</td></tr>';
      return;
    }

    tbody.innerHTML = list.map(c => `
      <tr>
        <td><strong>${c.id}</strong></td>
        <td>${c.clientName || 'Cliente Web'}</td>
        <td>${c.service}</td>
        <td>${c.date}</td>
        <td><span class="badge ${c.status === 'Confirmado' ? 'badge-ok' : (c.status === 'Pendiente' ? 'badge-warn' : 'badge-info')}">${c.status}</span></td>
        <td><span class="badge-custom-budget" style="font-size:11.5px; padding:3px 8px;">${c.price || 'A convenir'}</span></td>
        <td>
          <div style="display:flex; gap:6px;">
            <button type="button" class="btn btn-outline" style="padding:4px 8px; font-size:11px;" onclick="TunaAdmin.updateContractStatus('${c.id}', 'Confirmado')">Aprobar</button>
            <button type="button" class="btn btn-outline" style="padding:4px 8px; font-size:11px; color:#c92a2a;" onclick="TunaAdmin.updateContractStatus('${c.id}', 'Cancelado')">Rechazar</button>
          </div>
        </td>
      </tr>
    `).join('');
  },

  updateContractStatus(id, newStatus) {
    if (TunaDB.contracts.updateStatus(id, newStatus)) {
      TunaApp.showToast(`Contrato ${id} marcado como «${newStatus}»`, 'success');
      this.renderContractsTable();
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('admin-contracts-tbody')) {
    TunaAdmin.renderContractsTable();
  }
});
