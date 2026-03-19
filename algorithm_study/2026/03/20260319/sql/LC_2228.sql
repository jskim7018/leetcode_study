SELECT DISTINCT
    user_id
FROM (
    SELECT
        user_id,
        DATEDIFF(
            purchase_date,
            LAG(purchase_date, 1) OVER (
                PARTITION BY user_id
                ORDER BY purchase_date ASC
            )
        ) AS date_diff_prev
    FROM purchases
) p
WHERE date_diff_prev <= 7
ORDER BY user_id ASC;
