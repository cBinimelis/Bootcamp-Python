# Modulo VI - Sesión VIII

## Agenda

- Autenticación y autorización

## Autenticación y autorización

### ¿Cómo utilizamos el modelo AUTH de Django?

La configuración por defecto del sistema de autenticación de Django satisface las necesidades más comunes de los proyectos, maneja una gama razonablemente amplia de tareas y tiene una implementación cuidadosa de contraseñas y permisos.

### El objeto User:

El núcleo del sistema de autenticación lo conforman los objetos de usuario y representan a las personas que interactúan con el sistema, se utilizan para habilitar funcionalidades como restringir el acceso, registrar perfiles de usuario, asociar contenido con creadores, etc. Sólo existe una clase de usuario en el marco de autenticación de Django, es decir,'superusers' o administradores y 'staff'.

```python
from django.contrib.auth import authenticate

user = authenticate (username='juan', password='secret')
if user is not None:
    #Credenciales autenticadas
else:
    #Credenciales no autenticadas
```

La forma más directa de crear usuarios es hacer uso de la función auxiliar create_user() incluida en el sistema de autenticación, de la siguiente manera:

```shell
$ python manage.py createsuperuser --username=jack --email=jack@bubbles.com
```

- **Autenticación en solicitudes web:** Django hace uso de sesiones y middleware para conectar el sistema de autenticacion a los objetos de solicitud. Estos proporcionan un atributo `request.user` en cada solicitud que representa al usuario actual.

```python
if request.user.is_authenticated:
    # Opciones para usuario autenticado
else:
    # Opciones para usuario anónimo
```

- **Inicio de sesión para un usuario:** Al ser autenticado un usuario, se debo atar a la sesión actual, esto se logra a través de la función `login()`.

```python
login(request, user, backend = None)
```

Cierre de sesión para un usuario se utiliza la función `django.contrib.auth.logout()` dentro de la vista. La función toma un objeto HttpRequest y no devuelve ningún valor.

**Ejecutando las migraciones**

```shell
$ python manage.py makemigrations
```

Al tener los nuevos archivos de migración, debe aplicarlos a su base de datos para asegurarse de que funcionen como se espera

```shell
$ python manage.py migrate
```

Para comenzar una migración de datos, se crea un archivo de migración vacío:

```shell
$ python manage.py makemigrations --empty nombre_de_app
```

- **INSTALLED_APPS:**

  - `django.contrib.auth`: que contiene el núcleo del marco de autenticación y sus modelos predeterminados.
  - `django.contrib.contenttypes`: que es el sistema de tipos de contenido de Django, que permite asociar permisos con los modelos que crea.

- **Configuración en settings.py:** La configuración requerida por el módulo de autenticación de usuarios de Django está incluida en el archivo settings.py. La configuración consiste en dos items que se ubican en la sección INSTALLED_APPS y dos más en la sección MIDDLEWARE:
  - **SessionMiddleware:** Que asocia usuarios con solicitudes mediante sesiones. Con esta configuración en su lugar, ejecutar el comando manage.py migrate crea las tablas de base de datos necesarias para los modelos y permisos relacionados con la autenticación para cualquier modelo definido en sus aplicaciones instaladas.
  - **AuthenticationMiddleware:** Que es el sistema de tipos de contenido de Django, que permite asociar permisos con los modelos que crea.
