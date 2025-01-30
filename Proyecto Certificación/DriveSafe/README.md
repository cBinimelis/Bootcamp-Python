# DriveSafe

## Instalación

1. Configurar entorno virtual con `python -m venv venv`
2. En caso de que pycharm/vscode no lo realice automáticamente, activar el entorno virtual con `venv/Scripts/activate`
3. Instalar dependencias con el comando `pip install -r requirements.txt`
4. Configurar el archivo `settings.py` y Postgres con la una base de datos acorde a la configuración
   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "drive_safe",
           "USER": "tu_usuario_db",
           "PASSWORD": "tu_contraseña_db",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }
   ```
5. Ejecutar las migraciones con `python manage.py migrate`
6. Configura a tu superuser con el comando `python manage.py createsuperuser`
