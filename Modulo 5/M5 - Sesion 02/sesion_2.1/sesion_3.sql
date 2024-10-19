CREATE TABLE animals(
	id serial PRIMARY KEY,
	name varchar(50),
	register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE departamentos(
id serial PRIMARY KEY,
name varchar(30)
)

CREATE TABLE docentes(
	id serial PRIMARY KEY,
	departamento_id int NOT NULL,
	name varchar(50),
	FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

ALTER TABLE animals
ADD COLUMN birth_day date NOT NULL;

ALTER TABLE docentes
ADD COLUMN last_name varchar(50);

ALTER TABLE alumnos 
ALTER COLUMN rut SET DATA TYPE char(12);

ALTER TABLE docentes
RENAME COLUMN name TO first_name;

ALTER TABLE animals
DROP COLUMN register_date;

ALTER TABLE alumnos
ADD COLUMN email varchar(150);

ALTER TABLE alumnos
ADD CONSTRAINT unique_email UNIQUE(email);

