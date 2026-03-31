SELECT
    activity_date AS login_date,
    COUNT(user_id) AS user_count
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY activity_date ASC
        ) AS rn
    FROM traffic
    WHERE activity = 'login'
) t
WHERE
    rn = 1
    AND activity_date >= DATE_SUB('2019-06-30', INTERVAL 90 DAY)
    AND activity_date <= '2019-06-30'
GROUP BY
    activity_date;