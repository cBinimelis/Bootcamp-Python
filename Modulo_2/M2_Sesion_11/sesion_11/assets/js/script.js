$(document).ready(function () {
  let account = 0;

  console.log("Desde JQuery");
  $("#change-class").click(function () {
    $("p").addClass("resaltar");
  });

  $("#remove-class").click(function () {
    $("p").removeClass("resaltar");
  });

  $("#toggle-class").click(function () {
    $("p").toggleClass("resaltar");
  });

  $("#create-list").click(function () {
    const items = ["Carlos", "Patricio", "Natalia", "Angela"];
    let listItems = '<ul class="list-group">';
    items.forEach(function (item) {
      listItems += `<li class="list-group-item">${item}</li>`;
    });
    listItems += "</ul>";
    $("#list-container").html(listItems);
  });

  $("#create-list-2").click(function () {
    account++;
    let nuevoElemento = $(
      `<li class="list-group-item">Elemento ${account}</li>`
    );
    let count = account;
    nuevoElemento.click(function () {
      console.log("!!!!!!!!!! " + count);
    });
    $("#ul-container").append(nuevoElemento);
  });
});
