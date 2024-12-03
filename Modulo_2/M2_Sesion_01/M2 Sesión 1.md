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

---

## Introducción al desarrollo web y HTML

## ¿Qué es el desarrollo web?

Desarrollo web es un término que nos define el desarrollo, creación e incluso, mantención de sitios web. De esta forma, incorpora la estructuración, funcionalidad y apariencia que tendrá un sitio web y que estará a cargo de un desarrollador web, personaje encargado de conocer los requerimientos que se deben cumplir para dar con la solución a una problemática planteada.

- W3C

  La W3C es un consorcio internacional que genera recomendaciones y estándares que aseguran el crecimiento de la World Wide Web (WWW o red informática mundial) a largo plazo. El objeto de la W3C es crear un sistema abierto con tecnologías abiertas y estandarizadas, para que todos puedan usarlas.

- HTML

  Es el acrónimo de HyperText Markup Language o, Lenguaje de Marcas de Hipertexto. Es el componente más básico de la Web y cumple la función de definir y estructurar las secciones, párrafos, encabezados, enlaces, imágenes, entre otras cosas que componen una página web.

- Visual Studio Code

  Para comenzar a trabajar en el desarrollo Frontend, debemos contar con un editor de código fuente. En esta unidad utilizaremos Visual Studio Code, editor de código fuente ligero pero potente que se ejecuta en el escritorio y se encuentra con versión disponible para Sistema Operativo Windows, MacOS y Linux . Para conocer más en detalle puede visitar su sitio web oficial Visual Studio Code.

### Tipos de desarrollo

El desarrollo web, de manera general, se divide en tres ramas, o en tres tipos de desarrollos: el Backend, el Frontend y el Full Stack

- Frontend

  Es la parte encargada de realizar todo aquello que el usuario verá al momento de acceder a un sitio web. En esta parte del desarrollo se realiza la composición, diseño e interactividad de una página web utilizando una triada bastante común: HTML, CSS y JAVASCRIPT.

- Backend

  Es aquel punto del desarrollo que se encarga de realizar lo que el usuario no ve. Es decir, se encarga de desarrollar aquella parte del sitio web que se encuentra “al lado del servidor” y que incluye la base de datos y la aplicación que dispondrá los datos sustraídos desde la base de datos, de manera tal que luego puedan ser visualizados por el usuario.

- Fullstack

  Es aquel desarrollador que cuenta con la capacidad y conocimientos para desarrollar tanto en el Backend como en el Frontend . Comúnmente estos desarrolladores están interesados en ambas áreas y, por lo tanto, son capaces de estructurar aquello que “vera el usuario” como aquello que “no vera el usuario”.
