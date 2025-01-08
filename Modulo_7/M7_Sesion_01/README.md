# Modulo VII - Sesión I

## Agenda

- Acceso a datos con Django

## Acceso a datos con Django

Django obtiene la estructura, acceso y control de los datos de una aplicación a través de su ORM (Object Relational Mapper), esto significa que no importa qué motor de base de datos esté usando, el mismo código seguirá funcionando.

Todo se define dentro del archivo settings.py

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test",
        "USER": "user_test",
        "PASSWORD": "password_test",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

```

### Databases

Es donde se indicará que definiremos una base de datos. Dentro, tendremos el default que contiene toda la configuración clave de la base de datos. Django soporta oficialmente las siguientes bases de datos:

- **PostgreSQL:** Django es compatible con PostgreSQL 10 y superior. Se requiere psycopg2 2.8.4 o superior, aunque se recomienda la última versión.
- **MySQL:** Django es compatible con MySQL 5.7 y superior.
- **SQLite:** Django es compatible con SQLite 3.9.0 y versiones posteriores.
- **Oracle:** Django es compatible con las versiones 19c y posteriores de Oracle Database Server. Se requiere la versión 7.0 o superior del controlador cx_Oracle Python.

### Soporte para bases NoSql

En el caso de los manejadores de bases de datos NoSql el más utilizado en el entorno Django es MongoDB. El método para conectar es a través de MongoEngine.

En este caso el archivo settings.py se comenta la sección BASES DE DATOS como se muestra en el siguiente fragmento de código y se le agrega las líneas resaltadas.

```python
    import mongoengine
    mongoengine.connect(db=DATABASE_NAME, host=DATABASE_HOTS,
    username=USERNAME, password=PASSWORD)
     # DATABASES ""{
     # 'default':{
     # 'ENGINE': 'django1', #'django.db.backends.sqlite3',
     # 'NAME': 'blogs',#DB name
     # 'USER': 'root', #DB User name <optional>
     # }
     # }
```
