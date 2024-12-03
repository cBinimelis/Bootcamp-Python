$("#leer-posts").click(function () {
  //Ajax
  $.get("https://jsonplaceholder.typicode.com/posts", function (data) {
    data.forEach((post) => {
      $("#ul-posts").append(`<li class="list-group-item">${post.title}</li>`);
    });
  });
});

$("#crear-post").click(function () {
  $.post(
    "https://jsonplaceholder.typicode.com/posts",
    {
      title: $("#title").val(),
      body: $("#body").val(),
      userId: 1,
    },
    function (data) {
      Swal.fire({
        title: "¡Felicidades!",
        text: "post creado existosamente",
        icon: "success",
        confirmButtonText: "Cool",
      });
      $("#title").val("");
      $("#body").val("");
    }
  ).fail(function (error) {
    console.log(error);
  });
});
