console.log("Hola JS... Por enésima vez");

var numero1, numero2, resultado;
numero1 = prompt("Ingrese el primer número");
numero2 = prompt("Ingrese el segundo número");
numero1 = parseInt(numero1);
numero2 = parseInt(numero2);
//LLAMADA A LA FUNCION
resultado = resta(numero1, numero2);
alert("La resta de " + numero1 + " - " + numero2 + " es " + resultado);
//INICIO FUNCIONES
function suma(numero1, numero2) {
  resultado = numero1 + numero2;
  return resultado;
}
function resta(numero1, numero2) {
  resultado = numero1 - numero2;
  return resultado;
}
function multiplicacion(numero1, numero2) {
  resultado = numero1 * numero2;
  return resultado;
}
function division(numero1, numero2) {
  resultado = numero1 / numero2;
  return resultado;
}
