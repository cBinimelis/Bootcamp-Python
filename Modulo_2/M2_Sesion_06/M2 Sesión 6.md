# Módulo II - Sesión VI

## Agenda

- Contenedores
- Grillas
- Form
- Botones
- Columnas

Aunque hablar de todos los elementos que nos ofrece un framework de la característica de Bootstrap tomaría mucho tiempo, existen más elementos básicos que podemos conocer inicialmente.

### Contenedores

Los contenedores son el elemento de diseño más básico en Bootstrap y son necesarios cuando se usa el sistema de cuadrícula predeterminado (como nombrábamos previamente).

Se utilizan para contener, rellenar y (en ocasiones) centrar el contenido dentro de ellos, es decir, todos los elementos que se encuentran contenidos dentro de ellos.

Bootstrap cuenta con 3 tipos distintos de contenedores:

- .container:
  Este tipo de contenedor establece un tamaño maximo de ancho en cada punto de interrupción (definido preciamente por Bootstrap, no tenemos la necesidad de determinar los puntos de interrupción).

- container-fluid:
  Este tipo de contenedor establece un tamaño de ancho del 100% en cada uno de los puntos de quiebre.

- container-[punto de quiebre]:
  Este tipo de contenedor mantiene un tamaño máximo del 100% de ancho hasta el punto especificado, teniendo, posterior a eso, un tamaño especifico por cada punto de quiebre definido.

### Grillas

Un componente importante para la responsividad son las grillas, un sistema de cuadrícula utilizado para crear diseños de todas las formas y tamaños. Esto ocurre gracias al sistema de doce columnas con el cual indicamos cuantas de ellas utilizará un elemento en un determinado tamaño de pantalla. Además, este sistema de grillas trabaja con contenedores.

### Form

Bootstrap nos entrega diseños de formularios adaptativos y atractivos. Este framework no nos entrega validaciones para nuestros formularios, ya que la lógica que utilicemos para eso será el valor agregado que aportemos nosotros como programadores utilizando expresiones regulares, algún lenguaje de programación, etc.

### Botones

Los botones son un elemento relevante en un diseño web y puede ser usado en muchas otras cosas, no solo en un formulario, por lo tanto, su estética también es relevante. Bootstrap nos ofrece botones con colores que dan una señal al usuario y los cuales también facilitaran nuestro trabajo de diseño.

### Columnas

Toda esta tecnología ya desarrollada por Bootstrap y que podemos utilizar a nuestro favor, incluye un diseño automático de las columnas de la cuadricula de flexbox, lo que significa que puede establecer el ancho de una columna y hacer que las columnas hermanas se redimensionen automáticamente a su alrededor.
