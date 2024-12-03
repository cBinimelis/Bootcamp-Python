# Modulo VI - Sesión IV

## Agenda

- Archivos de Configuración

## Archivos de Configuración

Cualquier directorio con un archivo `__init__.py` se considera un paquete de Python. La siguiente imagen muestra la estructura de un módulo Python estándar.

- `settings.py`: Al momento de generar un proyecto consigo se crea un archivo llamado settings.py que es nuestro archivo de configuración.
- `BASE_DIR`: Esta es la variable que tiene por contenido la ruta a una determinada zona de tu proyecto, por defecto lleva la ruta al archivo settings.py.
- `SECRET_KEY`: Esta carpeta de plantillas contiene todas las plantillas que creará en diferentes aplicaciones de Django.
- `DEBUG`: Django proporciona un depurador integrado que facilita mucho la vida del desarrollador, DEBUG proporciona una variable boleana que sólo acepta True o False.
- `ALLOWED_HOSTS`: Host permitidos para el proyecto, mientras el DEBUG esté en True esta variable puede permanecer vacía, cuando DEBUG cambie a False debes agregar un host obligatorio que puede ser el dominio de tu sitio.
- `MIDDLEWARE`: Es un sistema de "complemento" ligero y de bajo nivel para alterar globalmente la entrada o salida de Django.
- `TEMPLATES`: Todo proyecto en Django tiene esta variable que lleva una clave secreta, el contenido de esta variable siempre debe estar protegida y nunca escrita como texto plano dentro del archivo.
- `INSTALLED_APPS`: Variable donde agregamos las aplicaciones de terceros que vayamos utilizando o las que vayamos creando.
- `variables de url`:Se utilizan para almacenar archivos multimedia o estáticos. Cree carpetas estáticas y multimedia en el directorio principal.
- `media_url`:Es la ruta relativa a BASE_DIR. Esta variable se utiliza para almacenar los archivos multimedia.
- `static_url`:Es la ruta relativa a BASE_DIR. Esta variable se utiliza para almacenar archivos estáticos.
- `DATABASE`: Aquí podemos configurar cualquier motor de base de datos que Django utilice: MySQL, Postgres, Oracle, SQLite (por defecto).

Las variables ROOT son rutas absolutas. Estas variables se utilizan para recuperar archivos multimedia o estáticos.

- `MEDIA_ROOT`: Es la ruta absoluta. Esta variable se utiliza para recuperar los archivos multimedia.
- `STATIC_ROOT`: Es la ruta absoluta. Esta variable se utiliza para recuperar los archivos estáticos.

### Modelo MVC y la creación de aplicaciones

- **M:** la porción de acceso a la base de datos.
- **V:** la porción que selecciona qué datos mostrar.
- **C:** la porción que delega a la vista dependiendo de la entrada del usuario.
