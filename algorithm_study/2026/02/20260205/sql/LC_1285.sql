WITH start_table AS (
    SELECT
        log_id AS start_id,
        ROW_NUMBER() OVER (ORDER BY log_id) AS id
    FROM logs
    WHERE log_id - 1 NOT IN (
        SELECT log_id
        FROM logs
    )
),
end_table AS (
    SELECT
        log_id AS end_id,
        ROW_NUMBER() OVER (ORDER BY log_id) AS id
    FROM logs
    WHERE log_id + 1 NOT IN (
        SELECT log_id
        FROM logs
    )
)

SELECT
    s.start_id,
    e.end_id
FROM start_table AS s
LEFT JOIN end_table AS e
    ON s.id = e.id
ORDER BY
    s.start_id ASC;

-- WITH numbered AS (
--     SELECT
--         log_id,
--         log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
--     FROM logs
-- )
-- SELECT
--     MIN(log_id) AS start_id,
--     MAX(log_id) AS end_id
-- FROM numbered
-- GROUP BY grp
-- ORDER BY start_id;
