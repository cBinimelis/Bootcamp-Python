CREATE DATABASE CredAuto

CREATE TABLE Empresa
(
    RUT VARCHAR(10) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(120) NOT NULL,
    Direccion VARCHAR(120) NOT NULL,
    Telefono VARCHAR(15) NOT NULL,
    Correo VARCHAR(80) NOT NULL,
    Web VARCHAR(50) NOT NULL
)

CREATE TABLE Cliente
(
    RUT VARCHAR(10) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(120) NOT NULL,
    Correo VARCHAR(80) NOT NULL,
    Direccion VARCHAR(120) NOT NULL,
    Celular VARCHAR(15) NOT NULL,
    Alta CHAR(1)
)

CREATE TABLE Marca
(
    idMarca NUMBER(12) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(120)
)

CREATE TABLE TipoVehiculo
(
    idTipoVehiculo NUMBER(12) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(120)
)


CREATE TABLE Venta
(
    Folio NUMBER(12) PRIMARY KEY NOT NULL,
    Fecha DATE,
    Monto NUMBER(12),
    idVehiculo NUMBER(12) UNIQUE,
    RUT VARCHAR(19),
    FOREIGN KEY (RUT) REFERENCES Cliente(RUT)
)

CREATE TABLE Vehiculo
(
    idVehiculo NUMBER(12) PRIMARY KEY NOT NULL,
    Patente VARCHAR(10),
    Marca VARCHAR(20),
    Modelo VARCHAR(20),
    Color VARCHAR(15),
    Precio NUMBER(12),
    FrecuenciaMantencion NUMBER(5),
    idMarca NUMBER(12),
    idTipoVehiculo NUMBER(12),
    FOREIGN KEY (idMarca) REFERENCES Marca(idMarca),
    FOREIGN KEY (idTipoVehiculo) REFERENCES TipoVehiculo(idTipoVehiculo)
)

ALTER TABLE Venta
ADD CONSTRAINT venta_vehiculo
FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo)

CREATE TABLE Mantencion
(
    idMantencion NUMBER(12) PRIMARY KEY NOT NULL,
    Fecha DATE,
    TrabajoRealizado VARCHAR2(2000),
    Folio NUMBER(12),
    FOREIGN KEY (folio) REFERENCES Venta(folio)
)