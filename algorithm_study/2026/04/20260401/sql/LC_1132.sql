SELECT
    ROUND(AVG(daily_percent) * 100, 2) AS average_daily_percent
FROM (
    SELECT
        a.action_date,
        COUNT(r.post_id) * 1.0 / COUNT(*) AS daily_percent
    FROM (
        SELECT DISTINCT action_date, post_id
        FROM Actions
        WHERE action = 'report'
          AND extra = 'spam'
    ) a
    LEFT JOIN Removals r
        ON a.post_id = r.post_id
    GROUP BY a.action_date
) t;
