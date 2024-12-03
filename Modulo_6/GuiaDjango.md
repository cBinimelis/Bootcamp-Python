# Django

## Crear un proyecto: paso a paso

1. Crear un proyecto, cuidando que se cree un entorno virtual `venv`.
2. Abrir la terminal y activar el entorno virtual usando `venv/Scripts/activate`[^1].
3. Con la terminal aún abierta, instalar Django con el comando `pip instal django`.
4. Crear un proyecto Django con el comando `django-admin startproject mysite .`

   Una vez creado el proyecto en Django analizamos los archivos y para qué se usan:

   ```
   📂 mysite
   ┣ 📜 __init__.py
   ┣ 📜 asgi.py
   ┣ 📜 settings.py
   ┣ 📜 urls.py
   ┗ 📜 wsgi.py
   ```

   - `settings.py`: Archivo de configuración central de todo el proyecto Django.
   - `urls.py`: Archivo de rutas o urls principal del proyecto, acá van las rutas del landing page y de cada app creada.

> [!NOTE]
> Crear el proyecto de esta manera nos permite crear el proyecto django dentro del proyecto creado en el punto 1.

5.  Una vez creado el proyecto, pedes agregar todas las vistas necesarias para hacer que tu landing page funcione adecuadamente, siguiendo los siguientes conceptos:

    - **A:** Templates, para crear tus templates deber ir al archivo `settings.py` y modificar el arreglo `TEMPLATES`, cambiando específicamente la lista `DIRS`, quedando de la siguiente manera:

      ```python
      TEMPLATES = [
      {
          "BACKEND": "django.template.backends.django.DjangoTemplates",
          "DIRS": [BASE_DIR / "templates"], # Esta es la línea modificada.
          "APP_DIRS": True,
          "OPTIONS": {
              "context_processors": [
                  "django.template.context_processors.debug",
                  "django.template.context_processors.request",
                  "django.contrib.auth.context_processors.auth",
                  "django.contrib.messages.context_processors.messages",
              ],
          },
      },
      ]
      ```
      Crear en el mismo nivel de la app `mysite` una carpeta llamada `templates`

      ```
      📂 mysite
      ┣ 📂 mysite
      ┣ 📂 templates
      ┗ 📂 venv
      ```

    - **B:** Configurar los archivos estáticos en `settings.py`

      ```python
      # Static files (CSS, JavaScript, Images)
      # https://docs.djangoproject.com/en/5.1/howto/static-files/
      STATIC_URL = "static/"
      STATICFILES_DIRS = [BASE_DIR / "static"] #Se agrega esta fila para crear una ruta absoluta
      ```
      Además, en el mismo nivel de la app `mysite` se debe crear una carpeta con el nombre `static`
      ```
      📂 mysite
      ┣ 📂 mysite
      ┣ 📂 static
      ┣ 📂 templates
      ┗ 📂 venv
      ```

    - **C:** Crear dentro de `templates` un archivo llamado `base.html`, acá vas a declarar todo el html principal, el cual servirá como template padre para aplicar la herencia. Recuerda que lo que va acá se cargará en todos los templates que hereden de el. (Acá es donde debes colocar los archivos de bootstrap, tus archivos de estilo, archivos javascript y todos aquellos archivos que correspondan a tu landing page.)

      ```html
      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
          />
          <title>{% block title%} mysite {% endblock %}</title>
          {% load static %}
          <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" />
          <link rel="stylesheet" href="{% static 'css/style.css' %}" />
        </head>
        <body>
          {% block content %} {% endblock %}
          <script src="{% static 'js/bootstrap.js' %}"></script>
        </body>
      </html>
      ```
      ```
      📂 mysite
      ┣ 📂 mysite
      ┣ 📂 static
      ┣ 📂 templates
      ┃ ┗ 📜 base.html
      ┗ 📂 venv
      ```

    - **D:** Crear todos los templates necesarios para las rutas que vas a declarar:

      - home
      - contact
      - about
      - projects
      - etc

        ```html
        {% extends 'base.html' %} {%block title%} mysite {%endblock%} {%block
        content%}
        <h1>About</h1>
        {% endblock %}
        ```

    - **E:** Ir al archivo `views.py` dentro de tu app `mysite` y crear todas las vistas necesarias para que puedan ser llamadas desde `urls.py`

      ```python
      from django.shortcuts import render

      def home(request):
          return render(request, "home.html")

      def contact(request):
          return render(request, "contact.html")

      def about(request):
          return render(request, "about.html")
      ```

    - **F:** Ir al archivo `urls.py` dentro de tu app `mysite` y crear todas las rutas necesarias, cuidando que hagan coherencia con tus templates o vistas de tu landing.

      ```python
      from django.contrib import admin
      from django.urls import path
      from . import views

      urlpatterns = [
          path("", views.home, name="home"),
          path("admin/", admin.site.urls),
          path("contact/", views.contact, name="contact"),
          path("about/", views.about, name="about"),
      ]
      ```

6.  Para comenzar a agregar apps a tu sistema web, lo debes hacer con el comando `python manage.py startapp dashboard`, esto creará una app a nivel de `mysite` con la siguiente estructura:

    ```
    📦mysite
    ┣ 📂dashboard
    ┃ ┣ 📂migrations
    ┃ ┣ 📜__init__.py
    ┃ ┣ 📜admin.py
    ┃ ┣ 📜apps.py
    ┃ ┣ 📜models.py
    ┃ ┣ 📜tests.py
    ┃ ┗ 📜views.py
    ┣ 📂mysite
    ┣ 📂static
    ┣ 📂templates
    ┗ 📂venv
    ```

- `admin.py`: Permite declarar los modelos y sus configuraciones, para que sean administrados desde el panel de administrador
- `models.py`: Permite declarar todas las configuraciones de tus modelos.
- `views.py`: Permite declarar todas las funciones que reciven las peticiones desde el front y que llaman desde `urls.py`

7. Una vez creada tu app puedes agregar todas las rutas necesarias para hacer que tu app funcione adecuadamente, siguiendo lo siguientes pasos:

   - **A:** Ir a `mysite/settings.py` y agregar la app recién creada al arreglo `INSTALLED_APPS`

     ```python
     INSTALLED_APPS = [
         "django.contrib.admin",
         "django.contrib.auth",
         "django.contrib.contenttypes",
         "django.contrib.sessions",
         "django.contrib.messages",
         "django.contrib.staticfiles",
         "dashboard",
     ]
     ```

   - **B:** Crear dentro de tu app una carpeta llamada templates y dentro de esta, otra carpeta con el mismo nombre de tu app

     ```
     📦mysite
     ┣ 📂dashboard
     ┃ ┣ 📂migrations
     ┃ ┣ 📂templates
     ┃ ┃  ┗ 📂dashboard
     ┃ ┣ 📜__init__.py
     ┃ ┣ 📜admin.py
     ┃ ┣ 📜apps.py
     ┃ ┣ 📜models.py
     ┃ ┣ 📜tests.py
     ┃ ┗ 📜views.py
     ┣ 📂mysite
     ┣ 📂static
     ┣ 📂templates
     ┗ 📂venv
     ```

   - **C:** Crea dentro de la carpeta `templates` que está a nivel de tu proyecto, una carpeta llamada `general` y allí crear tu archivo `base.html`, el cual se usará como template padre para la herencia de tus apps.

     ```
     📦mysite
     ┣ 📂dashboard
     ┣ 📂mysite
     ┣ 📂static
     ┣ 📂templates
     ┃ ┣ 📂general
     ┃ ┃  ┗ 📜base.html
     ┃ ┣ 📜about.html
     ┃ ┣ 📜base.html
     ┃ ┣ 📜contact.html
     ┃ ┗ 📜home.html
     ┗ 📂venv
     ```

   - **D:** Crear todos los templates necesarios para las rutas que vas a declarar.
   - **E:** Ir al archivo `views.py` dentro de tu app y crear todas las vistas necesarias para que puedan ser llamadas desde `urls.py`
   - **F:** Crear en tu app el archivo `urls.py`, en el cual deberás crear todas las rutas necesarias, cuidando que hagan coherencia con tus templates o vistas de tu app.
   - **G:** Ir al archivo `mysite/urls.py` y agregar las urls declaradas en tu app.

     ```python
     from django.contrib import admin
     from django.urls import path
     from . import views

     urlpatterns = [
         path("", views.home, name="home"),
         path("admin/", admin.site.urls),
         path("contact/", views.contact, name="contact"),
         path("about/", views.about, name="about"),
         path("dashboard/", include("dashboard.urls")),
     ]
     ```

8. Para agregar PostgreSQL a tu proyecto, deber ir al archivo `mysite/settings.py` y agregar el driver respectivo, más las credenciales de tu base de datos.

   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "mysite_db",
           "USER": "postgres",
           "PASSWORD": "******",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }
   ```

   Luego debes instalar la librería **psycopg2** con el comando `pip install psycopg2` en tu consola de comandos, esta librería te permitirá acceder a tu base de datos y realizar las migraciones. Para finalizar, en la misma consola ejecutamos el comando `py manage.py createsuperuser` para crear un usuario con privilegios de administrador.

9. Para ejecutar tus migraciones, incluyendo las iniciales, debes utilizar los comandos:
   - `python manage.py makemigrations`: Esto buscará todos los modelos agregados mo modificados y creará los archivos de migración.
   - `python manage.py migrate`: Esto ejecutará las migraciones del comando anterior y llevará los cambios a la base de datos.
10. Para agregar autenticación a nuestro proyecto debemos ir a `mysite/settings.py` y agregar lo siguiente:

    ```python
    LOGIN_REDIRECT_URL = "dashboard:home"
    LOGOUT_REDIRECT_URL = "login"
    LOGIN_URL = "/login/"
    ```

    - `LOGIN_REDIRECT_URL`: Url a donde será redireccionada la aplicación cuando alguien realice un login exitoso.
    - `LOGOUT_REDIRECT_URL`: Url a donde será redireccionada la aplicación cuando se haga un logout exitoso.
    - `LOGIN_URL`: Url donde se encuentra el inicio de sesión.

11. Ir a `mysite/urls.py` y agregar las rutas de autenticación login y logout.

    ```python
    urlpatterns = [
        path("", views.home, name="home"),
        path("admin/", admin.site.urls),
        path("contact/", views.contact, name="contact"),
        path("about/", views.about, name="about"),
        path("dashboard/", include("dashboard.urls")),
        path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
        path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    ]
    ```

12. Para proteger rutas y que estas solo puedan ser accedidas cuando una persona está logueada, se debe ocupar el decorador `@login_required`.

    ```python
    from django.shortcuts import render
    from django.contrib.auth.decorators import login_required

    @login_required
    def home(request):
        return render(request, "dashboard/home.html")
    ```

[^1]: Si es que no estás utilizando PyCharm.
