CREATE DATABASE Arriendopolis

CREATE TABLE Empresa
(
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(50),
    Direccion VARCHAR(100),
    Telefono VARCHAR(20),
    Correo VARCHAR(80),
    Web VARCHAR(150)
);

CREATE TABLE Herramienta
(
    idHerramienta NUMBER(12) PRIMARY KEY,
    Nombre VARCHAR(120),
    PrecioDia NUMBER(12)
);

CREATE TABLE Cliente
(
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Correo VARCHAR(80),
    Direccion VARCHAR(120),
    Celular VARCHAR(15)
);

CREATE TABLE Arriendo
(
    Folio NUMBER(12) PRIMARY KEY,
    Fecha DATE,
    Dias NUMBER(3),
    ValorDia NUMBER(12),
    Garantia VARCHAR(30),
    idHerramienta NUMBER(12),
    RUT VARCHAR(10),
    FOREIGN KEY (RUT) REFERENCES Cliente(RUT),
    FOREIGN KEY (idHerramienta) REFERENCES Herramienta(PK)
);
