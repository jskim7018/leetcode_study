-- 1. Sort by server_id and status_time
-- 2. Use LEAD to bring the next status_time down as stop_time

WITH ordered_events AS (
    SELECT
        server_id,
        status_time,
        session_status,
        LEAD(status_time) OVER (
            PARTITION BY server_id
            ORDER BY status_time
        ) AS next_time
    FROM Servers
)

SELECT
    FLOOR(
        SUM(
            CASE
                WHEN session_status = 'start'
                THEN TIMESTAMPDIFF(SECOND, status_time, next_time)
                ELSE 0
            END
        ) / (60 * 60 * 24)
    ) AS total_uptime_days
FROM ordered_events;