# Módulo II - Sesión III

## Agenda

- CSS

## CSS - Cascade Style Sheets

CSS u Hojas de Estilo en Cascada (en inglés Cascading Style Sheets) es un lenguaje de estilizado, es decir, un lenguaje que nos permite dar estilos a documentos HTML y otros lenguajes que no hemos estudiado durante este curso.
Se componede 3 elementos basicos:

- Selector
- Propiedad
- Valor

```
p {
    color: red;
}
```

> Declaracion de una regla de CSS

### Selectores

Son los encargados de seleccionar todos los elementos que sean del mismo tipo, estas pueden ser etiquetas, clases o identificadores.

- Selector de Etiqueta

  ```
  label {
      color: green;
  }
  ```

- Selector de clase

  ```
  .text-green {
      color: green;
  }

  <p class="text-green">Hello</p>
  ```

- Selector de Id

  ```
  #status {
      color: green;
  }

  <h2 id="status">Status</h2>
  ```

- Selector por Atributos

  ```
  a[target="_blank"] {
      color: indigo;
  }

  <a target="blank" >Go to</a>
  ```

- Selector por Comportamiento

  ```
  a:hover {
      color: turquoise;
  }

  <a>Go to</a>
  ```

- Selector por Descendencia

  ```
  div p a{
      color: yellow;
  }
    <div>
        <p>
            <a>Go to</a>
        </p>
    </div>
  ```

Existen también selectores especiales como por ejemplo el selector general `*`, cuya funcion es aplicar la regla inserta a todos los elementos del documento.

## Introducción a CSS

### ¿Qué es CSS?

CSS u _Hojas de Estilo en Cascada_ (del inglés _Cascade Style Sheets_) es un lenguaje que nos permite darle estilo a los documentos **HTML** y otros lenguajes que no hemos estudiado en este curso. Como analogía de CSS, en conjunto con HTML, podríamos decir que HTML es el "esqueleto" de nuestra página, mientras que CSS es la "apariencia" de la misma.

### Navegadores y CSS

De todos los componentes de los navegadores, se denomina “motor” la parte que se encarga de interpretar el código HTML y CSS. Los navegadores Firefox, Chrome, Safari y Opera son los más avanzados en el soporte de CSS, ya que incluyen muchos elementos de la versión CSS 3, siendo Chrome quien entrega el mejor soporte para todas las características multimedia de CSS 3.
