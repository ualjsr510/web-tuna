/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Formularios Interactivos y Autenticación con Base de Datos (forms.js)
 */

const TunaForms = {
  // Cálculo interactivo de presupuestos de contratación
  calculateQuote() {
    const serviceType = document.getElementById('contract-service-type')?.value || 'boda';
    const durationHours = parseInt(document.getElementById('contract-duration')?.value || '1');
    const tunoCount = parseInt(document.getElementById('contract-tunos')?.value || '6');
    const displacement = document.getElementById('contract-displacement')?.checked ? 50 : 0;

    let baseRate = 180;
    if (serviceType === 'boda') baseRate = 220;
    if (serviceType === 'certamen') baseRate = 300;
    if (serviceType === 'academico') baseRate = 200;

    const hourlyExtra = (durationHours - 1) * 70;
    const tunoExtra = Math.max(0, tunoCount - 4) * 25;
    const total = baseRate + hourlyExtra + tunoExtra + displacement;

    const totalEl = document.getElementById('quote-total-price');
    const breakdownEl = document.getElementById('quote-breakdown');

    if (totalEl) totalEl.textContent = total.toFixed(2) + ' €';
    if (breakdownEl) {
      breakdownEl.innerHTML = `
        Tarifa base: ${baseRate} € · Horas adicionales: ${hourlyExtra} € · Músicos adicionales: ${tunoExtra} € ${displacement > 0 ? '· Desplazamiento provincia: 50 €' : ''}
      `;
    }
  },

  submitContractForm(event) {
    if (event) event.preventDefault();
    const service = document.getElementById('contract-service-type')?.value || 'Actuación';
    const date = document.getElementById('contract-date')?.value || new Date().toISOString().split('T')[0];
    const location = document.getElementById('contract-location')?.value || 'Almería Capital';
    const price = document.getElementById('quote-total-price')?.textContent || 'A convenir';
    const notes = document.getElementById('contract-notes')?.value || '';

    // Guardar en la base de datos
    const newContract = TunaDB.contracts.create({
      service: service,
      date: date,
      location: location,
      price: price,
      notes: notes
    });

    TunaApp.showToast(`¡Solicitud enviada con éxito! Referencia: ${newContract.id}`, 'success');
    
    // Si el usuario está registrado, llevar a sus contratos; si no, confirmación
    setTimeout(() => {
      if (TunaDB.auth.getCurrentUser()) {
        window.location.href = '../cliente/Contratos.html';
      } else {
        alert(`¡Gracias por tu solicitud! Hemos registrado tu petición con código ${newContract.id}. Nos pondremos en contacto contigo en breve.`);
        window.location.href = 'index.html';
      }
    }, 800);
  },

  submitJoinForm(event) {
    if (event) event.preventDefault();
    const name = document.getElementById('join-name')?.value || 'Aspirante';
    const instrument = document.getElementById('join-instrument')?.value || 'Guitarra';

    TunaApp.showToast(`¡Solicitud recibida, ${name}! Te esperamos en el próximo ensayo en el Edificio CAE.`, 'success');
    
    if (event.target && event.target.reset) event.target.reset();

    const successBox = document.getElementById('join-success-banner');
    if (successBox) successBox.style.display = 'block';
  },

  // Inicio de sesión real contra la base de datos
  submitLoginForm(event) {
    if (event) event.preventDefault();
    const emailInput = document.getElementById('login-email') || document.querySelector('input[type="email"]');
    const passInput = document.getElementById('login-password') || document.querySelector('input[type="password"]');

    if (!emailInput || !passInput) return;

    const email = emailInput.value;
    const password = passInput.value;

    const res = TunaDB.auth.login(email, password);

    if (res.success) {
      TunaApp.showToast(`¡Bienvenido de nuevo, ${res.user.nombre}!`, 'success');
      
      setTimeout(() => {
        if (res.user.rol === 'admin') {
          window.location.href = '../admin/index.html';
        } else {
          // Si venía de contratación o pedido, continuar el flujo
          const ref = document.referrer;
          if (ref.includes('Contratacion')) {
            window.location.href = '../visitante/FormularioContratacion.html';
          } else if (ref.includes('Cesta')) {
            window.location.href = '../visitante/DireccionEnvio.html';
          } else {
            window.location.href = '../cliente/index.html';
          }
        }
      }, 500);
    } else {
      alert(res.error);
    }
  },

  // Registro de nueva cuenta en la base de datos
  submitRegisterForm(event) {
    if (event) event.preventDefault();
    const email = document.getElementById('reg-email')?.value || document.querySelector('input[type="email"]')?.value;
    const password = document.getElementById('reg-pass')?.value || document.querySelector('input[type="password"]')?.value;
    const nombre = document.getElementById('reg-nombre')?.value || 'Nuevo';
    const apellidos = document.getElementById('reg-apellidos')?.value || 'Cliente';
    const telefono = document.getElementById('reg-tel')?.value || '600 000 000';

    if (!email || !password) {
      alert('Por favor, introduce tu correo y una contraseña.');
      return;
    }

    const res = TunaDB.users.create({
      email: email,
      password: password,
      nombre: nombre,
      apellidos: apellidos,
      telefono: telefono,
      rol: 'cliente'
    });

    if (res.success) {
      TunaApp.showToast(`¡Cuenta creada con éxito! Bienvenido, ${nombre}`, 'success');
      setTimeout(() => {
        window.location.href = '../cliente/index.html';
      }, 600);
    } else {
      alert(res.error);
    }
  },

  // Rellenar credenciales de demostración en el formulario de acceso
  fillDemoCredentials(role) {
    const emailInput = document.getElementById('login-email') || document.querySelector('input[type="email"]');
    const passInput = document.getElementById('login-password') || document.querySelector('input[type="password"]');

    if (emailInput && passInput) {
      if (role === 'admin') {
        emailInput.value = 'admin@derechoual.es';
        passInput.value = 'admin123';
      } else {
        emailInput.value = 'marta.gil@ual.es';
        passInput.value = 'cliente123';
      }
      TunaApp.showToast(`Credenciales de ${role} cargadas. Pulsa 'Iniciar sesión'.`);
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('contract-service-type')) {
    TunaForms.calculateQuote();
  }
});
