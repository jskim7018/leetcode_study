WITH steps_with_prevs AS (
    SELECT
        *,
        LAG(steps_date, 1) OVER (
            PARTITION BY user_id
            ORDER BY steps_date ASC
        ) AS prev_date,
        
        LAG(steps_date, 2) OVER (
            PARTITION BY user_id
            ORDER BY steps_date ASC
        ) AS prev_prev_date,
        
        LAG(steps_count, 1) OVER (
            PARTITION BY user_id
            ORDER BY steps_date ASC
        ) AS prev_steps_count,
        
        LAG(steps_count, 2) OVER (
            PARTITION BY user_id
            ORDER BY steps_date ASC
        ) AS prev_prev_steps_count
    FROM steps
)

SELECT
    user_id,
    steps_date,
    ROUND(
        (steps_count + prev_steps_count + prev_prev_steps_count) / 3.0,
        2
    ) AS rolling_average
FROM steps_with_prevs
WHERE DATEDIFF(steps_date, prev_date) = 1
  AND DATEDIFF(prev_date, prev_prev_date) = 1
ORDER BY user_id, steps_date;
