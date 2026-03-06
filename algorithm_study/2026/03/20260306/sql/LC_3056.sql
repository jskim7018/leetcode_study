SELECT
    ag.age_bucket,
    ROUND(
        SUM(CASE WHEN activity_type = 'send' THEN time_spent ELSE 0 END)
        / SUM(time_spent) * 100,
        2
    ) AS send_perc,
    ROUND(
        SUM(CASE WHEN activity_type = 'open' THEN time_spent ELSE 0 END)
        / SUM(time_spent) * 100,
        2
    ) AS open_perc
FROM activities a
LEFT JOIN age ag
    ON a.user_id = ag.user_id
GROUP BY
    ag.age_bucket;