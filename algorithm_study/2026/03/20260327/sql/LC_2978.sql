WITH coords_w_id AS (
    SELECT
        *,
        ROW_NUMBER() OVER () AS rn
    FROM coordinates
)

SELECT DISTINCT
    c1.X,
    c1.Y
FROM coords_w_id c1
JOIN coords_w_id c2
    ON c1.X = c2.Y
   AND c1.Y = c2.X
WHERE
    c1.X <= c1.Y
    AND c1.rn != c2.rn
ORDER BY
    c1.X ASC,
    c1.Y ASC;