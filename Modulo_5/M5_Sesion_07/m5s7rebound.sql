-- Listar los clientes sin ventas por medio de una subconsulta.
SELECT *
FROM venta
WHERE rut NOT IN (SELECT rut
FROM cliente)

-- Listar  todas  ventas  con  las  siguientes  columnas:  Folio,  Fecha,  Monto,  NombreCliente, RutCliente.
SELECT v.folio, v.fecha, v.monto, c.nombre, v.rut
FROM venta v
    INNER JOIN cliente c ON c.rut = v.rut

-- Clasificar los clientes 
SELECT TO_CHAR(v.fecha, 'YYYY') AS Periodo,
    c.nombre,
    CASE
        WHEN monto > 3000001 THEN 'Cliente Premium'
        WHEN monto > 1000001 THEN 'Cliente Gold'
        ELSE 'Cliente Standar'
    END AS Clasificacion
FROM venta v
    INNER JOIN cliente c ON c.rut = v.rut

-- Listar las ventas con la marca del vehículo más vendido.
SELECT *
FROM venta
WHERE idVehiculo = (SELECT idVehiculo
FROM venta
GROUP BY idVehiculo
ORDER BY COUNT(*) DESC LIMIT 1 );