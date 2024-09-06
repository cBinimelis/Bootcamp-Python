# Módulo III - Sesión VIII

## Agenda

- Funciones

## Funciones

Para llamar a una funcion se utiliza la palabra reservada `def` y la sintáxis de la misma sería la siguiente:

```python
def nombre_funcion(argumentos):
    <cuerpo>
    return respuesta
```

---

## Estructuras de datos en Python

Las estructuras de datos son la forma en que podemos almacenar y recuperar datos.

**Para qué se utilizan las estructuras de datos?**

- Introducir información
- Procesar la información
- Mantener la información
- Recuperar información

### Las estructuras de datos de Python

Python tiene cuatro estructuras de datos no primitivas incorporadas: **Listas**, **Diccionario**, **Tupla** y **Conjunto**.

### Set

Python Set es una colección desordenada de datos que es mutable y no permite ningún elemento duplicado.
Los conjuntos se utilizan básicamente para incluir pruebas de pertenencia y eliminar entradas duplicadas.
Las llaves ( { } ) representan a los sets, Los objetos colocados dentro de llaves se tratan como un set.

Un set se crea colocando todos los elementos dentro de llaves { }, separados por comas, o utilizando la función incorporada set().

### Listas

Las listas en Python son uno de los tipos de objetos de colección más versátiles disponibles. Los otros dos tipos son los diccionarios y las tuplas, pero en realidad son más bien variaciones de las listas.

Para crear listas, se utilizan los corchetes y se declaran los datos o elementos correspondientes. Si no se pasan elementos a los corchetes, devuelve una lista vacía.

### Tupla

Las tuplas de Python funcionan exactamente como las listas de Python, excepto que son inmutables, es decir, no pueden ser modificadas.
Normalmente se escriben dentro de paréntesis para distinguirlas de las listas (que usan corchetes)

Crear una tupla es tan sencillo como poner diferentes valores separados por comas. Usualmente ponemos este grupo de valores entre paréntesis para facilitar su lectura.

### Diccionario

El diccionario de Python es como las tablas hash en cualquier otro lenguaje.
Es una colección desordenada de valores de datos, usada para almacenar valores de datos como un mapa, que, a diferencia de otros Tipos de Datos que mantienen un solo valor como elemento, el Diccionario mantiene el par clave:valor.
Crear un diccionario es tan sencillo como colocar los elementos dentro de llaves { } separadas por comas. Cada elemento tiene una clave y un valor correspondiente que se expresa como un par (clave: valor).

## Acceder a un elemento de una estructura

- **Listas y Tuplas :** A través de su índice, para ello simplemente debemos hacer uso del operador corchete.
- **Sets :** Se puede recorrer los elementos del set utilizando un ciclo for o utilizando la palabra clave in.
- **Diccionarios :** Se puede utilizar también el operador corchete junto con la clave para obtener su valor.

## Iterando estructuras de datos

Iterar sobre una estructura de datos significa moverse a través de ella. Su sintaxis es:

```python
range (comienzo, final, paso)
```

- **Comienzo (límite superior, opcional):** Este parámetro se utiliza para proporcionar el valor índice inicial de la secuencia de enteros que se va a generar. Si mo se sumunustrs se asime por defecto que es cero.
- **Final (límite inferior, requerido):** Este parámetro se utiliza para proporcionar el índice final de la secuencia de enteros a generar, es decir, cuántos elementos se van a generar.
- **Paso (opcional):** Proporciona el incremento en enteros entre el número actual generado y el siguiente.
