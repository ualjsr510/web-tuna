/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Capa de Base de Datos y Persistencia Relacional (db.js)
 * Sincronizada con el esquema SQL de la base de datos oficial
 */

const TunaDB = {
  // Inicialización de la base de datos local
  init() {
    if (!localStorage.getItem('tuna_db_initialized')) {
      this.seedDefaultData();
      localStorage.setItem('tuna_db_initialized', 'true');
    }
  },

  seedDefaultData() {
    // 1. Usuarios del sistema
    const users = [
      {
        id: 1,
        email: 'marta.gil@ual.es',
        password: 'cliente123',
        rol: 'cliente',
        nombre: 'Marta',
        apellidos: 'Gil Navarro',
        telefono: '600 123 456',
        direccion: 'Calle de la Reina, 14, 2ºA',
        ciudad: 'Almería',
        cp: '04001',
        fechaRegistro: '2026-01-15'
      },
      {
        id: 2,
        email: 'admin@derechoual.es',
        password: 'admin123',
        rol: 'admin',
        nombre: 'Maese',
        apellidos: 'Tuno Mayor',
        telefono: '685 99 55 10',
        direccion: 'Edificio CAE, Campus UAL',
        ciudad: 'Almería',
        cp: '04120',
        fechaRegistro: '2024-09-01'
      },
      {
        id: 3,
        email: 'carlos.ruiz@ual.es',
        password: 'cliente123',
        rol: 'cliente',
        nombre: 'Carlos',
        apellidos: 'Ruiz Sánchez',
        telefono: '600 234 567',
        direccion: 'Avenida de la Estación, 8',
        ciudad: 'Almería',
        cp: '04005',
        fechaRegistro: '2026-02-03'
      },
      {
        id: 4,
        email: 'lucia.fernandez@ual.es',
        password: 'cliente123',
        rol: 'cliente',
        nombre: 'Lucía',
        apellidos: 'Fernández Mora',
        telefono: '600 345 678',
        direccion: 'Calle Murcia, 21',
        ciudad: 'Almería',
        cp: '04004',
        fechaRegistro: '2026-03-20'
      }
    ];
    localStorage.setItem('tuna_db_users', JSON.stringify(users));

    // 2. Contratos iniciales
    const contracts = [
      {
        id: 'CTR-2026-01',
        userId: 1,
        clientName: 'Marta Gil Navarro',
        email: 'marta.gil@ual.es',
        phone: '600 123 456',
        service: 'Boda y Serenata',
        date: '2026-05-18',
        time: '21:00',
        location: 'Hotel Catedral Almería',
        guests: 120,
        hours: 2,
        musicians: 8,
        price: 'A convenir',
        status: 'Realizado',
        notes: 'Recepción en cóctel y serenata bajo balcón.'
      },
      {
        id: 'CTR-2026-02',
        userId: 1,
        clientName: 'Marta Gil Navarro',
        email: 'marta.gil@ual.es',
        phone: '600 123 456',
        service: 'Serenata Aniversario',
        date: '2027-03-20',
        time: '22:30',
        location: 'Casco Histórico Almería',
        guests: 30,
        hours: 1,
        musicians: 6,
        price: 'A convenir',
        status: 'Pendiente',
        notes: 'Ronda sorpresa.'
      },
      {
        id: 'CTR-2026-03',
        userId: 3,
        clientName: 'Carlos Ruiz Sánchez',
        email: 'carlos.ruiz@ual.es',
        phone: '600 234 567',
        service: 'Cumpleaños',
        date: '2027-01-16',
        time: '20:00',
        location: 'Finca Los Olivos, Viator',
        guests: 60,
        hours: 1,
        musicians: 6,
        price: 'A convenir',
        status: 'Confirmado',
        notes: 'Entrada por sorpresa durante la cena.'
      },
      {
        id: 'CTR-2026-04',
        userId: 4,
        clientName: 'Lucía Fernández Mora',
        email: 'lucia.fernandez@ual.es',
        phone: '600 345 678',
        service: 'Evento de empresa',
        date: '2027-02-12',
        time: '19:00',
        location: 'Auditorio Maestro Padilla, Almería',
        guests: 150,
        hours: 2,
        musicians: 10,
        price: 'A convenir',
        status: 'Pendiente',
        notes: ''
      }
    ];
    localStorage.setItem('tuna_db_contracts', JSON.stringify(contracts));

    // 3. Pedidos iniciales
    const orders = [
      {
        id: 'PED-2026-081',
        userId: 1,
        date: '2026-04-10',
        subtotal: 37.00,
        shipping: 4.50,
        total: 41.50,
        status: 'En preparación',
        address: 'Calle de la Reina, 14, 2ºA, 04001 Almería',
        items: [
          { name: 'Capa tradicional de paño', price: 25.00, qty: 1, size: 'M' },
          { name: 'CD XXV Aniversario', price: 12.00, qty: 1, size: 'Estándar' }
        ]
      },
      {
        id: 'PED-2026-074',
        userId: 3,
        date: '2026-10-22',
        subtotal: 28.00,
        shipping: 4.50,
        total: 32.50,
        status: 'Enviado',
        address: 'Avenida de la Estación, 8, 04005 Almería',
        items: [
          { name: "Sudadera 'Derecho Almería'", price: 28.00, qty: 1, size: 'L' }
        ]
      },
      {
        id: 'PED-2026-052',
        userId: 4,
        date: '2026-09-02',
        subtotal: 25.00,
        shipping: 0,
        total: 25.00,
        status: 'Entregado',
        address: 'Calle Murcia, 21, 04004 Almería',
        items: [
          { name: 'Capa tradicional de paño', price: 25.00, qty: 1, size: 'S' }
        ]
      }
    ];
    localStorage.setItem('tuna_db_orders', JSON.stringify(orders));
  },

  // -------------------------------------------------------------
  // MÓDULO DE AUTENTICACIÓN Y SESIÓN
  // -------------------------------------------------------------
  auth: {
    getCurrentUser() {
      const raw = localStorage.getItem('tuna_db_session');
      if (raw) {
        try { return JSON.parse(raw); } catch (e) {}
      }
      return null;
    },

    login(email, password) {
      TunaDB.init();
      const users = JSON.parse(localStorage.getItem('tuna_db_users') || '[]');
      const user = users.find(u => u.email.toLowerCase() === email.toLowerCase().trim() && u.password === password);
      
      if (user) {
        const sessionData = {
          id: user.id,
          email: user.email,
          nombre: user.nombre,
          apellidos: user.apellidos,
          rol: user.rol,
          telefono: user.telefono,
          direccion: user.direccion,
          ciudad: user.ciudad,
          cp: user.cp
        };
        localStorage.setItem('tuna_db_session', JSON.stringify(sessionData));
        return { success: true, user: sessionData };
      }
      return { success: false, error: 'Credenciales incorrectas. Verifica el correo y la contraseña.' };
    },

    logout() {
      localStorage.removeItem('tuna_db_session');
      TunaApp.showToast('Sesión cerrada con éxito');
      setTimeout(() => {
        // Redirigir siempre a la portada pública
        const inSubfolder = /\/(visitante|cliente|admin)\//i.test(window.location.pathname);
        window.location.href = (inSubfolder ? '../' : '') + 'visitante/index.html';
      }, 400);
    },

    // Control de acceso a páginas protegidas
    checkRouteGuard(requiredRole) {
      const current = this.getCurrentUser();
      
      if (!current) {
        // No hay sesión iniciada: expulsar a la pantalla de acceso
        alert('Acceso restringido: Debes iniciar sesión con tu cuenta para acceder.');
        window.location.href = '../visitante/Acceso.html';
        return false;
      }

      if (requiredRole === 'admin' && current.rol !== 'admin') {
        alert('Acceso denegado: Esta zona requiere privilegios de Administrador.');
        window.location.href = '../visitante/index.html';
        return false;
      }

      return true;
    }
  },

  // -------------------------------------------------------------
  // MÓDULO DE USUARIOS
  // -------------------------------------------------------------
  users: {
    getAll() {
      TunaDB.init();
      return JSON.parse(localStorage.getItem('tuna_db_users') || '[]');
    },

    getById(id) {
      return this.getAll().find(u => u.id === id);
    },

    create(userData) {
      TunaDB.init();
      const users = this.getAll();
      if (users.some(u => u.email.toLowerCase() === userData.email.toLowerCase().trim())) {
        return { success: false, error: 'Ya existe una cuenta registrada con este correo electrónico.' };
      }

      const newUser = {
        id: Date.now(),
        email: userData.email.trim(),
        password: userData.password,
        rol: userData.rol || 'cliente',
        nombre: userData.nombre.trim(),
        apellidos: userData.apellidos ? userData.apellidos.trim() : '',
        telefono: userData.telefono ? userData.telefono.trim() : '',
        direccion: userData.direccion || '',
        ciudad: userData.ciudad || 'Almería',
        cp: userData.cp || '04001',
        fechaRegistro: new Date().toISOString().split('T')[0]
      };

      users.push(newUser);
      localStorage.setItem('tuna_db_users', JSON.stringify(users));
      
      // Iniciar sesión automáticamente con la nueva cuenta
      localStorage.setItem('tuna_db_session', JSON.stringify(newUser));
      return { success: true, user: newUser };
    },

    update(id, updates) {
      const users = this.getAll();
      const idx = users.findIndex(u => u.id === id);
      if (idx !== -1) {
        users[idx] = { ...users[idx], ...updates };
        localStorage.setItem('tuna_db_users', JSON.stringify(users));
        
        // Si es el usuario activo, actualizar sesión
        const current = TunaDB.auth.getCurrentUser();
        if (current && current.id === id) {
          localStorage.setItem('tuna_db_session', JSON.stringify(users[idx]));
        }
        return true;
      }
      return false;
    }
  },

  // -------------------------------------------------------------
  // MÓDULO DE CONTRATOS
  // -------------------------------------------------------------
  contracts: {
    getAll() {
      TunaDB.init();
      return JSON.parse(localStorage.getItem('tuna_db_contracts') || '[]');
    },

    getByUser(userId) {
      return this.getAll().filter(c => c.userId === userId);
    },

    getById(id) {
      return this.getAll().find(c => c.id === id) || null;
    },

    create(data) {
      TunaDB.init();
      const list = this.getAll();
      const currentUser = TunaDB.auth.getCurrentUser() || { id: null, nombre: 'Cliente web', apellidos: '' };
      
      const newContract = {
        id: 'CTR-2026-' + Math.floor(10 + Math.random() * 90),
        userId: currentUser.id,
        clientName: `${currentUser.nombre} ${currentUser.apellidos || ''}`.trim(),
        email: currentUser.email || 'cliente@ual.es',
        phone: currentUser.telefono || '600 000 000',
        service: data.service,
        date: data.date,
        time: data.time || '20:00',
        location: data.location,
        guests: data.guests || 50,
        hours: data.hours || 1,
        musicians: data.musicians || 6,
        price: data.price || 'A convenir',
        status: 'Pendiente',
        notes: data.notes || '',
        created: new Date().toLocaleDateString('es-ES')
      };

      list.unshift(newContract);
      localStorage.setItem('tuna_db_contracts', JSON.stringify(list));
      return newContract;
    },

    updateStatus(id, newStatus) {
      const list = this.getAll();
      const item = list.find(c => c.id === id);
      if (item) {
        item.status = newStatus;
        localStorage.setItem('tuna_db_contracts', JSON.stringify(list));
        return true;
      }
      return false;
    }
  },

  // -------------------------------------------------------------
  // MÓDULO DE PEDIDOS
  // -------------------------------------------------------------
  orders: {
    getAll() {
      TunaDB.init();
      return JSON.parse(localStorage.getItem('tuna_db_orders') || '[]');
    },

    getByUser(userId) {
      return this.getAll().filter(o => o.userId === userId);
    },

    getById(id) {
      return this.getAll().find(o => o.id === id) || null;
    },

    update(id, updates) {
      const list = this.getAll();
      const order = list.find(o => o.id === id);
      if (!order) return false;
      Object.assign(order, updates);
      localStorage.setItem('tuna_db_orders', JSON.stringify(list));
      return true;
    },

    create(orderData) {
      TunaDB.init();
      const list = this.getAll();
      const currentUser = TunaDB.auth.getCurrentUser() || { id: null };

      const newOrder = {
        id: 'PED-2026-' + Math.floor(100 + Math.random() * 900),
        userId: currentUser.id,
        date: new Date().toISOString().split('T')[0],
        subtotal: orderData.subtotal,
        shipping: orderData.shipping,
        total: orderData.total,
        status: 'En preparación',
        address: orderData.address,
        items: orderData.items || []
      };

      list.unshift(newOrder);
      localStorage.setItem('tuna_db_orders', JSON.stringify(list));
      return newOrder;
    },

    updateStatus(id, newStatus) {
      const list = this.getAll();
      const order = list.find(o => o.id === id);
      if (order) {
        order.status = newStatus;
        localStorage.setItem('tuna_db_orders', JSON.stringify(list));
        return true;
      }
      return false;
    }
  }
};

// Inicializar base de datos de inmediato
TunaDB.init();

