# Modulo VII - Sesión IX

## Agenda

- CRUD en Django

## CRUD en Django

### (Create, Read, Update and Delete)

Para crear un nuevo proyecto utilizamos la siguiente instrucción:
`django-admin startproject linkdump`

La aplicación se va a llamar linkdump, el comando anterior crea un directorio linkdump en el que podemos encontrar los siguientes ficheros:
`__init__.py`: Define nuestro directorio como un módulo Python válido.
`manage.py`: Utilidad para gestionar nuestro proyecto: arrancar servidor de pruebas, sincronizar modelos, etc.
`settings.py`: Configuración del proyecto.
`urls.py`: Gestión de las urls. Este fichero sería el controlador de la aplicación. Mapea las url entrantes a funciones Python definidas en módulos.

A continuación se va a definir los parámetros de acceso a la base de datos, en el gestor de base de datos mysql, para ello se modifica algunas líneas del fichero settings.py:

```python
DATABASES ""{
  'default':{
      'ENGINE': 'mysql',
      'NAME': 'bdurl',
      'USER': 'bduser',
      'PASSWORD': 'passuserbd',
      'HOST': '',
      'PORT': '',
  }
}
```

Creamos las tablas necesarias para la administración de nuestra página con el comando:

```bash
python manage.py syncdb
```

Para ello vamos a crear una aplicación (que se llamará linktracker) en nuestro proyecto:

```bash
python manage.py startapp linktracker
```

Vamos a crear el modelo de datos, para ello añadimos en el fichero linktracker/models.py:

```python
from django.db import models

#Create your models here.

class Link (models.Model):
  link_description = models.CharField(max_length = 200)
  link_url = models.CharField(max_length = 200)
```

Añadimos nuestra aplicación (linkdump.linktracker) en la lista INSTALLED_APPS que encontramos en el fichero settings.py y volvemos a actualizar nuestra base de datos, para crear la nueva tabla:

```bash
python manage.py syncdb
```
