-- CREAR BASE DE DATOS
CREATE DATABASE peliculas;

-- CREAR TABLAS EN BASE A LOS ARCHIVOS
CREATE TABLE peliculas (
	pelicula_id INTEGER PRIMARY KEY,
	nombre VARCHAR(120),
	estreno INTEGER, 
	director VARCHAR(100)
);

CREATE TABLE reparto (
	pelicula_id INTEGER,
	nombre_actor VARCHAR(120),
	FOREIGN KEY (pelicula_id) REFERENCES peliculas(pelicula_id)
);

-- POBLAR LAS TABLAS DESDE LOS ARCHIVOS
COPY peliculas FROM 'peliculas.csv' WITH CSV;
COPY reparto FROM 'reparto.csv' WITH CSV;

-- LISTAR ACTORES DE TITANIC
SELECT p.nombre AS titulo, p.estreno, p.director, r.nombre_actor AS actor 
FROM peliculas p
INNER JOIN reparto r ON r.pelicula_id = p.pelicula_id
WHERE p.nombre = 'Titanic'

-- LISTAR TOP 10 DIRECTORES
SELECT director, COUNT(nombre) AS total
FROM peliculas
GROUP BY director
ORDER BY (total) DESC

-- INDICAR CUANTOS ACTORES HAY
SELECT COUNT(DISTINCT nombre_actor) AS total_actores
FROM reparto

-- PELICULAS ENTRE 1990 Y 1999
SELECT * 
FROM peliculas 
WHERE estreno BETWEEN 1990 AND 1999
ORDER BY nombre

-- LISTAR ACTORES DE LA PELICULA MÁS NUEVA
SELECT *
FROM reparto r
INNER JOIN peliculas p ON p.pelicula_id = r.pelicula_id
WHERE p.pelicula_id = (
	SELECT pelicula_id FROM peliculas 
	ORDER BY estreno DESC LIMIT 1);

-- ACTUALIZAR DIRECTOR SOLO EN MEMORIA
BEGIN;
	UPDATE peliculas SET director = 'Quentin Tarantino' WHERE pelicula_id = 87;
	UPDATE peliculas SET director = 'Valentin Trujillo' WHERE pelicula_id = 45;
	UPDATE peliculas SET director = 'Ari Aster' WHERE pelicula_id = 13;
	UPDATE peliculas SET director = 'Jordan Peele' WHERE pelicula_id = 61;
	UPDATE peliculas SET director = 'Darren Aronofsky' WHERE pelicula_id = 22;
ROLLBACK;

-- INSERTE 3 ACTORES A LA PELICULA RAMBO
SAVEPOINT add_to_rambo;
	INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (72, 'Richard Crenna');
	INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (72, 'John McLiam');
	INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (72, 'Patrick Stack');
COMMIT;

-- ELIMINA LAS PELICULAS DE 2008 SOLO EN MEMORIA
BEGIN;
	DELETE FROM peliculas WHERE estreno = 2008;
ROLLBACK;

-- INSERTAR 2 ACTORES PARA CADA PELICULA DEL 2001
-- LOTR:FOTR
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (13, 'Sala Baker');
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (13, 'Brent McIntyre');

-- MONSTERS INC.
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (16, 'Billy Crystal');
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (16, 'John Goodman');

-- EL VIAJE DE CHIHIRO
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (55, 'Rumi Hiiragi');
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (55, 'Miyu Irino');

-- AMELIE
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (78, 'André Dussollier');
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (78, 'Flora Guiet');

-- OCEAN'S ELEVEN
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (94, 'Bernie Mac');
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (94, 'Qin Shaobo');

-- MOULIN ROUGE
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (99, 'Matthew Whittet');
INSERT INTO reparto (pelicula_id, nombre_actor) VALUES (99, 'Tara Morice');

-- CAMBIAR NOMBRE DE 'KING KONG' A 'DONKEY KONG'
BEGIN;
	UPDATE peliculas SET nombre = 'Donkey Kong' WHERE pelicula_id = 57
ROLLBACK;