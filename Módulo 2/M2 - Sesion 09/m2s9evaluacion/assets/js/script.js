var tareas = [
  { tarea: "Pintar la fachada de la casa" },
  { tarea: "Comprar comida para el perro" },
  { tarea: "Pagar la tarjeta de crédito" },
];

const tabla = document.getElementById("cuerpo-tabla");
const tablaReset = tabla;
cargarTareas();

function tareasToggle() {
  let formulario = document.getElementById("formulario");
  if (formulario.style.display === "") {
    formulario.style.display = "block";
  } else {
    formulario.style.display = "";
  }
}

function cargarTareas() {
  for (i = 0; i < tareas.length; i++) {
    let nodeText = document.createTextNode(tareas[i].tarea);
    let rawText = tareas[i].tarea;
    agregarFila(nodeText, rawText);
  }
}

function agregarFila(textForCell, rawText) {
  let row = document.createElement("tr");
  let textCell = document.createElement("td");
  let buttonCell = document.createElement("td");
  let button = document.createElement("input");
  button.type = "submit";
  button.value = "Finalizar";
  button.classList.add("btn", "btn-danger");
  button.onclick = function () {
    eliminar(rawText);
  };
  textCell.appendChild(textForCell);
  row.appendChild(textCell);
  buttonCell.appendChild(button);
  row.appendChild(buttonCell);
  tabla.appendChild(row);
}

function agregarTarea() {
  let texto = document.getElementById("nuevaTarea");
  tareas.push({ tarea: texto.value });
  limpiarTabla();
  texto.value = "";
}

function limpiarTabla() {
  tabla.innerHTML = "";
  cargarTareas();
}

function eliminar(tarea) {
  let texto = tarea;
  for (let i = 0; i < tareas.length; i++) {
    if (texto == tareas[i].tarea) {
      tareas.splice(i, 1);
      break;
    }
  }
  limpiarTabla();
}
