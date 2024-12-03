# Modulo V - Sesión IV

## Agenda

- Sentencias DDL a partir del modelo físico

## Sentencias DDL a partir del modelo físico

### Lenguaje SQL

Todos los principales SGBDR (Sistema Gestor de Bases de Datos Relacionales) incorporan un motor SQL (Structured Query Language) en el Servidor de Base de Datos, así como herramientas de cliente que permiten enviar comandos SQL para que sean procesadas por el motor del servidor. De esta forma, todas las tareas de gestión de la Base de Datos (BD) pueden realizarse utilizando sentencias SQL.

### Sentencias DDL

El DDL es la parte del lenguaje SQL que realiza la función de definición de datos del SGBD. Fundamentalmente, se encarga de la creación, modificación y eliminación de los objetos de la base de datos (es decir de los metadatos). Por supuesto es el encargado de la creación de las tablas.

- **CREATE:** Este comando crea una base de datos con el nombre que se indique. También permite crear tablas al añadir la palabra clave _"table"_.
  `CREATE DATABASE prueba;`
- **DROP:** La orden _DROP TABLE_ seguida del nombre de una tabla, permite eliminar la tabla en cuestión.
  `DROP TABLE prueba;`
- **TRUNCATE:** Este comando solo aplica a tablas y su función es borrar el contenido completo de la tabla especificada.
  `TRUNCATE TABLE alumno;`
- **ALTER:** Permite modificar la estructura de una tabla u objeto.
  `ALTER TABLE alumno ADD edad INT;`

### Sentencias DML

Es un lenguaje proporcionado por los sistemas gestores de bases de datos que permite a los usuarios de la misma llevar a cabo las tareas de consulta o modificación de los datos contenidos en las Bases de Datos del SGBD.

- **SELECT:** Utilizado para consultar registros que satisfagan un criterio determinado. La sintáxis fundamental es la siguiente:
  `SELECT columna FROM tabla;`
- **INSERT:** Este comando añade datos a una tabla. Su sintaxis fundamental es:
  `INSERT INTO usuario (nombre, apellidos, edad, carrera) VALUES ("Martin", "Bastida Godínez", "23", "Ingeniería en TI");`
- **DELETE:** Elimina los registros de la tabla que cumplan con la condición indicada.
  `DELETE registro FROM tabla WHERE [CONDICIÓN];`
- **UPDATE:** Añadir datos a una tabla se realiza mediante la instrucción UPDATE. Su sintaxis fundamental es:
  `UPDATE tabla SET columna1=valor1 WHERE [CONDICIÓN];`
