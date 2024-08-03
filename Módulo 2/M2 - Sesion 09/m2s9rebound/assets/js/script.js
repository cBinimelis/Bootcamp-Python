function mostrarCaja() {
  document.getElementById("text2").style.display = "block";
}

function ocultarCaja() {
  document.getElementById("text2").style.display = "none";
}

let initialW = document.getElementById("img").style.width;
function agrandarImagen() {
  document.getElementById("img").style.width = "100%";
}

function resetImagen() {
  document.getElementById("img").style.width = initialW;
}

function agrandarLetra() {
  document.getElementById("caja3").style.fontSize = "200%";
}
