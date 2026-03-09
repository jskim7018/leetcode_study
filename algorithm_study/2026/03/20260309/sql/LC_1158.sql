WITH user_order_cnt AS (
    SELECT
        u.user_id,
        COUNT(o.order_id) AS orders_in_2019
    FROM users u
    LEFT JOIN orders o
        ON u.user_id = o.buyer_id
    WHERE YEAR(o.order_date) = 2019
    GROUP BY u.user_id
)

SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COALESCE(uoc.orders_in_2019, 0) AS orders_in_2019
FROM users u
LEFT JOIN user_order_cnt uoc
    ON u.user_id = uoc.user_id;