CREATE TABLE gatos(
	color varchar(30)
);

ALTER TABLE gatos
ADD COLUMN idGato serial NOT NULL

ALTER TABLE gatos
ADD CONSTRAINT pk_idGato PRIMARY KEY (idGato)

CREATE TABLE mascotas(
	idMascota serial PRIMARY KEY NOT NULL,
	name varchar(50)
);

ALTER TABLE mascotas
ADD COLUMN idGato int NOT NULL;

ALTER TABLE mascotas
ADD CONSTRAINT fk_gatos_mascotas FOREIGN KEY (idGato)
REFERENCES gatos (idGato);