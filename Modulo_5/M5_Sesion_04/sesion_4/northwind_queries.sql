SELECT customer_id, company_name, phone
FROM customers

SELECT product_id, product_name, unit_price, units_in_stock
FROM products
WHERE units_in_stock > 50 OR unit_price > 100
ORDER BY unit_price DESC, units_in_stock DESC

select *
FROM customers
WHERE region IS null AND city = 'México D.F.'

SELECT *
FROM products
WHERE units_in_stock > 50 OR unit_price > 100

SELECT p.product_name, c.category_name
FROM products AS p
    INNER JOIN categories AS c ON p.category_id = c.category_id

SELECT t.territory_description, r.region_description
FROM territories AS t
    INNER JOIN region AS r ON t.region_id = r.region_id
WHERE r.region_description = 'Northern'

SELECT e.employee_id, e.first_name, e.last_name,
    t.territory_description, r.region_description
FROM territories AS t
    INNER JOIN region AS r ON r.region_id = r.region_id
    INNER JOIN employee_territories AS et ON et.territory_id = t.territory_id
    INNER JOIN employees AS e ON e.employee_id = et.employee_id

-- LISTADO DE ORDENES CON SUS PRODUCTOS, CATEGORIAS, PROVEEDORES Y QUIEN DESPACHO

SELECT o.order_id AS "N° ORDEN", p.product_name AS "PRODUCTO",
    c.category_name AS "CATEGORIA", s.company_name AS "PROVEEDOR",
    sh.company_name AS "ENVIADO VIA"
FROM orders AS o
    INNER JOIN order_details AS od ON o.order_id = od.order_id
    INNER JOIN products AS p ON od.product_id = p.product_id
    INNER JOIN categories AS c ON p.category_id = c.category_id
    INNER JOIN suppliers AS s ON p.supplier_id = s.supplier_id
    INNER JOIN shippers AS sh ON o.ship_via = sh.shipper_id

-- LEFT JOIN

SELECT o.order_id, c.company_name, e.last_name |','| e.first_name AS employee_name,
    o.order_date, o.shipped_date, s.company_name AS shipper_name,
    o.ship_name, o.ship_address
FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
    LEFT JOIN employees e ON o.employee_id = e.employee_id
    LEFT JOIN shippers s ON o.ship_via = s.shipper_id