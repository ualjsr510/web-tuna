@startuml
title Diagrama de Flujo - Perfil Administrador

start
:Iniciar Sesión como Administrador;
:Acceder al Panel de Control / Dashboard;

repeat
  :Seleccionar módulo de administración;
  switch (Módulo seleccionado)
  case (Contratos)
    :Visualizar lista de Formularios/Solicitudes;
    :Revisar detalles del evento solicitado;
    if (¿Aprobar solicitud?) then (Sí)
      :Cambiar estado a Aprobado / Confirmado;
    else (No)
      :Rechazar solicitud o solicitar ajustes;
    endif
  case (Tienda)
    :Acceder a gestión de Productos y Precios;
    split
      :Añadir nuevo producto;
    split again
      :Editar precio / descripción existente;
    split again
      :Eliminar producto del catálogo;
    end split
    :Guardar cambios en catálogo;
  case (Miembros)
    :Acceder a la lista de Miembros;
    :Actualizar Descripción, Fotos, Apodos o Instrumentos;
    :Guardar ficha del miembro;
  case (Repertorio y audiovisuales)
    :Acceder a Gestión Multimedia;
    :Agregar / Modificar / Eliminar Canciones, Vídeos o Fotos;
    :Publicar actualización en la web;
  endswitch

repeat while (¿Desea gestionar otro módulo?) is (Sí)

:Cerrar Sesión de Administrador;
stop
@enduml