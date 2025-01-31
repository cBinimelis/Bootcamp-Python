let seleccion = parseInt(
  prompt(
    "¡Hola! Soy Eva, tu asistente de Servicio al Cliente de Mentel." +
      "\nEstoy aquí para ayudarte en lo que necesites." +
      "\nEscribe el número de la opción que buscas:" +
      "\n1.-Boletas y Pagos" +
      "\n2.- Señal y Llamadas" +
      "\n3.- Oferta Comercial" +
      "\n4.- Otras Consultas"
  )
);

switch (seleccion) {
  case 1:
    boletasPagos();
    break;
  case 2:
    senalLlamadas();
    break;
  case 3:
    ofertaComercial();
    break;
  case 4:
    otrasConsultas();
    break;
  default:
    defaultOption();
    break;
}

function boletasPagos() {
  let opcion = parseInt(
    prompt("Seleccione una opción:" + "1.- Ver Boleta\n2.- Pagar Cuenta")
  );
  switch (opcion) {
    case 1:
      alert("Haga clic aquí para descargar su boleta.");
      break;
    case 2:
      alert("Usted está siendo transferido. Espere por favor...");
      break;
    default:
      defaultOption();
      break;
  }
}
function senalLlamadas() {
  let opcion = parseInt(
    prompt(
      "Seleccione una opción:" +
        "1.- Problemas con la señal\n2.- Problemas con las llamadas"
    )
  );
  switch (opcion) {
    case 1:
      ingresarSolicitud();
      break;
    case 2:
      ingresarSolicitud();
      break;
    default:
      defaultOption();
      break;
  }
}
function ofertaComercial() {
  let opcion = prompt(
    "¡Mentel tiene una oferta comercial acorde a tus necesidades!" +
      "\nPara conocer más informacipon y ser asesorado personalmente por un ejecutivo " +
      "escribe 'SI' y un ejecutivo te llamará. De lo contrario ingrese 'NO'"
  );
  switch (opcion) {
    case "SI":
      alert("Un ejecutivo contactará con usted.");
      break;
    case "NO":
      alert("Gracias por preferir nuestros servicios.");
      break;
    default:
      defaultOption();
      break;
  }
}
function otrasConsultas() {
  ingresarSolicitud();
}

function ingresarSolicitud() {
  let solicitud = prompt("A continuación escriba su consulta:");
  alert(
    "Estimado usuario. su consulta: '" +
      solicitud +
      "' ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos."
  );
}

function defaultOption() {
  alert(
    "La opción ingresada no es válida. Gracias por preferir nuestros servicios"
  );
}
