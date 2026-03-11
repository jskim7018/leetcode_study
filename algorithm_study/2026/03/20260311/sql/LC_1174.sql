-- First get min order_date of all
-- Could use window function
WITH delivery_w_min_date AS (
    SELECT *,
           MIN(order_date) OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS first_date
    FROM delivery
),
delivery_first AS (
    SELECT *
    FROM delivery_w_min_date
    WHERE order_date = first_date
)

SELECT 
    ROUND(SUM(order_date = customer_pref_delivery_date)/ COUNT(customer_id) * 100, 2) AS immediate_percentage
FROM delivery_first d
