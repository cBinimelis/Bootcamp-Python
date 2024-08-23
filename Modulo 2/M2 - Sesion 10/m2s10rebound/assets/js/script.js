function mostrarCaja() {
  $("#text2").show();
}

function ocultarCaja() {
  $("#text2").hide();
}

let initialW = document.getElementById("img").style.width;
function agrandarImagen() {
  $("#img").css("width", "100%");
}

function resetImagen() {
  $("#img").css("width", initialW);
}

function agrandarLetra() {
  $("#caja3").css("fontSize", "200%");
}
