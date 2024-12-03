# Modulo IV - Sesión V

## Agenda

- Herencias

## Herencia

La herencia múltiple es la capacidad de una subclase de heredar de múltiples súper clases.

Una de las principales ventajas es la reutilización de código permitiéndonos establecer una relación entre clases evitando que sea necesario volver a declarar ciertos métodos o atributos.

La Sobreescritura de métodos se refiere a la posibilidad de que una subclase cuente con métodos con el mismo nombre que los de una clase superior pero que definen comportamientos diferentes.

La función isinstance() comprueba si el objeto que es el primer argumento es una instancia o subclase de la clase classinfo que es el segundo argumento.

**LIBRERÍA**
Built-in

**SINTAXIS**
isinstance (objec, classinfo)

**PARÁMETROS**
object: Objeto a evaluar.
classinfo: Nombre de clase, tupla de nombres de clases o estructura recursiva de tuplas conteniendo nombres de clases.

Podemos comprobar si el número entero 4 pertenece a la clase int con el siguiente código: `isinstance(4,int) True`

Si pasamos como segundo argumento el nombre de la clase str (cadenas de texto), la función devuelve False: `isinstance(4, str) False`
