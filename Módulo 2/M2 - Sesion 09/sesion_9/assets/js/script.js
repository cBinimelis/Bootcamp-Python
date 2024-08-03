function saludo() {
  console.log("Hola Mundo (otra veh)");
}

saludo();
saludoPersona("Miguel", "Soto");

function saludoPersona(nombre, apellido) {
  console.log(
    `Hola ${nombre} ${apellido}, el plato para hoy es: ${menuDiario()}`
  );
}

function menuDiario() {
  return "Papas mayo";
}

let alumnos = Array();
console.log(alumnos);
let profesores = [];
console.log(profesores);

let alumnos2 = Array("Patricio", "Hector");
let profesores2 = ["Gabriel"];
console.log(alumnos2, profesores2);

let edades = [4, 1, 19, 12, 85, 33, 18, 15, 20, 29];
let menoresDeEdad = edades.filter((elemento) => elemento < 18);
console.log(menoresDeEdad);

let valorRecorrido = edades.length;
for (let index = 0; index < edades.length; index++) {
  console.log(edades[index]);
}

let contador = 0;
while (contador < 5) {
  console.log(`Bucle #${contador + 1}`);
  contador++;
}

let isExit = false;
let cnt = 0;
while (isExit === false) {
  console.log(`Bucle v2 #${cnt + 1}`);
  cnt++;
  if (cnt === 10) {
    isExit = true;
  }
}

let num = 0;

do {
  num = lanzarDado();
  console.log();
} while (num % 2 === 0);

function lanzarDado() {
  return 3;
}

let selectorId = document.getElementById("parrafo");
console.log(selectorId);

let creandoElemento = document.createElement("p");
creandoElemento.textContent = "Este nodo fue creado desde JavaScript";
document.body.appendChild(creandoElemento);

var selectorVarios = document.querySelector(".contenedor");
creandoElemento.textContent = "Este nodo MULTIPLE fue creado desde JavaScript";
selectorVarios.append(creandoElemento);

function miFuncion() {
  var captura = document.querySelector("#nieve");
  var valor = captura.value;
  document.getElementById("resultado").innerText = `Usted ha
 seleccionado ${valor}`;
}
