WITH customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        ROUND(AVG(order_rating), 2) AS average_rating,
        COUNT(order_rating) * 1.0 / COUNT(*) * 100 AS rating_percent
    FROM restaurant_orders
    GROUP BY customer_id
),

customer_peak_cnt AS (
    SELECT
        customer_id,
        COUNT(*) AS peak_cnt
    FROM restaurant_orders
    WHERE
        (
            HOUR(order_timestamp) >= 11
            AND (
                HOUR(order_timestamp) <= 13
                OR (HOUR(order_timestamp) = 14 AND MINUTE(order_timestamp) = 0)
            )
        )
        OR
        (
            HOUR(order_timestamp) >= 18
            AND (
                HOUR(order_timestamp) <= 20
                OR (HOUR(order_timestamp) = 21 AND MINUTE(order_timestamp) = 0)
            )
        )
    GROUP BY customer_id
)

SELECT
    cs.customer_id,
    cs.total_orders,
    ROUND(COALESCE(cpc.peak_cnt, 0) / cs.total_orders, 2) * 100 AS peak_hour_percentage,
    cs.average_rating
FROM customer_stats cs
LEFT JOIN customer_peak_cnt cpc
    ON cs.customer_id = cpc.customer_id
WHERE
    cs.total_orders >= 3
    AND ROUND(COALESCE(cpc.peak_cnt, 0) / cs.total_orders, 2) * 100 >= 60
    AND cs.average_rating >= 4.0
    AND cs.rating_percent >= 50
ORDER BY
    cs.average_rating DESC,
    cs.customer_id DESC;