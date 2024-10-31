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
SELECT p.nombre as titulo, p.estreno, p.director, r.nombre_actor as actor 
FROM peliculas p
INNER JOIN reparto r ON r.pelicula_id = p.pelicula_id
WHERE p.nombre = 'Titanic'

-- LISTAR TOP 10 DIRECTORES
SELECT director, count(nombre) AS total
FROM peliculas
GROUP BY director
ORDER BY (total) DESC

-- INDICAR CUANTOS ACTORES HAY
SELECT COUNT(DISTINCT nombre_actor) AS total_actores
FROM reparto

