let opcion = 0;

do {
  opcion = parseInt(
    prompt(
      "Elija su clase de inicio:" +
        "\n1.- Guerrero" +
        "\n2.- Mago" +
        "\n3.- Paladín" +
        "\n4.- Curandero" +
        "\n5.- Abandonar Misión"
    )
  );
  switch (opcion) {
    case 1:
      alert("Has elegido al poderoso Guerrero");
      break;
    case 2:
      alert("Has elegido al sabio Mago");
      break;
    case 3:
      alert("Has elegido al ágil Paladín");
      break;
    case 4:
      alert("Has elegido al confiable Curandero");
      break;
    case 5:
      continue;
    default:
      alert("La selección no es válida");
      break;
  }
} while (opcion !== 5);

alert("Bueh, supondré que ganó el rey demonio ¯\\_(ツ)_/¯");
