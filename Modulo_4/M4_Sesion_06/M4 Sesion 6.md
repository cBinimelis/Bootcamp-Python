# Modulo IV - Sesión VI

## Agenda

- Manejo de errores y excepciones

## Manejo de errores y excepciones

**¿Qué es una excepción?**
Una declaración o expresión estando sintácticamente correcta, puede generar un error cuando se intenta ejecutar. Los errores detectados durante la ejecución se llaman excepciones.

Cuando ocurre un error durante la ejecución de un programa, Python crea una excepción. Si no se controla esta excepción la ejecución del programa se detiene y se muestra el error (traceback).

Las principales excepciones definidas en Python son:

- **ZeroDivisionError:** Ocurre cuando se intenta dividir por cero.
- **OverflowError:** Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
- **IndexError:** Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
- **KeyError:** Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
- **FileNotFoundError:** Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
- **ImportError:** Ocurre cuando falla la importación de un módulo.

En el caso de Python, el manejo de excepciones se hace mediante los bloques que utilizan las sentencias try, except y finally.

### Errores de sintaxis

Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción, se utiliza el término levantar para referirse a la acción de generar una excepción.

A continuación se ubica el bloque except, que se encarga de capturar la excepción y nos da la oportunidad de procesarla mostrando por ejemplo un mensaje adecuado al usuario.
