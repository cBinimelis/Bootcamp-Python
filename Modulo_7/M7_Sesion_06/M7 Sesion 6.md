# Modulo VII - Sesión VI

## Agenda

- Migraciones

## Migraciones

La migración es el proceso mediante el cual se realiza una transferencia de datos que puede ser de unos sistemas de almacenamiento de datos a otros, de unos formatos de datos a otros o entre diferentes sistemas informáticos.

### Problemas que resuelve

La migración es un poderoso proceso mediante el cual realizamos una transferencia de datos con seguridad para no perder información.

Los archivos de migración para cada aplicación viven en un directorio de "migraciones" dentro de esa aplicación, y están diseñados para comprometerse y distribuirse como parte de su código base.

### Utilizando las migraciones

Hay varios comandos que se usarán para interactuar con las migraciones y el manejo de Django del esquema de la base de datos:

- **migrate:** Que es responsable de aplicar y no aplicar las migraciones.
- **makemigrations:** Que es responsable de crear nuevas migraciones basadas en los cambios que ha realizado en sus modelos.
- **sqlmigrate:** Que muestra las instrucciones SQL para una migración.
- **showmigrations:** Que enumera las migraciones de un proyecto y su estado.

### Parámetros

Comando: `django-admin`

- `makemigrations <my_app>`: Generar migraciones para my_app.
- `makemigrations –merge`: Resolver conflictos de migración para todas las aplicaciones.
- `makemigrations –merge <my_app>`: Resolver conflictos de migración para my_app.
- `makemigrations –name <migration_name><my_app>`: Genera una migración para my_app con el nombre migration_name.
- `migrate <my_app>`: Aplicar migraciones pendientes de my_app a la base de datos.
- `migrate <my_app><migration_name>`: Aplicar o no aplicar hasta el nombre de migration_name.
- `migrate <my_app> zero`: Desplegar todas las migraciones en my_app.
- `sqlmigrate <my_app> <migration_name>`: Imprime el SQL para la migración nombrada.
- `showmigrations`: Muestra todas las migraciones para todas las aplicaciones.
- `showmigrations <my_app>`: Muestra todas las migraciones en my_app.

### Utilizando las migraciones de Django

El makemigrations es responsable de empaquetar los cambios de su modelo en archivos de migración individuales, análogos a los commits, y migrate es responsable de aplicarlos a su base de datos.

Los tres pasos para trabajar las migraciones son:

1. Cambiar los modelos (en models.py).
2. Ejecutar el comando python manage.py makemigrations para crear migraciones para esos cambios.
3. Ejecutar el comando python manage.py migrate para aplicar esos cambios a la base de datos.

- Crear migraciones: `manage.py sqlmigrate polls 0001`
- Comprobar el modelo: `manage.py check`
- Migrar las bases de datos: `manage.py migrate`
