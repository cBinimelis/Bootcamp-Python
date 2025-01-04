# Modulo VI - Sesión X

## Agenda

- El sitio administrativo de Django I

## El sitio administrativo de Django I

### Utilizando manage.py

`manage.py` es un script que se genera automáticamente al crear un proyecto de Django, y se utiliza para administrar dicho proyecto. Debe ejecutarse mediante comandos de python y acepta los comandos integrados proporcionados por Django, tales como:

- Check
- Dbshell
- Diffsettings
- Flush
- Makemigrations
- Migrate
- Runserver
- Shell
- Starapp
- Starproject
- Test

### Crear un super usuario

```shell
python manage.py createsuperuser --username admin --email admin@mail.com
```

### Limitando el acceso al sitio administrativo

```python
urlpatterns =[
  path('my-secret-admin/', admin.site.urls),
]
```

### Conociendo el sitio de administración de Django

Para acceder al sitio administrativo de Django se logra a través de la URL configurada para /admin y las credenciales del super usuario creado.
