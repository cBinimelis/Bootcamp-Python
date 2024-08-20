$(document).ready(function () {
  $("#Logo").delay(800).fadeIn();
  $("html, body").animate(
    {
      scrollTop: $("#intro").offset().top,
    },
    2000
  );
});

$("#contactForm").on("submit", function (event) {
  event.preventDefault();
  let nombre = $("#nombre").val();
  let correo = $("#mail").val();
  let mensaje = $("#mensaje").val();

  if (nombre == "" || correo == "" || mensaje == "") {
    Swal.fire({
      title: "Paciencia",
      text: "Debes llenar todos los campos solicitados",
      icon: "warning",
    });
  } else {
    Swal.fire({
      title: "¡Gracias por tu mensaje!",
      text: "Pronto empezaremos a planear tu solución.",
      icon: "success",
    });
  }

  $("#nombre").val("");
  $("#mail").val("");
  $("#mensaje").val("");
});
