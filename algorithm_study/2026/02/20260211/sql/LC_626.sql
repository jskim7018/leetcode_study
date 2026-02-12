WITH seat_w_rn AS (
    SELECT
        *,
        ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM seat
),
seat_change_id AS (
    SELECT
        *,
        IF(rn % 2 = 1, rn + 1, rn - 1) AS change_id
    FROM seat_w_rn
)
SELECT
    sci.id,
    COALESCE(s.student, sci.student) AS student
FROM seat_change_id AS sci
LEFT JOIN seat AS s
    ON sci.change_id = s.id
ORDER BY
    sci.id ASC;

-- Using window function (LEAD, LAG)
-- SELECT
--     id,
--     COALESCE(
--         IF(
--             id % 2 = 1,
--             LEAD(student, 1) OVER (ORDER BY id),
--             LAG(student, 1) OVER (ORDER BY id)
--         ),
--         student
--     ) AS student
-- FROM seat
-- ORDER BY
--     id ASC;
