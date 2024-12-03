# Modulo V - Sesión III

## Agenda

- Tipos de Datos
- Álgebra Relacional
- Funciones
- Claves Primarias y Foráneas

## Tipos de Datos

Una de las principales características del trabajo con bases de SQL - PK y FK datos, es la necesidad de declarar los distintos tipos de datos existentes en cada campo a completar. Estos aplican restricciones sobre lo que puede ingresar a los registros. No podemos ingresar caracteres cuando piden un número, ni sobrepasar el límite de caracteres posibles.

- **INT:** Números enteros de 4 bytes que pueden tomar valor desde -2147483648 hasta 2147483647.
- **NUMERIC(P,S):** Número exacto de precisión indicada, este tipo es particularmente recomendable para los valores monetarios o todos los tipos numéricos donde la parte flotante no deba variar, las indicaciones se corresponden con el número total de dígitos (p) después de la parte decimal(s).
- **CHAR(S):** Cadena de hasta 2000 bytes de longitud fija.
- **VARCHAR(S):** Cadena de hasta 4000 bytes de longitud variable. A diferencia de `char`, si no se ocupa toda la memoria, esta queda libre, `char` ocupará toda la memoria solicitada.
- **DATE:** Almacena una fecha según el formato definido en los parámetros de la base de datos. PAra consultar en detalle los tipos de datos, podemos ir a la documentación de PostgreSQL.

## Algebra relacional

El álgebra relacional es un conjunto de operaciones que describen paso a paso cómo computar una respuesta sobre las relaciones, tal y como éstas son definidas en el modelo relacional.

Denominada de tipo procedimental, a diferencia del cálculo relacional que es de tipo declarativo.

- INNER JOIN:
  ```SQL
  SELECT *
  FROM A
  INNER JOIN B ON A.key = B.key
  ```
- LEFT JOIN
  ```SQL
  SELECT *
  FROM A
  LEFT JOIN B ON A.key = B.key
  ```
- LEFT JOIN
  ```SQL
  SELECT *
  FROM A
  LEFT JOIN B ON A.key = B.key
  WHERE B.key IS NULL
  ```
- RIGHT JOIN
  ```SQL
  SELECT *
  FROM A
  RIGHT JOIN B ON A.key = B.key
  ```
- RIGHT JOIN
  ```SQL
  SELECT *
  FROM A
  RIGHT JOIN B ON A.key = B.key
  WHERE A.key IS NULL
  ```
- FULL JOIN
  ```SQL
  SELECT *
  FROM A
  FULL JOIN B ON A.key = B.key
  ```
- FULL JOIN
  ```SQL
  SELECT *
  FROM A
  FULL JOIN B ON A.key = B.key
  WHERE A.key IS NULL
  ```

## Funciones

El lenguaje SQL tiene funciones incorporadas para hacer cálculos sobre los datos. Existen muchas más, que dependen del sistema de bases de datos que se utilice

- **AVG():** El promedio de los valores.
- **COUNT():** El número de filas.
- **MAX():** El valor más grande.
- **MIN():** El valor más pequeño.
- **SUM():** La suma de los valores.

## Claves primarias y foráneas

De manera adicional a las filas y columnas, las tablas también cuentan con claves primarias y foráneas. Estas buscan generar identificadores para cada registro de estas tablas mediante algún valor específico de una columna o atributo.

- **Clave Primaria (Primary Key):** Cuando hacemos referencia a esta columna dentro de su tabla de origen, hablaremos de una clave primaria. Esta clave siempre será de **carácter único.**
- **Clave foránea (Foreign Key):** Cuando hacemos referencia a una columna identificadora en otra tabla a la cual hacemos **referencia**, hablamos de una clave foránea.
