-- CREAR TABLA EDITORIALES
CREATE TABLE editoriales (
    codigo_editorial SERIAL PRIMARY KEY,
    nombre VARCHAR(80)
);

-- CREAR TABLA LIBROS
CREATE TABLE libros (
    codigo_libro SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    codigo_editorial INTEGER,
    FOREIGN KEY (codigo_editorial) REFERENCES editoriales(codigo_editorial)
)

-- INSERTAR EDITORIALES Y LIBROS
INSERT INTO editoriales (nombre) VALUES ('Anaya');
INSERT INTO editoriales (nombre) VALUES ('Andina');
INSERT INTO editoriales (nombre) VALUES ('S.M.');

INSERT INTO libros (titulo, codigo_editorial) VALUES ('Don Quijote de La Mancha I', 1);
INSERT INTO libros (titulo, codigo_editorial) VALUES ('El principito', 2);
INSERT INTO libros (titulo, codigo_editorial) VALUES ('El príncipe', 3);
INSERT INTO libros (titulo, codigo_editorial) VALUES ('Diplomacia', 3);
INSERT INTO libros (titulo, codigo_editorial) VALUES ('Don Quijote de La Mancha II', 1);

-- MODIFICAR LA TABLA LIBROS
ALTER TABLE libros
ADD autor VARCHAR(50),
ADD precio INTEGER

-- AGREGAR AUTOR Y PRECIO A LOS LIBROS YA INGRESADOS
UPDATE libros SET autor = 'Miguel de Cervantes', precio = 150 WHERE codigo_libro = 1;
UPDATE libros SET autor = 'Antoine SaintExupery', precio = 120 WHERE codigo_libro = 2;
UPDATE libros SET autor = 'Maquiavelo', precio = 180 WHERE codigo_libro = 3;
UPDATE libros SET autor = 'Henry Kissinger', precio = 170 WHERE codigo_libro = 4;
UPDATE libros SET autor = 'Miguel de Cervantes', precio = 140 WHERE codigo_libro = 5;

-- INSERTAR 2 NUEVOS LIBROS
INSERT INTO libros (titulo, codigo_editorial, autor, precio) VALUES ('Gatos Guerreros', 2, 'Erin Hunter', 110);
INSERT INTO libros (titulo, codigo_editorial, autor, precio) VALUES ('El café de los corazones rotos', 2, 'Penelope J. Stokes', 230);

-- ELIMINAR LIBROS SOLO EN MEMORIA
BEGIN; 
DELETE FROM libros WHERE codigo_editorial = 1;
ROLLBACK;

-- ACTUALIZAR NOMBRES DE EDITORIALES
BEGIN;

SAVEPOINT actualizar_andina;
UPDATE editoriales SET nombre = 'Iberlibro' WHERE codigo_editorial = 2;
ROLLBACK TO actualizar_andina;

UPDATE editoriales SET nombre = 'Mountain' WHERE codigo_editorial = 3;
COMMIT;