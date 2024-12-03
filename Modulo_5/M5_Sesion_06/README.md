# Modulo V - Sesión VI

## Agenda

- Relaciones

## Relaciones

### ¿Qué es una relación entre tablas?

Es una asociación establecida entre campos comunes, conocidos como columnas. Los campos que entran en relación pueden llamarse de manera distinta, pero tienen que ser del mismo tipo de dato.
Al realizar este tipo de acción entre tablas, podemos encontrar datos relacionados con ambas.

### Tipos de relaciones

- Relación uno a uno.
- Relación uno a varios.
- Relación varios a varios.

### Operaciones más comunes de relación entre 2 o más tablas

- Unión: **A U B**
  ```SQL
  SELECT c1, c2 FROM A
  UNION
  SELECT c1, c2 FROM B
  ```
- Intersección: **A ∩ B**
  ```SQL
  SELECT a1, a2, b1, b2
  FROM A
  INNER JOIN B ON a1 = b1
  ```
- Diferencia: **A - B**
  ```SQL
  SELECT a1, a2
  FROM A
  LEFT JOIN B ON a1 = b1
  WHERE b1 IS NULL
  ```
