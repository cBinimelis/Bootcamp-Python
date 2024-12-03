# Modulo IV - Sesión VII

## Agenda

- Throw de excepciones

## Throw de excepciones

### Excepciones definidas por el usuario

Los programas pueden nombrar sus propias excepciones creando una nueva clase excepción. Las excepciones, típicamente, deberán derivar de la clase Exception, directa o indirectamente.

```python
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise (MyError(3 * 2))
except MyError as error:
    print("Ocurrió una excepcion: ", error.value)

# Salida: 'Ocurrió una excepcion: ', 6
```

### Acciones de limpíeza con finally

Si una cláusula finally está presente, el bloque finally se ejecutará al final antes de que todo el bloque try se complete. La cláusula finally se ejecuta independientemente de que la cláusula try produzca o no una excepción. Los siguientes puntos explican casos más complejos en los que se produce una excepción.

Si ocurre una excepción durante la ejecución de la cláusula try, la excepción podría ser gestionada por una cláusula except. Por Ejemplo:

```python
def bool_return():
    try:
        return True
    finally:
        return False

bool_return()

# Salida: False
```

### Acciones de limpieza predefinidas

Algunos objetos definen acciones de limpieza estándar para llevar a cabo cuando el objeto ya no es necesario, independientemente de que las operaciones sobre el objeto hayan sido exitosas o no.

```python
for line in open('my file.txt'):
    print(line, end='')
```

La declaración with permite que los objetos como archivos sean usados de una forma que asegure que siempre se los libera rápido y en forma correcta.:

```python
with open('my file.txt') as f:
    for line in f:
        print(line, end='')
```
