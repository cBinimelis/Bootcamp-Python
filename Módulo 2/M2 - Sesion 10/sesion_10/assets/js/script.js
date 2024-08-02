let person = {
  rut: "18112233-Z",
  firstName: "Cristofer",
  LastName: "Binimelis",
  birthDate: "21-03-94",
  sleep: function () {
    console.log("Estoy durmiendo");
  },
  wakeUp: function () {
    console.log("Estoy despierto");
  },
};

/* Declarar un objeto llamado avion con: 
modelo, capacidad de pasajeros, matricula. 
Adicionalmente un método que se llame "volar" */

let avion = {
  matricula: "PY-BCP",
  modelo: "Boeing 747-8",
  capacidadPasajeros: "700",
  volar: function (destino) {
    console.log(`Estoy volando hacia ${destino} wiii!!!`);
  },
};

console.log(avion.volar("Nápoles"));
console.log(avion);

let labelName = document.getElementById("labelName");
labelName.innerHTML = "Hola Constanza!";

let btnAgregar = document.getElementById("btnAgregar");
btnAgregar.addEventListener("click", () => {
  let body = document.getElementById("bodyPrincipal");
  let ul = document.createElement("ul");
  ul.classList.add("list-group");

  let li = document.createElement("li");
  li.classList.add("list-group-item");

  let lib = document.createElement("li");
  lib.classList.add("list-group-item");
});
