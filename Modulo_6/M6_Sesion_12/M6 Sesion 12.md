# Modulo VI - Sesión XII

## Agenda

- Mejores prácticas en Django

## Mejores prácticas en Django

### Generar un archivo requirements.txt

para crear este archivo se utiliza el comando `pip freeze > requirements.txt`, lo cual crea un archivo con los nombres de las distintas librerías que utiliza el proyecto con sus respectivas versiones. Para luego instalar estas librerías se utiliza el comando `pip install -r requirements.txt`

### El orden de los imports

Se recomienda que las importaciones se coloquen en la parte superior del archivo, en líneas separadas y se agrupen en el siguiente orden:

1. Future (si es que se desea importar)
2. Librerías nativas o estándares de Python
3. Librerías de terceros
4. Paquetes propios de Django o el framework a utilizar
5. Paquetes o aplicaciones locales (de nuestro proyecto)
6. Try/Except en un import

### Generalidades

- **Modelos:** Por lo general se recomienda que los modelos sean nombrados en forma Singular y si contiene más de una palabra, la primera letra de cada palabra debe ir en Mayúscula.( UpperCamelCase )
- **Campo Booleano (BooleanField):** Se recomienda no declarar un campo de tipo BooleanField con null=True o blank=True; si deseas que el campo booleano sea opcional, utiliza el tipo de campo NullBoleanField.
- **Nombre de Campos de Modelo:** Los nombres de los campos de un modelo se deben escribir en minúscula, si se el campo posee más de una palabra, deben unirse mediante sub guiones(\_).
- **Modelos Abstractos:** Se recomienda por lo general el uso de modelos Abstractos para evitar repetir la escritura de campos globales, recuerda que los Modelos no son más que clases y se utiliza la Programación Orientada a Objetos para su definición.

- **Orden de un modelo:** Cuando escribimos nuestros modelos, debemos mantener un orden al escribir los campos, los campos de managers personalizados, la clase Meta, el método **str**, etc, procura mantener el siguiente orden:
  ```python
  # Los campos que hagan referencia a Managers personalizados
  class Meta
  def __str__()
  def save()
  def get_absolute_url()
  # Otros métodos propios que desees añadir
  ```
- **Estructura de la plantilla (Template):** Hay dos formas principales de organizar la estructura de su plantilla en Django: la forma predeterminada a nivel de aplicación y un enfoque personalizado a nivel de proyecto:
  - Nivel de Aplicación
  - Nivel de Proyecto
