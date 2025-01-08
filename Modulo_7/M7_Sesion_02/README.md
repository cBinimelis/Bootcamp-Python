# Modulo VI - Sesión II

## Agenda

- Paquetes de instalación de Bases de Datos
- Django Como ORM

## Paquetes de instalación de Bases de Datos

- **Database Python package:** `pip installation syntax`. PIP es un administrador de paquetes para paquetes o módulos de Python.
- **PostgreSQL psycopgX:** `pip install psycopgX`. X se refiere a la versión, actualmente se encuentra disponible 1, 2 ó 3, el cual dependerá de las versiones que se estén trabajando en el proyecto y su compatibilidad.
- **MySQL mysql-python:** `pip install mysql-python`
- **Oracle cx Oracle:** `pip install cx Oracle`

## Django Como ORM

El ORM de Django es una implementación del concepto de mapeo de objeto relacional (ORM). Esta siempre será la primera migración que realizaremos. `pyhton manage.py migrate`

Otros comandos son:

- `migrate` responsable de aplicar y no aplicar las migraciones.
- `makemigrations` responsable de crear nuevas migraciones basadas en los cambios que se han realizado en el modelo. Este comando empaqueta los cambios del modelo en archivos de migración individuales, análogos a los commit.
- `sqlmigrate` muestra las instrucciones SQL para una migración.
- `showmigrations` enumera las migraciones de un proyecto y su estado.

## Sintaxis de consultas en ORM

El ORM de Django nos proporciona dos métodos para filtar los querysets: filter y exclude. También podemos acceder a un único registro utilizando el método get.

El método _filter_ se utiliza para filtrar un conjunto de datos y devuelve un Queryset que cumple con las condiciones indicadas.

```python
Person.objects.filter(country_iso='CANADA')
```

El método _exclude_ tiene un comportamiento muy similar al método filter. También devuelve un Queryset filtrado.

```python
Person.objects.exclude(country_iso='CANADA')
```

Se puede utilizar estos métodos en una misma sentencia, por ejemplo, recuperar todos los usuarios que se dieron de alta un día y proporcionaron su email.

```python
Person.objects.filter(created_at=datetime(2022,7,18)).exclude(email="")
```

El método get devuelve un objeto que cumpla las condiciones indicadas.

```python
Person.objects.get(passport="12345678A")
```

Si los filtros añadidos no encuentran ningún resultado, se mostrará una excepción de tipo **Model.DoesNotExist** y si se encuentran múltiples resultados la excepción será **Model.MultipleObjectsReturned**.
