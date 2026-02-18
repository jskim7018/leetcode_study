WITH order_w_rn AS (
    SELECT
        c.name AS customer_name,
        c.customer_id,
        o.order_id,
        o.order_date,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY o.order_date DESC
        ) AS rn
    FROM orders o
    LEFT JOIN customers c
        ON o.customer_id = c.customer_id
)

SELECT
    customer_name,
    customer_id,
    order_id,
    order_date
FROM order_w_rn
WHERE rn <= 3
ORDER BY
    customer_name ASC,
    customer_id ASC,
    order_date DESC;
