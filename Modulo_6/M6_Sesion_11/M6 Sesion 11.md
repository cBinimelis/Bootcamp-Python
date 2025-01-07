# Modulo VI - Sesión XI

## Agenda

- El sitio administrativo de Django II
- Probando usuarios en el modelo AUTH

## El sitio administrativo de Django II

La aplicación de administración de Django puede usar tus modelos para construir automáticamente un área dentro del sitio que puedes usar para crear, consultar, actualizar y borrar registros. Todo lo que debes hacer para agregar tus modelos a la aplicación admin es registrarlos.

### Registrando los modelos

Primero, abre admin.py en la aplicación catálogo (/locallibrary/catalog/admin.py).

Registra los modelos copiando el siguiente texto al final del archivo:

```python
from .models import Author, Genre, Book, BookInstance

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)
```

### Creando un administrador

Para crear un usuario administrador se debe ejecutar el comando `python manage.py createsuperuser` e ingresar un nombre de usuario, correo y contraseña fuerte.

Para probar el inicio de sesión del usuario ejecutando `python manage.py runserver` e ingresando las credenciales en `http_//127.0.0.1:8000/admin/`

## Probando usuarios en el modelo AUTH

```python

INSTALLED_APPS = [
    #...
    "django.contrib.auth",            # Framework principal de autenticación y sus modelos
    "django.contrib.contenttypes",    # Sistema de tipos de contenido de Django. (Permite asociar los permisos a los modelos)
    #...
]

MIDDLEWARE = [
    #...
    "django.contrib.sessions.middleware.SessionMiddleware",     # Maneja sesiones a través de las peticiones
    #...
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Asocia usuarios a peticiones usando sesiones
    #...
]

```

## Administrando usuarios y grupos

```python
from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername','myemail@crazymail.com','mypassword')

# Update fields and then save again
user.first_name = 'John'
user.last_name='Smith'
user.save()
```
