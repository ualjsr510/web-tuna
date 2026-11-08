with open("prototipo/css/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

stepper_css = """
/* ==========================================================================
   CHECKOUT STEPPER & FUNNEL (FLUJO DE COMPRA A LA DERECHA)
   ========================================================================== */
.checkout-layout {
  display: flex;
  gap: 28px;
  align-items: flex-start;
  width: 100%;
}

.checkout-main-col {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.checkout-sidebar-col {
  width: 350px;
  flex: none;
  display: flex;
  flex-direction: column;
  gap: 18px;
  position: sticky;
  top: 90px;
}

.checkout-stepper-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-top: 4px solid var(--gold);
  border-radius: 8px;
  padding: 22px 20px;
  box-shadow: var(--shadow-sm);
}

.stepper-header {
  font-family: var(--serif);
  font-size: 15px;
  color: var(--ink);
  margin: 0 0 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--line);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stepper-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.stepper-item {
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
}

.stepper-item:not(:last-child)::after {
  content: "";
  position: absolute;
  left: 14px;
  top: 30px;
  bottom: -14px;
  width: 2px;
  background: var(--line);
}

.stepper-item.completed:not(:last-child)::after {
  background: var(--gold);
}

.stepper-bubble {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 12px;
  z-index: 2;
  flex: none;
  transition: all 0.2s ease;
}

.stepper-item.pending .stepper-bubble {
  background: var(--soft);
  color: var(--muted);
  border: 1px solid var(--line);
}

.stepper-item.active .stepper-bubble {
  background: var(--accent);
  color: #fff;
  border: 2px solid var(--gold);
  box-shadow: 0 0 0 3px rgba(197, 155, 63, 0.25);
}

.stepper-item.completed .stepper-bubble {
  background: var(--gold);
  color: #1a1012;
  border: 1px solid var(--gold-dark);
}

.stepper-label {
  display: flex;
  flex-direction: column;
}

.stepper-title {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.2;
}

.stepper-item.active .stepper-title {
  color: var(--accent);
  font-weight: 800;
}

.stepper-item.completed .stepper-title {
  color: var(--gold-dark);
}

.stepper-sub {
  font-size: 11px;
  color: var(--muted);
}

.checkout-summary-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 20px;
  box-shadow: var(--shadow-sm);
}

@media (max-width: 960px) {
  .checkout-layout {
    flex-direction: column-reverse;
  }
  .checkout-sidebar-col {
    width: 100%;
    position: static;
  }
}
"""

if "CHECKOUT STEPPER" not in css:
    css += "\n" + stepper_css
    with open("prototipo/css/styles.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Added Stepper CSS styles to prototipo/css/styles.css")
else:
    print("Stepper CSS already present")

