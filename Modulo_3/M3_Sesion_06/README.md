# Módulo III - Sesión VI

## Agenda

- Estructuras Condicionales
- Ciclos
  - For
  - While

---

## Sentencias condicionales

Haciendo uso de las instrucciones condicionales creamos el flujo del programa, filtrando las instrucciones que no deseamos si las condiciones no son las ideales.

### Las subcondiciones

- Cada una de las condiciones que se deben cumplir las llamaremos subcondiciones. Pudiendo tener **n** cantidad de subcondiciones a evaluar, donde todas y cada una se debe cumplir para ejecutar la acción.
- Las subcondiciones pueden ser evaluadas utilizando el operador **and**, así como con el operador **or**.
- Utilizamos el **and** si necesitamos que se cumpla más de una condición. La sintaxis en caso del operador **and** es como sigue:

En el caso de que queramos que se cumpla alguna de las condiciones (cualquiera) para ejecutar la acción debemos utilizar el operador **or**.

- Cuando Python realiza la evaluación de una expresión, las subcondiciones se evalúan según el orden en que aparecen en el código, así que primero se evalúa la primera subcondición y en caso de ser verdadera (true) se evalúa la condición siguiente, y así sucesivamente.
- En caso de ser falsa una subcondición automáticamente se considera falsa toda la expresión del **if** o del **elif**, no haciendo falta evaluar las subcondiciones siguientes. Y en caso de que todas las subcondiciones sean verdaderas entonces la expresión se considera verdadera.

### Manejando múltiples condiciones con elif

Para evaluar expresiones en cascada, es decir, en caso de que la primera expresion sea falsa es necesario evaluar una nueva expresion y asi sucesivamente utilizamos elif.

En la estructura podemos tener tantos elif como sea necesario, los cualse son chequeados según el orden en que aparecen en la estructura.

### Utilizando convenciones de nombres en variables

Aun cuando no es obligatorio el uso de ningún sistema en específico para nombrar nuestras variables, funciones, entre otras. es buena práctica seguir algunas convenciones, pues así mejoramos la legibilidad de nuestro código, y facilitamos a otros entender lo que hicimos, e incluso a nosotros mismos cuando queramos hacer revisiones en el futuro.

Existen varios sistemas que se utilizan, dependiendo de que queramos nombrar:

- **lowerCamelCase**: este sistema consiste en poner todas las palabras del nombre sin espacios, escritas en minúscula, excepto la primera letra de cada palabra a partir de la
  segunda palabra.
- **UpperCamelCase**: este sistema es idéntico al anterior, excepto porque la primera letra de la primera palabra también va en mayúscula.
- **snake_case**: en este caso todas las palabras se escriben en minúsculas, y los espacios se sustituyen por guiones de piso.
- **SCREAMING_SNAKE_CASE**: este caso es igual al anterior, pero con todas las letras en
  mayúsculas.

Cuando deseamos ponerle nombre a una variable en Python, usualmente el sistema a usar es el **snake_case**.
