WITH order_w_recent_rnk AS (
    SELECT
        p.product_id,
        p.product_name,
        o.order_id,
        o.order_date,
        RANK() OVER (
            PARTITION BY p.product_id
            ORDER BY o.order_date DESC
        ) AS rnk
    FROM orders o
    LEFT JOIN products p
        ON o.product_id = p.product_id
)

SELECT
    product_name,
    product_id,
    order_id,
    order_date
FROM order_w_recent_rnk
WHERE rnk = 1
ORDER BY
    product_name ASC,
    product_id ASC,
    order_id ASC;