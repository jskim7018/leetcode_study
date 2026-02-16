WITH user_visit_window AS (
    SELECT 
        user_id,
        DATEDIFF(
            LEAD(visit_date, 1, DATE('2021-01-01')) 
            OVER (PARTITION BY user_id ORDER BY visit_date), 
            visit_date
        ) AS visit_window
    FROM uservisits
)
SELECT 
    user_id,
    MAX(visit_window) AS biggest_window
FROM user_visit_window
GROUP BY user_id
ORDER BY user_id ASC;
