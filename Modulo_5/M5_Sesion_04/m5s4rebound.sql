CREATE DATABASE Empresa;

CREATE TABLE Departamentos(
	departamento_id INT PRIMARY KEY,
	nombre VARCHAR(100),
	ubicacion VARCHAR(100)
);

CREATE TABLE Empleados(
	empleado_id INT PRIMARY KEY,
	nombre VARCHAR(100),
	puesto VARCHAR(100),
	salario DECIMAL(10,2),
	fecha_contratacion DATE,
	departamento_id INT,
	FOREIGN KEY (departamento_id) REFERENCES Departamentos(departamento_id)
);

ALTER TABLE Empleados
ADD correo_electronico VARCHAR(100);


ALTER TABLE Empleados
RENAME TO Trabajadores;

DROP TABLE Departamentos;