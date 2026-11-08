/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Módulo Catálogo (catalog.js)
 * Proporciona filtrado en tiempo real, cambio de categorías, selección de fichas y carrito
 */

let currentFilterCat = 'todos';

// Funciones globales compatibles con los eventos del HTML
function setCategoryTab(cat) {
  currentFilterCat = cat;
  
  // Actualizar estilos visuales de los botones de categoría
  document.querySelectorAll('button[onclick*="setCategoryTab"]').forEach(btn => {
    if (btn.getAttribute('onclick').includes(`'${cat}'`)) {
      btn.style.background = 'var(--accent)';
      btn.style.color = '#fff';
      btn.style.borderColor = 'var(--accent)';
    } else {
      btn.style.background = 'var(--soft)';
      btn.style.color = 'var(--ink)';
      btn.style.borderColor = 'var(--line)';
    }
  });

  const catSelect = document.getElementById('cat-select');
  if (catSelect) catSelect.value = cat;

  filterCatalog();
}

function filterCatalog() {
  const searchInput = document.getElementById('cat-search');
  const catSelect = document.getElementById('cat-select');
  const priceSelect = document.getElementById('price-select');
  const stockCheck = document.getElementById('stock-only');

  const searchTerm = (searchInput ? searchInput.value : '').toLowerCase().trim();
  const selectedCat = catSelect ? catSelect.value : currentFilterCat;
  const selectedPrice = priceSelect ? priceSelect.value : 'all';
  const onlyStock = stockCheck ? stockCheck.checked : false;

  const cards = document.querySelectorAll('.catalog-card, .catalog-card-item');
  let visibleCount = 0;

  cards.forEach(card => {
    const title = (card.getAttribute('data-name') || card.getAttribute('data-title') || '').toLowerCase();
    const cat = card.getAttribute('data-cat') || '';
    const price = parseFloat(card.getAttribute('data-price') || '0');
    const inStock = card.getAttribute('data-stock') !== 'false';

    let matchSearch = !searchTerm || title.includes(searchTerm);
    let matchCat = selectedCat === 'todos' || selectedCat === '' || cat === selectedCat;
    
    let matchPrice = true;
    if (selectedPrice === '0-10' || selectedPrice === 'under10') matchPrice = price <= 10;
    else if (selectedPrice === '10-20' || selectedPrice === '10to20') matchPrice = price > 10 && price <= 20;
    else if (selectedPrice === '20+' || selectedPrice === 'over20') matchPrice = price > 20;

    let matchStock = !onlyStock || inStock;

    if (matchSearch && matchCat && matchPrice && matchStock) {
      card.style.display = 'flex';
      visibleCount++;
    } else {
      card.style.display = 'none';
    }
  });

  const countBadge = document.getElementById('catalog-results-badge');
  if (countBadge) {
    countBadge.textContent = `${visibleCount} productos encontrados`;
  }
}

function selectCatalogProduct(id, name, price, img, desc, sizesStr) {
  const titleEl = document.getElementById('cat-detail-title');
  const priceEl = document.getElementById('cat-detail-price');
  const imgEl = document.getElementById('cat-detail-img');
  const descEl = document.getElementById('cat-detail-desc');
  const sizeSel = document.getElementById('cat-detail-size');

  if (titleEl) titleEl.textContent = name;
  if (priceEl) priceEl.textContent = price.toFixed(2) + ' €';
  if (imgEl) imgEl.src = img;
  if (descEl) descEl.textContent = desc;

  if (sizeSel && sizesStr) {
    const sizes = sizesStr.split('|');
    sizeSel.innerHTML = sizes.map(s => `<option value="${s}">${s}</option>`).join('');
  }

  const panel = document.getElementById('catalog-detail-panel');
  if (panel) {
    panel.style.boxShadow = '0 0 0 3px var(--gold)';
    panel.style.transition = 'box-shadow 0.3s ease';
    setTimeout(() => { panel.style.boxShadow = 'var(--shadow-sm)'; }, 600);
  }

  TunaApp.showToast(`Mostrando ficha de «${name}»`);
}

function addToCart(title, price, img, size) {
  const currentImg = img || document.getElementById('cat-detail-img')?.getAttribute('src') || '../assets/img/prod_capa.jpg';
  const currentSize = size || document.getElementById('cat-detail-size')?.value || 'M';

  TunaCart.addItem({
    id: 'prod-' + title.substring(0, 5).toLowerCase().replace(/\s+/g, ''),
    name: title,
    price: price,
    img: currentImg,
    size: currentSize,
    qty: 1
  });
}

document.addEventListener('DOMContentLoaded', () => {
  filterCatalog();
});
