# Modulo VI - Sesión V

## Agenda

- Despliegue de páginas con contenido dinámico

# Despliegue de páginas con contenido dinámico

Las páginas estáticas contienen información que no cambia hasta que el diseñador o programador la modifica manualmente.

Las páginas web dinámicas permiten cambiar fácilmente su contenido en tiempo real sin siquiera tocar el código de la página.

La puesta en producción de archivos estáticos consta de dos pasos: ejecute el comando `collectstatic`, cuando cambien los archivos estáticos, luego organice el directorio de archivos estáticos recopilados ( STATIC_ROOT ) para moverlos al servidor de archivos estáticos y servirlos.

### Desplegar una página web estática

Django mediante: `django.contrib.staticfiles`, gestiona el contenido estático

En `settings.py`, tenemos líneas exclusivamente dedicadas al manejo del contenido estático. existen 4 elementos:

- `static_root`
- `static_url`
- `staticfiles_finders`
- `staticfiles_dirs`: Este elemento permite declarar la ruta, desde la cual se enlazará el contenido estático, lo dejamos de la siguiente manera:
  `python
    STATIC_URL = "static/"
    STATICFILES_DIRS = [BASE_DIR / "static"]
    `
  Dentro del directorio static, debemos tener una carpeta por cada tipo de contenido estático, que deseemos incluir. Tendremos tres subdirectorios en static: css, img y js.
  `    📂 mysite
    ┣ 📂 mysite
    ┣ 📂 static
    ┃ ┣ 📂 css
    ┃ ┣ 📂 img
    ┃ ┗ 📂 js
    ┣ 📂 templates
    ┗ 📂 venv
   `
