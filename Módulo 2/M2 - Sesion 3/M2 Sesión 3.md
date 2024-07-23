# Módulo II - Sesión III

## Agenda

- CSS

## CSS - Cascade Style Sheets

Es un lenguaje de programación basado en reglas semánticas en las cuales se utilizan selectores para aplicar dichas reglas en los elementos por medio de selectores.

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
