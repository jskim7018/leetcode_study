WITH orders_w_intervals_no AS (
    SELECT
        *,
        FLOOR((minute - 1) / 6) + 1 AS interval_no
    FROM orders
)

SELECT
    interval_no,
    SUM(order_count) AS total_orders
FROM orders_w_intervals_no
GROUP BY interval_no
ORDER BY interval_no ASC;