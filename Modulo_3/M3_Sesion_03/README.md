# Módulo III - Sesión III

## Agenda

- Sintaxis Básica
- Funcion print
- Variables
- Operaciones Matemáticas
- Módulos
- Paquetes

## Sintaxis Básica

Lo primero es aprender a realizar los comentarios de código, la primera manera de realizar un comentario es hacerlo por linea, esto se realiza con el símbolo `#`

`# comentario de linea única`

Lo siguiente es poder realizar comentarios que abarquen varias lineas.

```python
"""
ESTO
ES UN
COMENTARIO
MULTILINEA
"""
```

El método de distinguir los bloques de código en python es por medio de la identación, es absolutamente necesario que el código esté correctamente identado para evitar conflictos a la hora de ejecución.

---

## Conceptos Básicos de Python

### Instrucción Print

Para imprimir texto en pantalla Python cuenta con la función print() y su sintaxis es muy sencilla.

```python
>>> print('hola mundo')
```

Dará como resultado la impresión en pantalla de "hola mundo"

```python
>>> cadena = "hola mundo de nuevo"
>>> print(cadena)
```

Dará como resultado la impresión en pantalla del contenido de la variable cadena, que en este caso es “hola mundo de nuevo”.

### Operaciones aritméticas básicas

Python nos permite realizar las siguientes operaciones aritméticas básicas:

Suma (+) Resta (-) Multiplicación (\*) División (/)

- División entera (//) – devuelve solo la parte entera del resultado de la división.
- Módulo o resto (%) – devuelve el resto de la división de 2 números
- Potencia (\*\*) – devuelve el resultado en elevar un número a otro

### Sintaxis Básica

Los nombres de variables no ameritan símbolos adicionales como el $ para designarlos, basta con escribir el nombre de la variable que se desea y asignarle su valor. Es importante tomar en cuenta que existe diferenciación entre mayúsculas y minúsculas, el nombre de la variable no puede empezar con un número, tampoco está permitido el uso de guiones (-) o de espacios en blanco. Ejemplo:

```python
>>> cadena = "esto es un segmento de texto"
```

### Identación

Es posible usar tabulación o espacios, la regla general es que se utilicen 4 espacios en caso de usar estos últimos. Ejemplo:

```python
if True:
    print (“True”)
```

En caso de no usar la identación el código podría dar un resultado completamente inesperado o simplemente arrojar un mensaje de error.

El uso de punto y coma (;) al final de una línea de código no es necesario en Python.

### Manejo de módulos

Para hacer uso de un módulo debemos primero importarlo con la sentencia import. Este sentencia la podemos utilizar en cualquier lugar del código de programación, y una vez ejecutada tendremos acceso a todo el código contenido dentro del archivo importado:

```python
import utilidades, funciones
```

Cuando importamos un módulo, Python buscará en ruta de búsqueda en la variable de entorno PYTHONPATH del sistema operativo. PYTHONPATH puede ser configurada en la ventana de consola haciendo uso del siguiente código:

```
set PYTHONPATH = C:\python\lib;
```

### Manejo de paquetes

Existen varias formas para hacer la importación de un paquete, todas ellas haciendo uso de la sentencia import.

```python
>>>import matematica.aritmetica
>>>print (matematica.aritmetica.sumar (7, 5))
```
