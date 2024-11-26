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