WITH RankedOrders AS (SELECT *,
RANK() OVER (PARTITION BY customer_id, product_id ORDER BY COUNT(product_id)) AS ranking
FROM Orders
GROUP BY customer_id, product_id)

SELECT ro.customer_id, ro.product_id, p.product_name
FROM RankedOrders ro 
LEFT JOIN Products p ON ro.product_id = p.product_id
WHERE ranking = 1