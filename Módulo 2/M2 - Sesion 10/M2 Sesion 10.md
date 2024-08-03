# Módulo II - Sesión VIII

## Agenda

### Sincrónica

- Objetos
- Manipulación del DOM

### Asincrónica

- ¿

## Objetos

Los objetos son la base del manejo de datos, la sintaxis de los mismos es:

```javascript
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
```

## Manipulación del DOM

Esto nos permite modificar cada uno de los distintos elementos de la página web, para ser más precisos la estructura y apariencia de los distintos elementos de nuestro HTML

---

## JQuery para manipular el DOM

Dentro de la programación con JavaScript, existen múltiples librerías y frameworks que se pueden utilizar, uno de ellos es la famosa librería JQuery.

Esta biblioteca simplifica enormemente la programación con JavaScript, considerándose de fácil aprendizaje y proporcionando un acceso simple a una serie de funciones y métodos de JavaScript ya prediseñados.

JQuery NO ES un lenguaje de programación, sino, una biblioteca de JavaScript

### ¿Qué es JQuery?

Según el sitio oficial de JQuery:

> "JQuery es una biblioteca de JavaScript rápida, pequeña y con muchas funciones. Hace que cosas como el recorrido y la manipulación del documento HTML, el manejo de eventos, la animación y Ajax sean mucho más simples con una API fácil de usar que funciona en una multitud de navegadores. Con una combinación de versatilidad y extensibilidad, JQuery ha cambiado la forma en que millones de personas escriben JavaScript”.

### La importancia de JQuery

JQuery es un software libre y de código abierto. Fue creada por [John Resig](https://johnresig.com/) y presentada el 14 de enero de 2006. Se cree que JQuery sigue siendo la biblioteca de JavaScript más utilizada, estando presente en un 77,2% de los sitios según informe de la [W3Techs](https://w3techs.com/). Por eso y por todas sus funcionalidades, es importante que aprendamos a usar esta poderosa herramienta.

### Sintaxis de JQuery

JQuery tiene una sintaxis un poco diferente a JavaScript puro, esta consta de un signo de dólar, que indica que se está trabajando con JQuery y, entre paréntesis, encontraremos indicado el selector al cual nos dirigimos. Esto puede ir seguido de una acción a realizar con este selector.

```js
$(selector).acccion();
```

### Características de JQuery

JQuery toma muchas tareas comunes que requieren muchas líneas de código JavaScript para llevarlas a cabo y las envuelve en métodos que puede llamar con una sola línea de código. La biblioteca JQuery contiene las siguientes características:

- Manipulación de HTML/DOM
- Manipulación de CSS
- Métodos de eventos HTML
- Efectos y Animaciones
- AJAX
- Utilidades
