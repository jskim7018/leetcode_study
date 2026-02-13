SELECT
    c.customer_id,
    c.customer_name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
HAVING
    SUM(o.product_name = 'A') > 0
    AND SUM(o.product_name = 'B') > 0
    AND SUM(o.product_name = 'C') = 0;
