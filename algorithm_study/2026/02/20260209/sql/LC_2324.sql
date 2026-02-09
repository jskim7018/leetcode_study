WITH product_quantity AS (
    SELECT
        product_id,
        user_id,
        SUM(quantity) AS quantity
    FROM sales
    GROUP BY
        product_id,
        user_id
)
SELECT
    t.user_id,
    t.product_id
FROM (
    SELECT
        s.user_id,
        s.product_id,
        s.quantity * p.price AS price,
        MAX(s.quantity * p.price) OVER (
            PARTITION BY s.user_id
        ) AS max_price
    FROM product_quantity AS s
    JOIN product AS p
        ON p.product_id = s.product_id
) AS t
WHERE
    t.price = t.max_price;