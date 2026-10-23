@startuml
title Diagrama de Flujo - Perfil Visitante

start
:Ingresar a la página principal (Inicio);

repeat
  :Visualizar menú principal de navegación;
  switch (Selección del visitante)
  case (La tuna)
    :Seleccionar subsección (Historia / Miembros / Galería);
    :Visualizar información pública de la tuna;
  case (Cancionero)
    :Seleccionar Repertorio o enlace a Spotify;
    :Escuchar o visualizar canciones;
  case (Vídeos)
    :Seleccionar Actuaciones o canal de Youtube;
    :Reproducir contenido multimedia;
  case (Captación)
    :Consultar sección Únete o Local de ensayo;
    :Ver información de reclutamiento;
  case (Tienda)
    :Explorar Catálogo de productos;
    :Consultar detalles de artículos;
  case (Contratación)
    if (¿El usuario ha iniciado sesión como cliente?) then (Sí)
      :Redirigir a Formulario de Contratación;
    else (No)
      :Mostrar aviso "Solo los clientes podrán contratar";
      :Ofrecer opción de Registro / Inicio de Sesión;
    endif
  endswitch

repeat while (¿Desea continuar navegando?) is (Sí)

:Salir del sitio web;
stop
@enduml