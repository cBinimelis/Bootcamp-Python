-- INSERTE DATOS DE UNA EMPRESA
INSERT INTO "Empresa"
    ("RUT", "Nombre", "Direccion", "Telefono", "Correo", "Web")
VALUES
    (
        '99222333-4',
        'Ferretería y Herramientas Chasquilla S.A.',
        'Av. Las Tuercas 5439',
        '043215899',
        'ferreteria_chasquill@maestro.com',
        'maestro.com/chasquilla'
);

-- INSERTE 5 HERRAMIENTAS
INSERT INTO "Herramienta"
    ("idHerramienta", "Nombre", "PrecioDia")
VALUES
    ('1', 'Taladro', 16990),
    ('2', 'Pistola de Clavos', 18990),
    ('3', 'Soldadora', 36990),
    ('4', 'Martillo Hidraulico', 79990),
    ('5', 'Sierra Eléctrica', 19990);

-- INSERTE 3 CLIENTES (2 EXTRA AÑADIDOS)
INSERT INTO "Cliente"
    ("RUT", "Nombre", "Correo", "Direccion", "Celular")
VALUES
    ('19789852-4', 'José Carcamo Gomez', 'jcarcamo@maestro.com', 'Los Clavos #98', '988997744'),
    ('15999888-5', 'Martín Jiménez Morales', 'mjimenez@maestro.com', 'Psje El Perno #598', '955664411' ),
    ('18666111-3', 'Daniela Rojas Herrera', 'drojas@maestro.com', 'Las Rejas #5, Interior', '933222158'),
    ('13999852-1', 'Emilio Romero Vargas', 'evargas@maestro.com', 'Av La Sierra #3549', '945659782'),
    ('11669771-2', 'Mariana Castro Ortiz', 'mcastro@maestro.com', 'Psje Pino Oregon Cepillado Seco #45', '985664433');

-- ELIMINA El ÚLTIMO CLIENTE
DELETE FROM "Cliente"
WHERE 'Rut' = '11669771-2';

-- ELIMINA LA PRIMERA HERRAMIENTA
DELETE FROM "Herramienta"
WHERE 'idHerramienta' = '1';

-- INSERTE 2 ARRIENDOS PARA CADA CLIENTE
INSERT INTO "Arriendo"
    ("Folio", "Fecha", "Dias", "ValorDia", "Garantia", "Herramienta_idHerramienta", "Cliente_RUT")
VALUES
    (45251, '2024-10-25', 15, 36990, '30 Días, Accidente, Pérdida', '3', '13999852-1'),
    (45252, '2024-10-25', 15, 16990, '30 Días, Accidente, Pérdida', '1', '13999852-1'),
    (45106, '2024-09-12', 29, 79990, '30 Días, Accidente, Pérdida', '4', '15999888-5'),
    (45107, '2024-09-12', 29, 36990, '30 Días, Accidente, Pérdida', '3', '15999888-5'),
    (45192, '2024-09-27', 1, 16990, '5 Días, Accidente, Pérdida', '1', '19789852-4'),
    (45201, '2024-09-29', 1, 18990, '5 Días, Accidente, Pérdida', '2', '19789852-4'),
    (45209, '2024-09-29', 2, 16990, '5 Días, Accidente, Pérdida', '1', '18666111-3'),
    (45210, '2024-09-29', 2, 36990, '5 Días, Accidente, Pérdida', '3', '18666111-3');


-- MODIFIQUE EL CORREO ELECTRÓNICO DEL PRIMER CLIENTE
UPDATE "Cliente"
SET "Correo" = 'jocarcamo@maestro.com'
WHERE "RUT" = '19789852-4';

-- LISTE TODAS LAS HERRAMIENTAS
SELECT *
FROM "Herramienta";

-- LISTE LOS ARRIENDOS DEL SEGUNDO CLIENTE
SELECT *
FROM "Arriendo"
WHERE "Cliente_RUT" = '15999888-5';

--LISTE LOS CLIENTES CURO NOMBRE CONTENGA UNA A
SELECT *
FROM "Cliente"
WHERE "Nombre" LIKE '%A%' OR "Nombre" LIKE '%a%';;

-- OBTENGA EL NOMBRE DE LA SEGUNDA HERRAMIENTA INSERTADA
SELECT "Nombre"
FROM "Herramienta"
LIMIT 1 OFFSET 1

-- MODIFIQUE LOS PRIMEROS 2 ARRIENDOS INSERTADOS CON FECHA 15/01/2020
UPDATE "Arriendo"
SET "Fecha" = '15/01/2020'
WHERE "Folio" IN (SELECT "Folio" FROM "Arriendo" LIMIT 2)

-- LISTE FOLIO, FECHA Y VALOR DIA DE LOS ARRIENDOS DE ENERO DEL 2020
SELECT "Folio", "Fecha", "ValorDia" FROM
"Arriendo"
WHERE "Fecha" BETWEEN '01/01/2020' AND '31/01/2020'