SELECT vehiculo_id
FROM vehiculo
EXCEPT
SELECT vehiculo_id
FROM venta

-------------------------------------------------

SELECT v.folio "Folio", v.fecha "FechaVenta", v.monto "MontoVenta", c.nombre "NombreCliente", 
	c."RUT" "RutCliente", vh.patente "Patente", mc.nombre "NombreMarca", vh.modelo "Modelo"
FROM venta v
INNER JOIN cliente c on c."RUT" = v."RUT"
INNER JOIN vehiculo vh on vh.vehiculo_id = v.vehiculo_id
INNER JOIN marca mc on mc.marca_id = vh.marca_id
WHERE TO_CHAR (fecha ,'YYYY')= '2020'

-------------------------------------------------

SELECT TO_CHAR (fecha ,'YYYY-MM') "Mes", mc.nombre "NombreMarca", SUM(monto) "Total"
FROM venta v
INNER JOIN vehiculo vh on vh.vehiculo_id = v.vehiculo_id
INNER JOIN marca mc on mc.marca_id = vh.marca_id
WHERE TO_CHAR (fecha ,'YYYY')= '2020'
GROUP BY TO_CHAR (fecha ,'YYYY-MM'), "NombreMarca"

-------------------------------------------------

SELECT "RUT" "RUT" , nombre "Nombre"
FROM empresa 
UNION
SELECT "RUT", nombre
FROM cliente 
