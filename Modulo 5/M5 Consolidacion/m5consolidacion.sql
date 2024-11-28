-- INSERTAR, MODIFICAR Y ELIMINAR UN CUSTOMER
-- INSERTAR
INSERT INTO customer
    (customer_id, store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active)
VALUES
    (600 , 3, 'Jose', 'Mendez', 'jose.mendez@sakilacustomer.org', 12, true, now(), null , 1 )
---------------

-- MODIFICAR
UPDATE customer 
SET last_name = 'Mendez', last_update = now()
WHERE customer_id = 600;
---------------

-- ELIMINAR
DELETE FROM customer
WHERE customer_id = 600;
----------------------------------------


-- INSERTAR, MODIFICAR Y ELIMINAR UN STAFF
-- INSERTAR
INSERT INTO staff
    (staff_id, first_name, last_name, address_id, email, store_id, active, username, password, last_update, picture)
VALUES
    (3, 'María', 'Gutierrez', 517, 'Maria.Gutierrez@sakilastaff.com', 1, true, 'Maria', '8cb2237d0679ca88db6464eac60da96345513964', now(), 'binary data' )
---------------

-- MODIFICAR
UPDATE staff 
SET address_id = 215, last_update = now()
WHERE staff_id = 3;
---------------

-- ELIMINAR
DELETE FROM staff
WHERE staff_id = 3;


-- INSERTAR, MODIFICAR Y ELIMINAR UN ACTOR
-- INSERTAR

INSERT INTO actor
    (actor_id, first_name, last_name,last_update)
VALUES
    (201, 'Johnny', 'Knoxville', now())
---------------

-- MODIFICAR
UPDATE actor 
SET first_name= 'Philip',last_name = 'Clapp', last_update = now()
WHERE actor_id = 201;
---------------

-- ELIMINAR
DELETE FROM actor
WHERE actor_id = 3;




------------------------------------------------------------------------------------
-- Listar todas las “rental” con los datos del “customer” dado un año y mes.

SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer, c.email, CONCAT(a.address,', ',a.district) AS address, a.phone, f.title AS movie, TO_CHAR (r.rental_date,'YYYY-MM') "month"
FROM rental r
    INNER JOIN customer c ON c.customer_id = r.customer_id
    INNER JOIN address a ON a.address_id = c.address_id
    INNER JOIN inventory i ON i.inventory_id=r.inventory_id
    INNER JOIN film f ON f.film_id = i.film_id
WHERE TO_CHAR(rental_date,'YYYY-MM') = '2005-08'




------------------------------------------------------------------------------------
-- Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”.

SELECT p.payment_id, TO_CHAR(p.payment_date, 'YYYY-MM-DD') AS payment_date, p.amount, f.title, CONCAT(c.first_name, ' ', c.last_name) AS customer
FROM payment p
    INNER JOIN customer c ON c.customer_id = p.customer_id
    INNER JOIN rental r ON r.rental_id = p.rental_id
    INNER JOIN inventory i ON i.inventory_id=r.inventory_id
    INNER JOIN film f ON f.film_id = i.film_id



------------------------------------------------------------------------------------
-- Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0.

SELECT *
FROM film
WHERE release_year= '2006' AND rental_rate > 4.0



------------------------------------------------------------------------------------
-- Realiza un Diccionario de datos que contenga el nombre de las tablas y columnas, si éstas pueden ser nulas, y su tipo de dato correspondiente.
SELECT table_name, column_name, is_nullable, data_type
from information_schema.columns
WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
ORDER BY table_name
