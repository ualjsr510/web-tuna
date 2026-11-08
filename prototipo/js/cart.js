/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Módulo Cesta de la Compra y Flujo Checkout (cart.js)
 * Conectado a la base de datos
 */

// Asegurar que el carrito comience vacío por defecto
if (!localStorage.getItem('tuna_cart_initialized_empty_v1')) {
  localStorage.setItem('tuna_cart', JSON.stringify([]));
  localStorage.setItem('tuna_cart_initialized_empty_v1', 'true');
}

const TunaCart = {
  getCart() {
    let cart = localStorage.getItem('tuna_cart');
    if (!cart) {
      cart = [];
      localStorage.setItem('tuna_cart', JSON.stringify(cart));
    } else {
      try {
        cart = JSON.parse(cart);
      } catch (e) {
        cart = [];
      }
    }
    return cart;
  },

  saveCart(cart) {
    localStorage.setItem('tuna_cart', JSON.stringify(cart));
    this.updateHeaderBadge();
    this.renderMiniCheckoutSummary();
  },

  addItem(product) {
    const cart = this.getCart();
    const existing = cart.find(item => item.id === product.id && item.size === product.size);
    if (existing) {
      existing.qty = (existing.qty || 1) + (product.qty || 1);
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        price: parseFloat(product.price),
        qty: parseInt(product.qty) || 1,
        size: product.size || 'M',
        img: product.img || '../assets/img/prod_capa.jpg'
      });
    }
    this.saveCart(cart);
    TunaApp.showToast(`«${product.name}» añadido a la cesta`, 'success');
  },

  removeItem(index) {
    const cart = this.getCart();
    const removed = cart.splice(index, 1);
    this.saveCart(cart);
    if (removed.length > 0) {
      TunaApp.showToast(`«${removed[0].name}» eliminado de la cesta`, 'info');
    }
    this.renderCartPage();
    this.renderMiniCheckoutSummary();
  },

  updateQty(index, delta) {
    const cart = this.getCart();
    if (cart[index]) {
      cart[index].qty = Math.max(1, (cart[index].qty || 1) + delta);
      this.saveCart(cart);
      this.renderCartPage();
      this.renderMiniCheckoutSummary();
    }
  },

  updateHeaderBadge() {
    const cart = this.getCart();
    const count = cart.reduce((acc, it) => acc + (it.qty || 1), 0);
    document.querySelectorAll('.cart-counter-val').forEach(el => {
      el.textContent = count;
    });
  },

  renderCartPage() {
    const tableBody = document.getElementById('cart-items-body');
    const emptyMsg = document.getElementById('cart-empty-state');
    const cartContent = document.getElementById('cart-content-wrapper');
    const subtotalEl = document.getElementById('cart-subtotal-val');
    const shippingEl = document.getElementById('cart-shipping-val');
    const totalEl = document.getElementById('cart-total-val');

    if (!tableBody) return;

    const cart = this.getCart();
    if (cart.length === 0) {
      if (emptyMsg) emptyMsg.style.display = 'block';
      if (cartContent) cartContent.style.display = 'none';
      return;
    }

    if (emptyMsg) emptyMsg.style.display = 'none';
    if (cartContent) cartContent.style.display = 'flex';

    tableBody.innerHTML = '';
    let subtotal = 0;

    cart.forEach((item, idx) => {
      const lineTotal = item.price * item.qty;
      subtotal += lineTotal;
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td style="display:flex; align-items:center; gap:14px; padding:12px;">
          <div class="tuna-photo-frame" style="width:58px; height:58px; flex:none; border-radius:6px; border:1px solid var(--line);">
            <img src="${item.img}" alt="${item.name}">
          </div>
          <div>
            <strong style="color:var(--ink); font-size:14px; display:block;">${item.name}</strong>
            <span style="font-size:11.5px; color:var(--muted);">Opción/Talla: ${item.size}</span>
          </div>
        </td>
        <td style="font-weight:600; padding:12px;">${item.price.toFixed(2)} €</td>
        <td style="padding:12px;">
          <div style="display:inline-flex; align-items:center; border:1px solid var(--line); border-radius:5px; background:var(--card);">
            <button type="button" onclick="TunaCart.updateQty(${idx}, -1)" style="border:none; background:none; padding:4px 10px; cursor:pointer; font-weight:bold;">−</button>
            <span style="padding:4px 8px; font-weight:700; min-width:24px; text-align:center;">${item.qty}</span>
            <button type="button" onclick="TunaCart.updateQty(${idx}, 1)" style="border:none; background:none; padding:4px 10px; cursor:pointer; font-weight:bold;">+</button>
          </div>
        </td>
        <td style="font-weight:700; color:var(--accent); padding:12px;">${lineTotal.toFixed(2)} €</td>
        <td style="padding:12px;">
          <button type="button" onclick="TunaCart.removeItem(${idx})" title="Eliminar producto" style="border:none; background:none; color:#c92a2a; cursor:pointer; font-size:16px;">🗑</button>
        </td>
      `;
      tableBody.appendChild(tr);
    });

    const shipping = subtotal > 40 ? 0.00 : 4.50;
    const total = subtotal + shipping;

    if (subtotalEl) subtotalEl.textContent = subtotal.toFixed(2) + ' €';
    if (shippingEl) shippingEl.textContent = shipping === 0 ? 'Gratis (Promoción)' : shipping.toFixed(2) + ' €';
    if (totalEl) totalEl.textContent = total.toFixed(2) + ' €';
  },

  renderMiniCheckoutSummary() {
    const container = document.getElementById('checkout-mini-items');
    const subtotalEl = document.getElementById('checkout-subtotal-val');
    const shippingEl = document.getElementById('checkout-shipping-val');
    const totalEl = document.getElementById('checkout-total-val');

    if (!container) return;

    const cart = this.getCart();
    if (cart.length === 0) {
      container.innerHTML = '<p style="color:var(--muted); font-size:12px; margin:0;">Cesta vacía</p>';
      if (subtotalEl) subtotalEl.textContent = '0.00 €';
      if (totalEl) totalEl.textContent = '0.00 €';
      return;
    }

    let subtotal = 0;
    container.innerHTML = cart.map(item => {
      const lineTotal = item.price * item.qty;
      subtotal += lineTotal;
      return `
        <div style="display:flex; justify-content:space-between; align-items:center; gap:10px; font-size:12.5px; padding-bottom:6px; border-bottom:1px solid var(--line-soft);">
          <div style="display:flex; align-items:center; gap:8px; min-width:0;">
            <span style="font-weight:700; color:var(--accent);">${item.qty}x</span>
            <span style="white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:170px; color:var(--ink);">${item.name}</span>
          </div>
          <strong style="color:var(--ink); flex:none;">${lineTotal.toFixed(2)} €</strong>
        </div>
      `;
    }).join('');

    const shipping = subtotal > 40 ? 0.00 : 4.50;
    const total = subtotal + shipping;

    if (subtotalEl) subtotalEl.textContent = subtotal.toFixed(2) + ' €';
    if (shippingEl) shippingEl.textContent = shipping === 0 ? 'Gratis' : shipping.toFixed(2) + ' €';
    if (totalEl) totalEl.textContent = total.toFixed(2) + ' €';
  },

  // Guardar dirección de envío temporal
  saveShippingAddress(addr) {
    localStorage.setItem('tuna_checkout_address', typeof addr === 'string' ? addr : JSON.stringify(addr));
  },

  getShippingAddress() {
    const raw = localStorage.getItem('tuna_checkout_address');
    if (!raw) {
      return {
        name: 'Marta Gil Sánchez',
        street: 'Calle Real 12, 2ºB',
        city: 'Almería',
        postalCode: '04001',
        province: 'Almería',
        phone: '685 99 55 10',
        shippingType: 'standard'
      };
    }
    try {
      return JSON.parse(raw);
    } catch(e) {
      return { street: raw, name: 'Cliente', city: 'Almería', postalCode: '04001', phone: '685 99 55 10' };
    }
  },

  // Guardar método de pago seleccionado
  savePaymentMethod(method) {
    localStorage.setItem('tuna_checkout_payment', method);
  },

  getPaymentMethod() {
    return localStorage.getItem('tuna_checkout_payment') || 'Tarjeta de crédito / débito (Visa / Mastercard)';
  },

  // Finalizar pedido y guardar en la base de datos
  submitCheckoutOrder(shippingAddress, paymentMethod) {
    const cart = this.getCart();
    if (cart.length === 0) {
      // Si la cesta ya se vació porque se recargó la confirmación, usar el último pedido
      const last = localStorage.getItem('tuna_last_confirmed_order');
      if (last) {
        try { return JSON.parse(last); } catch(e){}
      }
      return null;
    }

    let subtotal = 0;
    cart.forEach(i => subtotal += (i.price * i.qty));
    const shipping = subtotal > 40 ? 0 : 4.50;
    const total = subtotal + shipping;

    const addrObj = this.getShippingAddress();
    const formattedAddr = typeof shippingAddress === 'string' 
      ? shippingAddress 
      : `${addrObj.street || 'Calle Real 12'}, ${addrObj.postalCode || '04001'} ${addrObj.city || 'Almería'} (${addrObj.name || 'Marta Gil'})`;

    const chosenPayment = paymentMethod || this.getPaymentMethod();

    const newOrder = TunaDB.orders.create({
      subtotal: subtotal,
      shipping: shipping,
      total: total,
      address: formattedAddr,
      paymentMethod: chosenPayment,
      items: cart
    });

    // Guardar el último pedido confirmado para el recibo
    localStorage.setItem('tuna_last_confirmed_order', JSON.stringify(newOrder));

    // Vaciar carrito
    localStorage.removeItem('tuna_cart');
    this.updateHeaderBadge();
    return newOrder;
  },

  // Renderizar la tabla de revisión para el Paso 4 (ConfirmacionPedido.html)
  renderReviewPage() {
    const container = document.getElementById('review-items-body');
    const addrEl = document.getElementById('review-address-text');
    const paymentEl = document.getElementById('review-payment-text');
    const subtotalEl = document.getElementById('review-subtotal-val');
    const shippingEl = document.getElementById('review-shipping-val');
    const totalEl = document.getElementById('review-total-val');
    const btnSubmit = document.getElementById('btn-confirm-order');

    const cart = this.getCart();
    const addr = this.getShippingAddress();
    const payment = this.getPaymentMethod();

    if (addrEl) {
      addrEl.innerHTML = `
        <strong>${addr.name || 'Marta Gil Sánchez'}</strong><br>
        ${addr.street || 'Calle Real 12, 2ºB'}<br>
        ${addr.postalCode || '04001'} ${addr.city || 'Almería'}, ${addr.province || 'Almería'}<br>
        <span style="color:var(--muted); font-size:12px;">📞 ${addr.phone || '685 99 55 10'}</span>
      `;
    }

    if (paymentEl) {
      paymentEl.textContent = payment;
    }

    if (container) {
      if (cart.length === 0) {
        container.innerHTML = `<tr><td colspan="4" style="text-align:center; padding:20px; color:var(--muted);">No hay artículos en la cesta</td></tr>`;
      } else {
        let subtotal = 0;
        container.innerHTML = cart.map(item => {
          const lineTotal = item.price * item.qty;
          subtotal += lineTotal;
          return `
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:12px; display:flex; align-items:center; gap:12px;">
                <img src="${item.img}" alt="${item.name}" style="width:48px; height:48px; object-fit:cover; border-radius:4px; border:1px solid var(--line);">
                <div>
                  <strong style="color:var(--ink); font-size:13.5px; display:block;">${item.name}</strong>
                  <span style="font-size:11.5px; color:var(--muted);">Talla/Opción: ${item.size}</span>
                </div>
              </td>
              <td style="padding:12px; font-size:13px;">${item.price.toFixed(2)} €</td>
              <td style="padding:12px; font-weight:700; text-align:center;">${item.qty}</td>
              <td style="padding:12px; font-weight:700; color:var(--accent); text-align:right;">${lineTotal.toFixed(2)} €</td>
            </tr>
          `;
        }).join('');

        const shipping = subtotal > 40 ? 0.00 : 4.50;
        const total = subtotal + shipping;

        if (subtotalEl) subtotalEl.textContent = subtotal.toFixed(2) + ' €';
        if (shippingEl) shippingEl.textContent = shipping === 0 ? 'Gratis (Promoción)' : shipping.toFixed(2) + ' €';
        if (totalEl) totalEl.textContent = total.toFixed(2) + ' €';
        if (btnSubmit) btnSubmit.textContent = `🔒 Formalizar y Pagar Pedido (${total.toFixed(2)} €)`;
      }
    }
  },

  // Renderizar el recibo oficial para el Paso 5 (ReciboPedido.html)
  renderReceiptPage() {
    const raw = localStorage.getItem('tuna_last_confirmed_order');
    let order = null;
    if (raw) {
      try { order = JSON.parse(raw); } catch(e){}
    }
    if (!order) {
      // Tomar el más reciente de TunaDB
      const all = TunaDB.orders.getAll();
      order = all[all.length - 1] || {
        id: 'PED-2026-003',
        date: new Date().toLocaleDateString('es-ES'),
        total: 37.00,
        subtotal: 37.00,
        shipping: 0,
        address: 'Calle Real 12, 04001 Almería (Marta Gil)',
        paymentMethod: 'Tarjeta de crédito / débito',
        items: [
          { name: 'Capa tradicional de paño', price: 25.00, qty: 1, size: 'M' },
          { name: 'CD XXV Aniversario', price: 12.00, qty: 1, size: 'Estándar' }
        ]
      };
    }

    const orderIdEl = document.getElementById('receipt-order-id');
    const orderDateEl = document.getElementById('receipt-order-date');
    const orderTotalEl = document.getElementById('receipt-order-total');
    const orderSubtotalEl = document.getElementById('receipt-order-subtotal');
    const orderShippingEl = document.getElementById('receipt-order-shipping');
    const orderAddressEl = document.getElementById('receipt-order-address');
    const orderPaymentEl = document.getElementById('receipt-order-payment');
    const itemsTbody = document.getElementById('receipt-items-tbody');

    if (orderIdEl) orderIdEl.textContent = order.id;
    if (orderDateEl) orderDateEl.textContent = order.date;
    if (orderTotalEl) orderTotalEl.textContent = (order.total || 0).toFixed(2) + ' €';
    if (orderSubtotalEl) orderSubtotalEl.textContent = (order.subtotal || order.total || 0).toFixed(2) + ' €';
    if (orderShippingEl) orderShippingEl.textContent = (order.shipping === 0 || !order.shipping) ? '0.00 € (Gratis)' : order.shipping.toFixed(2) + ' €';
    if (orderAddressEl) orderAddressEl.textContent = order.address || 'Calle Real 12, 04001 Almería';
    if (orderPaymentEl) orderPaymentEl.textContent = order.paymentMethod || 'Tarjeta de crédito';

    if (itemsTbody && order.items) {
      itemsTbody.innerHTML = order.items.map(item => `
        <tr style="border-bottom:1px solid var(--line);">
          <td style="padding:10px 12px; font-size:13px; font-weight:600; color:var(--ink);">
            ${item.name}
            <span style="display:block; font-size:11px; color:var(--muted); font-weight:normal;">Opción/Talla: ${item.size || 'Estándar'}</span>
          </td>
          <td style="padding:10px 12px; font-size:13px; text-align:center;">${item.qty || 1}</td>
          <td style="padding:10px 12px; font-size:13px; text-align:right;">${(item.price || 0).toFixed(2)} €</td>
          <td style="padding:10px 12px; font-size:13px; font-weight:700; color:var(--accent); text-align:right;">
            ${((item.price || 0) * (item.qty || 1)).toFixed(2)} €
          </td>
        </tr>
      `).join('');
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  TunaCart.updateHeaderBadge();
  TunaCart.renderCartPage();
  TunaCart.renderMiniCheckoutSummary();
  if (document.getElementById('review-items-body')) {
    TunaCart.renderReviewPage();
  }
  if (document.getElementById('receipt-order-id')) {
    TunaCart.renderReceiptPage();
  }
});
