-- Listar los clientes sin arriendos
SELECT *
FROM "Cliente" c
WHERE NOT EXISTS (
    SELECT *
FROM "Arriendo" a
WHERE a."Cliente_RUT" = c."RUT"
);


-- Listar  todos  los  arriendos  con  las  siguientes  columnas:  Folio,  Fecha,  Dias,  ValorDia, NombreCliente, RutCliente. 
SELECT a."Folio", a."Fecha", a."Dias", a."ValorDia", c."Nombre" AS nombre_cliente, c."RUT" AS rut_cliente
FROM "Arriendo" a
    INNER JOIN "Cliente" c ON a."Cliente_RUT" = c."RUT";


-- Clasificar los clientes
SELECT c.*,
    CASE 
        WHEN a.total_arriendos > 3 THEN 'Alto'
        WHEN a.total_arriendos BETWEEN 1 AND 3 THEN 'Medio'
        ELSE 'Bajo'
    END AS clasificacion
FROM "Cliente" c
    JOIN (
    SELECT "Cliente_RUT", COUNT(*) AS total_arriendos
    FROM "Arriendo"
    GROUP BY "Cliente_RUT"
) a ON c."RUT" = a."Cliente_RUT";

-- listar los clientes con el nombre de la herramienta más arrendada.
SELECT c.*, h."Nombre" AS herramienta_mas_arrendada
FROM "Cliente" c
    INNER JOIN (
    SELECT a."Cliente_RUT", h."Nombre", COUNT(*) AS total_arriendos
    FROM "Arriendo" a
        JOIN "Herramienta" h ON a."Herramienta_idHerramienta" = h."idHerramienta"
    GROUP BY a."Cliente_RUT", h."Nombre"
    ORDER BY a."Cliente_RUT", total_arriendos DESC
) h ON c."RUT" = h."Cliente_RUT"
GROUP BY c."RUT", h."Nombre"
HAVING COUNT(*) = 1;