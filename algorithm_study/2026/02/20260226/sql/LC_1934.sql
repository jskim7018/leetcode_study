SELECT
    s.user_id,
    ROUND(IF(
        COUNT(action) = 0,
        0,
        SUM(
            CASE 
                WHEN action = 'confirmed' THEN 1 
                ELSE 0 
            END
        ) / COUNT(*)
    ), 2) AS confirmation_rate
FROM signups s
LEFT JOIN confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id;