@startuml
title Diagrama de Flujo - Perfil Cliente

start
:Iniciar Sesión como Cliente;
:Acceder al Panel de Inicio;

repeat
  :Seleccionar acción del menú de cliente;
  switch (Opción seleccionada)
  case (Contratación)
    :Abrir Formulario de Contratación;
    :Ingresar datos del evento (Fecha, Lugar, Tipo);
    :Enviar solicitud;
    :Recibir confirmación de recepción;
  case (Datos)
    :Visualizar información personal;
    if (¿Desea modificar datos?) then (Sí)
      :Editar Nombre, Teléfono o Correo;
      :Guardar cambios;
      :Confirmar actualización de perfil;
    else (No)
    endif
  case (Pedidos)
    :Consultar Historial de Pedidos;
    :Ver estado de solicitudes y contrataciones pasadas;
  case (Gestionar cuenta)
    :Ingresar contraseña actual;
    :Ingresar y confirmar nueva contraseña;
    :Validar requerimientos de seguridad;
    :Actualizar contraseña de acceso;
  endswitch

repeat while (¿Desea realizar otra gestión?) is (Sí)

:Cerrar Sesión;
stop
@enduml