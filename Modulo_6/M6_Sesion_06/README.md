# Modulo VI - Sesión VI

## Agenda

- Templates en Django
- Aplicación de filtros Contenido estático

## Templates en Django

Una plantilla (o template) es un archivo de texto que determina la estructura o diseño de un archivo (como una página HTML).

### Inclusión de templates

Una plantilla es un archivo de texto que determina la estructura o diseño de un archivo (como una página HTML), con marcadores usados para representar el contenido real. Django automáticamente buscará plantillas en un directorio llamado 'templates' de su aplicación.

Para usar el sistema de plantillas en el código Python, sólo sigue estos dos pasos:

1. Crea un objeto Template brindando el código en crudo de la plantilla como una cadena. Django también ofrece un camino para crear objetos Template especificando la ruta al archivo de plantilla en el sistemas de archivos; vamos a examinar esto en un rato.
2. Llama al método render() del objeto Template con un conjunto de variables (o sea, el contexto).

### Aplicación de filtros Contenido estático

- **STATIC_URL:** El rol es acceder a los archivos estáticos en el proyecto a través de la URL. En su archivo de configuración, defina STATIC_URL , por ejemplo: `STATIC_URL = 'static/'`
- **STATICFILE_DIR:** Se usa para incluir adicional directorios para collectstatic buscar.

  ```python
  STATIC_URL = 'static/'

  if not DEBUG:
      STATIC_ROOT= 'home/django/wor-data/site.com/static'

  STATICFILES DIRS=[
      op.path.join (BASEDIR, 'static/'),
  ]
  ```

- **BLOQUES (BLOCK - ENDBLOCK):** Se usa para anular partes específicas de una plantilla. Puede crear una jerarquía de plantillas, así que comience con base.html:

  ```html
  <body>
    {% block content %}
    <!--El contenido irá acá-->
    {% endblock content %}
  </body>
  ```

- HERENCIA DE PLANTILLAS: Es un patrón que se parece a las técnicas de programación orientada a objetos, en el que los bloques de contenido se insertan dentro de otras plantillas HTML.
- EXTENDS DE PLANTILLAS La etiqueta `extends` se usa para declarar una plantilla principal. Debe ser la primera etiqueta utilizada en una plantilla secundaria y una plantilla secundaria solo puede extenderse hasta una plantilla principal.
