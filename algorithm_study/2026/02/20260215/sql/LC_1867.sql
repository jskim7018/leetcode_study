WITH orders_avg_quantity AS (
    SELECT
        order_id,
        MAX(quantity) AS max_quantity,
        SUM(quantity) * 1.0 / COUNT(*) AS avg_quantity
    FROM ordersdetails
    GROUP BY order_id
)

SELECT
    oaq.order_id
FROM orders_avg_quantity AS oaq
CROSS JOIN (
    SELECT
        MAX(avg_quantity) AS max_avg_quantity
    FROM orders_avg_quantity
) AS max_aq
WHERE oaq.max_quantity > max_aq.max_avg_quantity;
