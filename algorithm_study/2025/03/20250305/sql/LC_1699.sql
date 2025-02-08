WITH NormalizedCalls AS (
    SELECT 
        CASE
            WHEN from_id < to_id THEN from_id
            ELSE to_id
        END AS from_id,
        CASE
            WHEN from_id < to_id THEN to_id
            ELSE from_id
        END AS to_id,
        duration
    FROM Calls
)

SELECT
    from_id AS person1,
    to_id AS person2,
    COUNT(*) AS call_count,
    SUM(duration) AS total_duration
FROM NormalizedCalls
GROUP BY from_id, to_id;
