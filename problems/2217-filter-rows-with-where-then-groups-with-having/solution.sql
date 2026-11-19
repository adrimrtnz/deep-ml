SELECT customer_id, COUNT(order_id), SUM(amount)
FROM orders
WHERE status = 'completed'
GROUP BY customer_id
HAVING COUNT(order_id) > 1 AND SUM(amount) >= 100