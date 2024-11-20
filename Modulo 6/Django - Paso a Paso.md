# Django

## Crear un proyecto: paso a paso

1. Crear un proyecto, cuidando que se cree un entorno virtual `venv`.
2. Abrir la terminal y activar el entorno virtual usando `py venv/Scripts/activate`.
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

5. Una vez creado el proyecto, pedes agregar todas las vistas necesarias para hacer que tu landing page funcione adecuadamente, siguiendo los siguientes conceptos:
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
   - **B:** Crear en el mismo nivel de la app `mysite` una carpeta llamada `templates`
   ```
   📂 mysite
   ┣ 📂 mysite
   ┣ 📂 templates
   ┗ 📂 venv
     ┗ 📜 pyvenv.cfg
   ```
   - **C:** Crear dentro de `templates` un archivo llamado `base.html`, acá vas a declarar todo el html principal, el cual servirá como template padre para aplicar la herencia. Recuerda que lo que va acá se cargará en todos los templates que hereden de el.

> [!IMPORTANT]
> Acá es donde debes colocar los archivos de bootstrap, tus archivos de estilo, archivos javascript y todos aquellos archivos que correspondan a tu landing page.

    - D

```
   📦mysite
   :package: mysite
   ┣ :open_file_folder: client
   ┣ 📂client
   ┣ 📂node_modules
   ┣ 📂server
   ┃ ┗ 📜index.js
   ┣ 📜.gitignore
   ┣ 📜package-lock.json
   ┗ 📜package.json


:+1: This PR looks great - it's ready to merge! :shipit:
```
