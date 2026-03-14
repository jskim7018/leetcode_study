WITH user_stats AS (
    SELECT
        user_id,
        MIN(event_date) AS first_event_date,
        MAX(event_date) AS last_event_date,
        MAX(monthly_amount) AS max_historical_amount,
        SUM(event_type = 'downgrade') AS downgrade_count
    FROM subscription_events
    GROUP BY user_id
),

last_event AS (
    SELECT
        user_id,
        plan_name AS current_plan,
        monthly_amount AS current_monthly_amount,
        event_type,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC
        ) AS rn
    FROM subscription_events
)

SELECT
    u.user_id,
    l.current_plan,
    l.current_monthly_amount,
    u.max_historical_amount,
    DATEDIFF(u.last_event_date, u.first_event_date) AS days_as_subscriber
FROM user_stats u
JOIN last_event l
    ON u.user_id = l.user_id
   AND l.rn = 1
WHERE
    l.event_type <> 'cancel'                          -- active
    AND u.downgrade_count > 0                         -- has downgrade
    AND l.current_monthly_amount < 0.5 * u.max_historical_amount
    AND DATEDIFF(u.last_event_date, u.first_event_date) >= 60
ORDER BY
    days_as_subscriber DESC,
    user_id ASC;