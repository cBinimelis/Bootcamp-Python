# Modulo VII - Sesión III

## Agenda

- ORM y la definición del modelo

## Conexión de Django a la base de datos

Al comenzar a explorar la capa de la base de datos de Django se necesita tener en cuenta algunas configuraciones iniciales: indicarle a Django qué servidor de base de datos usar y cómo conectarse con el mismo.

- El primer paso es la configuración de un servidor de base de datos y la creación de la base de datos en este (por ej. usando la sentencia CREATE DATABASE).
- `DATABASE_ENGINE = ''` Le indica a Django qué base de datos utilizar. Si usa una base de datos con Django, DATABASE_ENGINE debe configurarse con un string de los mostrados a continuación:

| CONFIGURACION         | BASE DE DATOS | ADAPTADOR REQUERIDO |
| --------------------- | ------------- | ------------------- |
| `postgresql`          | PostgreSQL    | psycopg version 1.x |
| `postgresql_pyscopg2` | PostgreSQL    | psycopg version 1.x |
| `mysql`               | MySQL         | MySQLdb             |
| `sqlite3`             | SQLite        | No requiere         |
| `oracle`              | Oracle        | cx_oracle           |

- `DATABASE_NAME = ''` Indica a Django el nombre de la base de datos. Si está usando SQLite, especifica la ruta completa del sistema de archivos hacia el archivo de la base de datos (por ejemplo: '/home/django/mydata.db').

- `DATABASE_USER = ''` Indica a Django cuál es el nombre de usuario a utilizar cuando se conecte a la base de datos. Si está usando SQLite, dejar vacío.

- `DATABASE_PASSWORD = ''` Indica a Django cuál es la contraseña a utilizar cuando se conecte a la base de datos. Si está utilizando SQLite o no ha incluido contraseña, dejar vacío.

- `DATABASE_HOST = ''` Le indica a Django cual es el host a usar cuando se conecta a la base de datos.

**Para probar la configuración de tu base de datos**

```python
from django.db import connection
cursos = connection.cursos()
```

### Soporte para bases NoSql

- En primer lugar se debe instalar la librería postgresql_psycopg2: `pip install psycopg2-binary`
- Luego se debe crear la base de datos. Esto se puede realizar desde el PGAdmin (entorno visual) o desde el PSQL Shell.
- Realizado esto debemos editar el archivo settings.py.
  ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgreSQL_psycopg2",
            "NAME": "db_practica_orm",
            "USER": "user_db",
            "PASSWORD": "user_db",
            "HOST": "",
            "PORT": "",
        }
    }
  ```
- Hecho esto se procede a teclear el comando de migración de la base de datos: `python manage.py migrate`

En la creación del proyecto en Django y conectar a PostgreSql se sigue los siguientes pasos

- Crear un entorno virtual: `virtualenv myenv`
- Inicializar la virtualenv: `.myenv\Scripts\activate`
- Descargar Django en nuestra virtualenv: `pip install django`
- Inicializar un proyecto con Django: `django-admin startproject .`
- Crear una base de datos local con PostgreSQL y asignarle un usuario
- Cambiar la configuración de la base de datos para utilizar PostgreSQL en lugar de SQLite en settings.py dentro de nuestro proyecto.
- Instalar el conector para PostgreSQL: `pip install psycopg2`
- Migrar la base de datos: `python manage.py migrate`
- Crear un superusuario para loguearnos en el admin de Django: `python manage.py createsuperuser`
- Iniciar sesión con el usuario creado en /admin.
