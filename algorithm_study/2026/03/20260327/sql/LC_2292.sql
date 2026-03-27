SELECT DISTINCT product_id
FROM (
    SELECT
        product_id,
        COUNT(*) AS cnt,
        YEAR(purchase_date) AS year,
        LAG(COUNT(*)) OVER (
            PARTITION BY product_id
            ORDER BY YEAR(purchase_date) ASC
        ) AS prev_cnt,
        LAG(YEAR(purchase_date)) OVER (
            PARTITION BY product_id
            ORDER BY YEAR(purchase_date) ASC
        ) AS prev_year
    FROM orders
    GROUP BY product_id, YEAR(purchase_date)
) o
WHERE
    prev_year IS NOT NULL
    AND (year - prev_year) = 1
    AND prev_cnt >= 3
    AND cnt >= 3;