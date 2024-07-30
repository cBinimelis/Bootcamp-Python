let clientes;
let usuarioActual;
let salir = false;

crearClientes();
inicioSesion();

//FUNCIONES

function crearClientes() {
  clientes = [
    new Persona("CL001", "Carlos Lopez", "1234", 550000),
    new Persona("MS002", "María Soto", "4321", 789000),
    new Persona("DF003", "Diego Figueroa", "8520", 1360000),
  ];
}

function inicioSesion() {
  let identificador = prompt(
    "Bienvenido a la banca \nIngrese su identificador"
  );
  for (cliente of clientes) {
    if (cliente.id === identificador) {
      let password = prompt("Ingrese su contraseña");
      if (cliente.clave === password) {
        usuarioActual = cliente;
        menuPrincipal();
        break;
      } else {
        alert("Contraseña no válida");
        break;
      }
    } else {
      alert("Identificador no válido");
      break;
    }
  }
  alert("Gracias por su preferencia.");
}

function menuPrincipal() {
  alert("Bienvenido/a " + usuarioActual.nombre);
  do {
    let eleccion = parseInt(
      prompt(
        "Seleccione lo que desea hacer:" +
          "\n1.- Ver Saldo" +
          "\n2.- Realizar Giro" +
          "\n3.- Realizar Deposito" +
          "\n4.- Salir"
      )
    );

    switch (eleccion) {
      case 1:
        mostrarSaldo();
        break;
      case 2:
        realizarGiro();
        break;
      case 3:
        realizaDeposito();
        break;
      case 4:
        salir = true;
        break;
      default:
        alert("Opción inválida");
        break;
    }
  } while (!salir);
}

function mostrarSaldo() {
  alert("Su saldo actual es: " + usuarioActual.saldo);
}

function realizarGiro() {
  let giro = parseInt(
    prompt(
      "Su saldo actual es: " +
        usuarioActual.saldo +
        "\nIngrese el monto que desea girar"
    )
  );

  if (giro <= usuarioActual.saldo) {
    usuarioActual.saldo -= giro;
    alert("Giro realizado. Su nuevo saldo es: " + usuarioActual.saldo);
  } else {
    alert("No cuenta con el saldo necesario para la operación");
  }
}

function realizaDeposito() {
  let deposito = parseInt(
    prompt(
      "Su saldo actual es: " +
        usuarioActual.saldo +
        "\nIngrese el monto que desea depositar"
    )
  );
  if (deposito > 0) {
    usuarioActual.saldo += deposito;
    alert("Depósito realizado. Su nuevo saldo es: " + usuarioActual.saldo);
  } else {
    alert("Monto o selección inválida");
  }
}

function Persona(id, nombre, clave, saldo) {
  (this.id = id),
    (this.nombre = nombre),
    (this.clave = clave),
    (this.saldo = saldo);
}
