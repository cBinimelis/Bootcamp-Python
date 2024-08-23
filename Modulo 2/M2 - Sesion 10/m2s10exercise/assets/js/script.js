$(document).ready(function () {
  // El código escrito acá se ejecutará luego de que se carguen los elementos de la página web
  let miTexto = $("#contenido").text();
  console.log(miTexto);

  let miAtributo = $("#nombre").attr("type");
  console.log(miAtributo);

  $("#caja1").mouseenter(function () {
    $("#caja2").show();
  });

  $("#caja1").mouseleave(function () {
    $("#caja2").hide();
  });

  $("#boton").click(function () {
    let nombre = $("#nombre").val();
    let correo = $("#correo").val();

    alert(`su nombre es ${nombre} y su correo es ${correo}`);
  });

  $("#boton1").click(function () {
    $("#contenido").css("background-color", "greenyellow");
  });

  $("#boton2").click(function () {
    $("#contenido").text("Texto escrito usando JQuery");
  });
});
