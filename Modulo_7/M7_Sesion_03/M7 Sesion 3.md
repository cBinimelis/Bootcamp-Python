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
