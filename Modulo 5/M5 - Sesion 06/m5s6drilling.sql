SELECT a."Folio", a."Fecha", a."Dias", a."ValorDia", c."Nombre" NombreCliente, c."RUT" RutCliente
FROM "Arriendo"  as a
    INNER JOIN "Herramienta" as h ON h."idHerramienta" = a."Herramienta_idHerramienta"
    INNER JOIN "Cliente" as c ON c."RUT" = a."Cliente_RUT"

------------------------------------------------------------------------------

    SELECT "RUT"
    FROM "Cliente"
EXCEPT
    SELECT "Cliente_RUT"
    FROM "Arriendo"

------------------------------------------------------------------------------

    SELECT "RUT" , "Nombre"
    FROM "Empresa"
UNION
    SELECT "RUT", "Nombre"
    FROM "Cliente"

------------------------------------------------------------------------------

SELECT TO_CHAR ("Fecha" ,'YYYY-MM') "Mes", COUNT("Folio") "Total"
FROM "Arriendo"
GROUP BY TO_CHAR ("Fecha" ,'YYYY-MM')