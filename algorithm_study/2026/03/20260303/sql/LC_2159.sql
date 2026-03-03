WITH first_sorted AS (
    SELECT
        first_col,
        ROW_NUMBER() OVER (ORDER BY first_col ASC) AS rn
    FROM data
),
second_sorted AS (
    SELECT
        second_col,
        ROW_NUMBER() OVER (ORDER BY second_col DESC) AS rn
    FROM data
)

SELECT
    f.first_col,
    s.second_col
FROM first_sorted AS f
LEFT JOIN second_sorted AS s
    ON f.rn = s.rn
ORDER BY
    f.rn;