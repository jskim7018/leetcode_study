WITH day_max AS (
    SELECT
        day,
        MAX(amount) AS max_amount
    FROM transactions
    GROUP BY day
)
SELECT
    t.transaction_id
FROM transactions AS t
LEFT JOIN day_max AS dm
    ON t.day = dm.day
WHERE t.amount = dm.max_amount
ORDER BY t.transaction_id ASC;
