var tareas = [
  { tarea: "Pintar la fachada de la casa" },
  { tarea: "Comprar comida para el perro" },
  { tarea: "Pagar la tarjeta de crédito" },
];

let boton = document.createElement("button");

cargarTareas();

let tabla = document.getElementById("cuerpo-tabla").innerHTML;
console.log(tabla);

document.body.appendChild(boton);
function cargarTareas() {
  for (i = 0; i < tareas.length; i++) {
    console.log(tareas[i].tarea);
  }
}

function completar() {
  alert("!!!!");
}
