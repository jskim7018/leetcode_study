SELECT DISTINCT
    user_id
FROM (
    SELECT
        user_id,
        DATEDIFF(
            created_at,
            LAG(created_at, 1) OVER (
                PARTITION BY user_id
                ORDER BY created_at ASC
            )
        ) AS date_diff_prev
    FROM users
) p
WHERE date_diff_prev <= 7
ORDER BY user_id ASC;
