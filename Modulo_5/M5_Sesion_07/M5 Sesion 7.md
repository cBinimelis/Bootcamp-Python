# Modulo V - Sesión VII

## Agenda

- SQL Avanzado

## SQL Avanzado

### Subconsultas

Las subconsultas son consultas que aparecen dentro de otra consulta. Éstas aumentan notablemente la potencia del lenguaje SQL.

```SQL
SELECT columna1, columna2
FROM tabla1
WHERE columna1 IN (SELECT columnaX FROM tabla2 WHERE condicion);
```

### JOIN

Los JOINs son una función que permite combinar filas de dos o más tablas basándose en una condición relacionada entre ellos. Los JOINs se utilizan fundamentalmente para consultas datos de múltiples tablas en una sola consulta.
Los tipos de JOINs son:

- **INNER JOIN:** Retorna registros que tienen valores coincidentes en ambas tablas
- **RIGHT JOIN:** Retorna todos los registros de la tabla de la derecha (tabla 2) y los registros coincidentes de la tabla de la izquierda (tabla 1). Si no hay coincidencias, los valores de la tabla de la izquierda serán NULL.
- **FULL JOIN:** Retorna todos los registros cuando hay una coincidencia en cualquiera de las tablas. Si no hay coincidencias, los valores de la tabla que no tienen coincidencias serán NULL.
- **CROSS JOIN:** Retorna el producto cartesianod e las tablas involucradas, es decir, todas las combinaciones de filas de ambas tablas.

### Consultas complejas

Algunas consultas presentan todo un desafío, desde el punto de vista y complejidad para entender el código SQL que se genera.
Para poder comprenderlas, éstas deben ir implementandose por partes, hasta llegar a la solución de lo que se requiere.

```SQL
SELECT c.nombre AS cliente,
       p.nombre AS producto,
       dp.cantidad,
       p.precio_unitario * dp.cantidad AS total
FROM clientes c
JOIN pedidos pd ON c.id_cliente = pd.id_cliente
JOIN detalles_pedido dp ON pd.id_pedido = dp.id_pedido
JOIN productos p ON dp.id_producto = p.id_producto
WHERE pd.fecha_pedido BETWEEN '2024-01-01' AND '2024-03-31'
ORDER BY total DESC;
```
