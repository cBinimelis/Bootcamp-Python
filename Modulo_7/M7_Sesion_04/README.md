# Modulo VII - Sesión IV

## Agenda

- Claves primarias y CRUD
- Realizando operaciones CRUD al modelo

## Implementar la capa del modelo en Django

### Manejo de claves primarias

Una llave primaria es una columna de tabla que sirve a un propósito especial

### Llaves primarias en columnas únicas

Por defecto, Django agrega a cada modelo el siguiente campo: `id = models.AutoField(primary_key=True)`

### Llaves primarias en columnas múltiples

Django aún no tiene una clave primaria compuesta (las claves primarias compuestas también se denominan claves primarias de varias columnas)
Existe una biblioteca de terceros, con el nombre django-compositekey que hace posible crear un modelo que tiene una clave principal de varias columnas.

## Realizando operaciones CRUD al modelo

Django se basa en la arquitectura MVT(Model View Template) y gira en torno a las operaciones CRUD(Create, Read, Update, Delete).

- **Crear (Create):** cree o agregue nuevas entradas en una tabla en la base de datos.
- **Leer (Read):** leer, recuperar, buscar o ver entradas existentes como una list(Vista de lista) o recuperar una entrada particular en detalle(Vista de detalles).
- **Actualizar (Update):** actualizar o editar entradas existentes en una tabla en la base de datos.
- **Eliminar (Delete):** desactivar o eliminar entradas existentes en una tabla en la base de datos.

Para crear una aplicación, necesitamos ejecutar el siguiente comando en la consola (dentro de la carpeta de djangogirls donde está el archivo manage.py):

```bash
#MAC OS X y Linux
(myvenv) ~/djangogirls$ python manage.py startapp blog

#WINDOWS
(myvenv) C:\Users\Name\djangogirls> python manage.py startapp blog
```

### Creando un modelo

Abre blog/models.py en el editor, borra todo, y escribe código como este:

```python
# blog/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
     title = models.CharField(max_length=200)
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)
```

### Creando un objeto con el modelo

```python
# blog/views.py
if request.POST['id']
    post = Post.objects.get (id = request.POST['id'])
    try:
        for request_data_in_array in request.POST:
            request_post_values = request.POST[request_data_in_array]
            setattr(post, request_data_in_array, request_post_values)
            post.save()
```

### Borrando un objeto con el modelo

Para eliminar un solo registro, usaremos el siguiente código:

```python
record = ModelName.objects.get(title = "Título")
record.delete()
```
