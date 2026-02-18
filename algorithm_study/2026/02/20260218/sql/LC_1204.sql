WITH queue_w_cumul_weight AS (
    SELECT *,
           SUM(weight) OVER (
               ORDER BY turn ASC
               ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
           ) AS weight_to_curr
    FROM queue
)

SELECT person_name
FROM queue_w_cumul_weight
WHERE weight_to_curr <= 1000
ORDER BY weight_to_curr DESC
LIMIT 1;
