# Modulo VII - Sesión VIII

## Agenda

- Consultas personalizadas
- Ejecutando SQL personalizado directamente
- Conexiones y cursores
- Invocación a procedimientos almacenados

## Consultas personalizadas

### Añadiendo anotaciones

- Pasando parámetros a raw():
  ```python
  Manager.raw(raw_query, params = None, translations = None)
  ```
- Si necesita realizar consultas parametrizadas, puede usar el argumento params para raw():
  ```python
  lname = 'Doe'
  Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
  ```
- Los parámetros no se pueden incluir entre comillas:
  ```python
    query = "SELECT \* FROM myapp_person WHERE last_name = '%s'"
  ```

## Ejecutando SQL personalizado directamente

A veces, incluso Manager.raw() no es suficiente: es posible que deba realizar consultas que no se asignen limpiamente a los modelos, o ejecutar directamente consultas UPDATE , INSERT o DELETE .
En estos casos, siempre se puede acceder directamente a la base de datos, enrutando por completo la capa del modelo.

Para protegerse contra la inyección de SQL, no debe incluir comillas alrededor de los marcadores de posición %s en la cadena de SQL.
Se debe tener en cuenta que si quieres incluir signos de porcentaje literal en la consulta, tienes que duplicarlos en caso de que estés pasando parámetros:

```python
cursor.execute("SELECT foo FROM bar WHERE baz = '30%'")

cursor.execute("SELECT foo FROM bar WHERE baz = '30%%' AND id = %s", [self.id])
```

Para usar la conexión de la base de datos, llame a connection.cursor() para obtener un objeto de cursor. Luego, llame a cursor.execute(sql, [params]) para ejecutar el SQL y cursor.fetchone() o cursor.fetchall() para devolver las filas resultantes.

```python
from django.db import connection

def my_custom_sql(self):
with connection.cursor() as cursor:
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor. fetchone()
return row
```

## Conexiones y cursores

Connection y el cursor implementan principalmente la API Python DB-API estándar descrita en PEP 249 , excepto cuando se trata del manejo de transacciones .

- Usando un cursor como gestor de contexto

```python
 with connection.cursor() ad c:
            c.execute(...)
```

- Es equivalente a:

  ```python
  c = connection.cursor()
            try:
                c.execute(...)
            finally:
                c.close()

  ```

## Invocación a procedimientos almacenados

CursorWrapper.callproc(procname, params=None, kparams=None) llama a un procedimiento almacenado de base de datos con el nombre dado.

```python
CREATE PROCEDURE "TEST_PROCEDURE" (v_i INTEGER, v_text NVARCHAR2(10)) AS
    p_i INTEGER;
    p_text NVARCHAR2(10);
BEGIN
    p_i:= v_i;
    p_text := v_text;
    ...
END;
```
