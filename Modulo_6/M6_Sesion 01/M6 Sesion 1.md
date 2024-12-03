# Modulo VI - Sesión I

## Agenda

- Django
- Características
- Instalación
- MVC / MTV
- Estructura
- Rutas
- Primera página

## Django

Es un framework de desarrollo web creado en 2005, es gratuito y de código abierto, lo que significa que no está sujeto a ninguna plataforma en particular, y puede ejecutar sus aplicaciones en muchas distribuciones de Linux, Windows y Mac OS.

### Características

- **Rápido desarrollo:** Django permite desarrollar aplicaciones de manera rápida con un enfoque en la reutilización de componentes y código.
- **Seguro:** Incluye protección contra ataques comunes, como inyección SQL, Cross-Site Scripting (XSS) y Cross-Site Request Forgery (CSRF).
- **Escalable:** Su estructura modular y de alto rendimiento permite aplicaciones a gran escala.
- **"Baterías incluidas":** Django proporciona una serie de herramientas integradas para manejar bases de datos, formularios, autenticación y más.

### ¿Por qué usarlo?

- Es el único framework que “por defecto” viene con un sistema de administración activo, listo para ser utilizado sin ningún tipo de configuración.
- Es un framework web de alto nivel escrito en Python.
- Su ORM (object relational mapping o manejadores de objetos relacionales), nos permite interactuar con una base de datos de manera muy práctica.
- Django puede ser (y ha sido) usado para construir casi cualquier tipo de sitio web.
- Puede funcionar con cualquier framework en el lado del cliente, y puede devolver contenido en casi cualquier formato (incluyendo HTML, RSS feeds, JSON, XML, etc).
- Django permite protección contra algunas vulnerabilidades de forma predeterminada.
- Django usa un componente basado en la arquitectura “shared-nothing” (cada parte de la arquitectura es independiente de las otras).
- Está escrito usando principios y patrones de diseño para fomentar la creación de código mantenible y reutilizable.
- Django puede ser instalado en distintos sistemas operativos, además de poder ser usado con Python 2 y 3.
- El entorno de desarrollo de es una instalación de Django en tu computadora local, la cual puede ser usada para desarrollar y probar apps antes de ser desplegadas al entorno de producción.

### Entorno desarrollo vs producción

El entorno de producción es el que está dirigido al usuario final, es el lugar donde correrá el código una vez está funcionando públicamente.

El entorno de desarrollo es donde se crean las aplicaciones, y suele contener configuraciones que les ayudan en el proceso. Por ejemplo, cuando tenemos el DEBUG en True.

| Django                                            | Python                                                                            |
| ------------------------------------------------- | --------------------------------------------------------------------------------- |
| Es un marco Web                                   | Es un lenguaje de programación                                                    |
| Está desarrollado por Django Software Foundation. | Está desarrollado por Python Software Foundation                                  |
| Fue lanzado en 2005                               | Fué lanzado en 1991                                                               |
| Está escrito en Python                            | Está escrito en C, pero la implementación predeterminada se llama CPython         |
| Se utiliza para desarrollo web                    | Se utiliza para desarrollar marcos como Django, Flask, Análisis de Datos, AI, etc |
| Es un marco MVT construido sobre Python           | Es un lenguaje de programación de alto nivel                                      |

### Requisitos para Django

- Tener instalado python3
- Tener instalado pip (manejador de paquetes de python)
- Instalar el paquete para generar ambientes virtuales de python (necesario solo para linux).

### Bases de datos

Django ofrece soporte oficial para las siguientes bases de datos:

- PostgreSQL.
- MariaDB.
- MySQL.
- Oracle.
- SQLite.

### Python y los entornos virtuales

- Python posee una estructura dogmática; ya que puede gestionar cualquier tarea en particular.
- Python es un lenguaje que se utiliza comúnmente para crear prototipos y desarrollar aplicaciones rápidamente.
- Django cuenta con una estructura minimalista y muy potente.
