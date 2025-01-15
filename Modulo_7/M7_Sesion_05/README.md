# Modulo VII - Sesión V

## Agenda

- Relaciones

## Qué son las Relaciones en el ORM de Django

El ORM de Django es una implementación del concepto de mapeo de objeto relacional (ORM).

Las relaciones en el ORM de Django tiene 3 tipos de campo para establecerlas entre los modelos (Tablas):

- El campo `ForeignKey` se utiliza para establecer una relación de 1 registro a varios registros.
- El campo `OneToOneField` se utiliza para relacionar registros uno a uno.
- El campo `ManyToManyField` para relacionar varios registros entre sí, creando una nueva tabla que contiene los IDs de los modelos.

### Relaciones Muchos a Uno

Significa que un registro de la tabla A puede tener muchos registros coincidentes en la tabla B, pero un registro de la tabla B sólo tiene un registro coincidente en la tabla A.
La relación se utiliza con frecuencia para describir clasificaciones o agrupaciones.

Veamos el siguiente código:

```python
class Number(models.Model):
    number = models.CharField(max_length = 10)

class Person(models.Model):
    name = models.CharField(max_length = 200)

class PersonNumber(models.Model):
    person = models.ForeingKey(Person, on_delete = models.CASCADE, related_name = "numbers")
    number = models.ForeingKey(Number, on_delete = models.CASCADE, related_name = "person")
```

### Relaciones Muchos a Muchos

Una relación de muchos a muchos se produce cuando varios registros de una tabla se asocian a varios registros de otra tabla. Se puede dividir la relación de muchos a muchos en dos relaciones de uno a muchos mediante el uso de una tercera tabla denominada tabla de unión.

```python
from django.db import models

class Publicacion(models.Model):
    title = models.CharField(max_length = 30)

    class Meta:
        ordering = ['title']

    def__str__(self):
        return self.title

class Articulo(models.Model):
    headline = models.CharField(max_length = 100)
    publicaciones = models.ManytoManyField(Publication)

    class Meta:
        ordering = ['headline']

    def__str__(self):
        return self.headline
```

Las tablas de unión o intermedias pueden acceder a los campos y los datos entre tablas sin necesidad de crear una relación diferente.

### Relaciones Uno a Uno

Una Relación uno a uno es un vínculo entre la información de dos tablas, donde cada registro en cada tabla solo aparece una vez.
Para definir una relación uno a uno, use OneToOneField como se muestra a continuación:

```python
from django.db import models

class Engine(models.Model):
    name = models.CharField(max_length = 25)

    def__unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length = 25)
    engine = models.OneToOneField(Engine)

    def__unicode__(self)
        return self.name
```
