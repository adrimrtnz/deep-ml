SELECT DISTINCT c.customer_id, c.name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE c.customer_id = o.customer_id
)
