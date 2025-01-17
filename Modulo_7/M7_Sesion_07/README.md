# Modulo VII - Sesión VI

## Agenda

- Consultas

## Ejecutando sentencias de recuperación con ORM

Una de las características más poderosas de Django es su Mapeador Relacional de Objetos (ORM), que le permite interactuar con su base de datos, como lo haría con instrucciones SQL (Structured Query Language).

### Recuperando registros

Para recuperar objetos de la base de datos, construimos un QuerySet o sea una consulta a través de una clase Manager.
Los Managers son accesibles únicamente a través de las clases del modelo, en vez que desde una instancia, para aplicar una separación entre las operaciones a “nivel de tabla” y las operaciones “A nivel de registro”.
El Manager es la principal fuente de QuerySets de un modelo.

### Recuperando todos los registros del modelo

Solo tenemos que usar el método all() de nuestro modelo:

```python
from contabilidad.models import Cliente, Factura

clientes = Cliente.objects.all()
for cliente in clientes:
    print(f"Nombre: {cliente.nombre}, Apellidos:_ {cliente.apellidos}")
```

En el caso de los modelos con relaciones, también podemos accesar a los datos del modelo relacionado, usando el nombre del campo que tiene la relación, seguido de un doble guión bajo (\_\_) y por último el campo del otro modelo:

```python
from contabilidad.models import Cliente, Factura
facturas = Factura.objects.all()
for factura in facturas:
    print(f"Pagada: {factura.pagada}, Importe: {factura.importe}, RFC Cliente: {factura.cliente__rfd}")
```

### Aplicando filtros en recuperación de registros

Podemos usar el método filter() como un símil del WHERE de SQL, y así obtener un conjunto de datos limitado por condiciones.

Cuando tenemos modelos con relaciones el procedimiento es muy similar, solo tenemos que usar ** para accesar al modelo referenciado, y si queremos usar un modificador usamos el sufijo **modificador.

## Sentencias SQL

Podemos realizar consultas en bruto con el método de administrador raw()

```python
Manager.raw(raw_query, params = (), translations = None)
```

Se puede entonces ejecutar un SQL personalizado como este:

```bash
>>> for p in Person.objects.raw('SELECT * FROM myapp_person'):
    ... print(p)
    John Smith
    Jane Jones
```

### Mapeando campos de consultas al modelo

- raw() asigna automáticamente campos en la consulta a campos en el modelo.

```python
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
```

### Búsquedas de índice

- raw() admite indexación, por lo que si solo necesita el primer resultado, puede escribir:

```python
first_person = Person.objects.raw('SELECT * FROM myapp_person')[0]
```
