WITH activity_w_next AS (
    SELECT
        *,
        LEAD(event_date, 1) OVER (
            PARTITION BY player_id
            ORDER BY event_date ASC
        ) AS next_date,
        ROW_NUMBER() OVER (
            PARTITION BY player_id
            ORDER BY event_date ASC
        ) as rn
    FROM activity
)

SELECT
    ROUND(COALESCE(COUNT(player_id) / total_cnt, 0), 2) AS fraction
FROM activity_w_next
JOIN (
    SELECT COUNT(DISTINCT player_id) AS total_cnt
    FROM activity
) total_cnt
WHERE rn = 1 AND DATEDIFF(next_date, event_date) = 1;
