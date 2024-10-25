select count(customer_id) as total_rows
from customers
where region is not null

SELECT SUM(freight) AS sum_total
FROM orders

SELECT MAX(freight),MIN(freight),AVG(freight)
FROM orders

SELECT concat(UPPER(first_name), ' ', LOWER(last_name))
FROM employees
WHERE LENGTH(region) > 1

SELECT 
	now(),
	to_char(now(), 'DD-MM-YYY HH12:MI:SS')

SELECT freight::TEXT, CAST(employee_id AS TEXT)
FROM orders
WHERE LENGTH(CAST(employee_id AS TEXT))>0

SELECT date_part('month', order_date) FROM orders

SELECT p.product_id,  SUM(od.unit_price * od.quantity) 
FROM products p
INNER JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_id
ORDER BY p.product_id


SELECT o.order_date,p.product_id, p.product_name, SUM(od.unit_price * od.quantity) 
FROM products p
INNER JOIN order_details od ON p.product_id = od.product_id
INNER JOIN orders o ON od.order_id = o.order_id
GROUP BY o.order_date, p.product_id
ORDER BY o.order_date, p.product_id 

select * from orders