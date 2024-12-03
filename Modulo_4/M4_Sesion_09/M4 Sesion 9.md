# Modulo IV - Sesión IX

## Agenda

- Apertura de archivos

## Apertura de archivos

Python ofrece una función con la que se puede crear un objeto de archivo con varios modos, uno de ellos, es el modo de lectura.

### Apertura modo lectura

- **Lectura completa del archivo:** El método read() leerá todo el contenido de un archivo y lo devolverá como una cadena de texto.
- **Lectura de una línea:** Si queremos leer un archivo línea por línea (en lugar de sacar todo el contenido del archivo de una sola vez) entonces podemos usar la función readline().
- **Apertura en modalidad escritura:** Con la función de escritura se define el contenido del archivo de texto usando la sintaxis de cadenas de Python.

### Método write()

Se puede añadir contenido a un archivo de la siguiente manera:

```python
fichero = open('datos guardados.txt', 'w')
fichero.write('Contenido a guardar"')
fichero.close()
```

### Método writelines()

También se puede utilizar el método `writelines()` y pasarle una lista

```python
fichero = open('datos guardados.txt', 'w')
lista = ['Manzana','Pera','Damasco']
fichero.writelines(lista)
fichero.close()
```

### Usando la función os.rename()

Una solución simple para cambiar el nombre de un archivo en Python es usar la función `os.rename()`:

```python
import os
os.rename('filename.txt', 'new_filename.txt')
```

### Usando la función shutil .move()

Puedes usar la función `shutil.move()` para renombrar o mover un archivo.

```python
import shutil
shutil.move('/path/to/dir/filename.txt', '/path/to/dir/new_filename.txt')
```
