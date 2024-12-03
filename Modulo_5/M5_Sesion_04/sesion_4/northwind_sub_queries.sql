SELECT * FROM orders

-- obtener las ventas cuyo monto sea mayot al average de todas las ventas
SELECT AVG(freight) FROM orders

-- comparando con un valor
SELECT * 
FROM orders
WHERE freight > (SELECT AVG(freight) FROM orders)


-- buscar todos los productos que pertenezcan a una categoria determinada
SELECT * 
FROM products
WHERE category_id IN(SELECT category_id FROM categories 
	WHERE category_name in ('Condiments','Seafood'))


SELECT order_id, (SELECT now()) AS fecha_actual, (SELECT product_name FROM products WHERE product_name = 'Chang')
FROM orders

-- listados de proveedores, cuando la cantidad de productos que provee sea mayor que 

SELECT supplier_id, count(*)
FROM products 
GROUP BY supplier_id
ORDER BY (supplier_id)

SELECT company_name, total_products.total
FROM suppliers
JOIN (select supplier_id, COUNT(*) AS total
		FROM products
		GROUP BY supplier_id) AS total_products
ON suppliers.supplier_id = total_products.supplier_id
WHERE total_products.total > 3