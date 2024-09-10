# Módulo III - Sesión IX

## Agenda

- Funciones en Python

## Funciones

Una función es una porción de código que se puede utilizar una y otra vez.
**¿Para quésirve una función?**

- Las funciones permiten que el mismo trozo de codigo se ejecyute varias veces.
- Las funcinones dividen los programas largos en componentes mas pequeños.
- Las funciones pueden ser compartidas y utilizadas por otros programadores

### Definir Funciones

Una vez que conocemos la sintaxis de una función, desglosemos cada una de sus secciones para así tener claro cómo definir una función.

**La primera línea de código de una función contiene 3 partes.**

La palabra clave _def_ debe estar al principio de la línea que declara la función.
Cada función necesita un nombre. El _nombre_de_la_funcion_ debe comenzar con una letra (o guión bajo) y suele ser todo en minúsculas.

**Los nombres de las funciones van seguidos de un conjunto de paréntesis ( ).**

Después del nombre de la función, del paréntesis y de los argumentos vienen los dos puntos ( : ). En Python, se requieren dos puntos al final de la primera línea de todas las funciones.

**El cuerpo de la función contiene el código que se ejecutará cuando se llame a la función.**

La palabra clave return suele ser la última línea de una función. return indica que cualquier expresión que siga es la respuesta de la función.
La respuesta es cualquier expresión que se incluya después de return.

### Recepción de parámetros en una función

Las funciones pueden ser escritas para aceptar múltiples argumentos de entrada. Para suministrar un valor prestablecido al declarar la función debemos escribir el nombre del parámetro, el signo igual y luego el valor.

Solo escribiremos la primera línea de la función, con un valor preestablecido para el parámetro mensaje.

### Retorno de una función

Lo primero que debemos tomar en cuenta es que una vez el intérprete encuentre el comando return, la ejecución de la función se detendrá una vez devuelto el resultado.

### Variables locales y variables globales

- Las variables globales se declaran en el cuerpo principal del código, se llaman variables globales porque pueden ser utilizadas en cualquier momento y lugar del código.
- Por su parte las variables locales son aquellas que declaramos dentro de una función.

### Invocación de una función

Para hacer uso de una función dentro de código, lo único que debemos hacer es escribir su nombre seguido de paréntesis y la lista de argumentos separados por comas dentro de los paréntesis.
