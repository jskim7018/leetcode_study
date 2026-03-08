WITH product_ids AS (
    SELECT DISTINCT
        product_id
    FROM products
),

product_w_max_date AS (
    SELECT
        p.*,
        MAX(change_date) OVER (
            PARTITION BY product_id
            ORDER BY change_date DESC
        ) AS max_date
    FROM products p
    WHERE change_date <= '2019-08-16'
),

products_w_price AS (
    SELECT
        product_id,
        new_price AS price
    FROM product_w_max_date
    WHERE change_date = max_date
)

SELECT
    pi.product_id,
    COALESCE(pwp.price, 10) AS price
FROM product_ids pi
LEFT JOIN products_w_price pwp
    ON pi.product_id = pwp.product_id;