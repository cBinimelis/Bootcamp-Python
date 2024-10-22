SELECT customer_id, company_name, phone
FROM customers

SELECT 	product_id, product_name, unit_price, units_in_stock
FROM products
WHERE units_in_stock > 50 OR unit_price > 100
ORDER BY unit_price DESC, units_in_stock DESC

select *
FROM customers
WHERE region IS null AND city = 'México D.F.'

SELECT 	*
FROM products
WHERE units_in_stock > 50 OR unit_price > 100

SELECT p.product_name, c.category_name 
FROM products AS p
INNER JOIN categories AS c ON p.category_id = c.category_id

SELECT t.territory_description, r.region_description
FROM territories AS t
INNER JOIN region AS r ON t.region_id = r.region_id
WHERE r.region_description = 'Northern'

SELECT e.employee_id, e.first_name,e.last_name, 
t.territory_description,r.region_description
FROM territories AS t
INNER JOIN region AS r ON r.region_id = r.region_id
INNER JOIN employee_territories AS et ON et.territory_id = t.territory_id
INNER JOIN employees AS e ON e.employee_id = et.employee_id

-- LISTADO DE ORDENES CON SUS PRODUCTOS, CATEGORIAS, PROVEEDORES Y QUIEN DESPACHO

SELECT 

