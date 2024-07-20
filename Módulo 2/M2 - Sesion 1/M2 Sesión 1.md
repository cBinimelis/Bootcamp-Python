# Módulo II - Sesión I

## Agenda

- HTML Introducción
- HTML Etiquetas
- VS Code (Editor de Código)
- Documento HTML
- Ejecutarlo desde tu PC
- Enlaces
- Imágenes

## Introduccion a HTML

HTML es el acrónimo de HyperText Markup Language o, en español, Lenguaje de Marcas de
Hipertexto. Es el componente más básico de la Web y cumple la función de definir el significado y la
estructura del contenido web, es decir, de estructurar las secciones, párrafos, encabezados, enlaces,
imágenes, entre otras cosas que componen una página web.

Comúnmente es utilizado en conjunto con CSS, tecnología que permitirá manejar el diseño de la
página web estructurada con HTML y, a su vez, con JavaScript, lenguaje de programación que
permitirá dar interactividad, acceso a datos provenientes de una base de datos, animaciones, entre
otras cosas, también a la página estructurada con HTML.

## Etiquetas HTML

- `h1`, `h2`, `h3`, `h4`, `h5`
- `p`
- `br`
- `ul`, `ol`, `li`
- `table`, `tr`, `td`
- `thead`, `th`
- `tbody`
- `a`

## VS Code

Se utilizará dentro del bootcamp el editor de texto VS Code para poder trabajar con los documentos HTML.

## Documento HTML

- Extensión:
  > ".html"
- Modo de nombrado:
  > "nombre.html"
- Nombres:
  > Los nombres deben ser alusivos a la funcionalidad del documento.
- Estructura:

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Document</title>
    </head>
    <body></body>
  </html>
  ```

## Ejecutarlo desde tu PC

Para ejecutar una pagina HTML simplemente puede abrirlo desde el explorador del archivo o presionar CTRL + F5 en el teclado.

## Enlaces

Rutas

- `.\` ruta al mismo nivel
- `..\` Ruta iniciando a nivel superior

Target

- `_self` Carga la URL en el mismo contexto de navegación que el actual. Este es el comportamiento por defecto.
- `_blank` Carga la URL en un nuevo contexto de navegación. Usualmente es una pestaña, sin embargo, los usuarios pueden configurar los navegadores para utilizar una ventana nueva en lugar de la pestaña.
- `_parent` Carga la URL en el contexto de navegación padre (parent) del actual. Si no existe el padre, este se comporta del mismo modo que `_self`.

- `_top` Carga la URL en el contexto más alto de navegación (el cual es un ancestro del actual, y no tiene padre (parent)). Si no hay padre (parent), este se comporta del mismo modo que `_self`.
