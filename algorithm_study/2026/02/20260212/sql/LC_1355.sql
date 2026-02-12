WITH activity_cnt AS (
    SELECT
        a.name,
        COUNT(f.id) AS cnt,
        MIN(COUNT(f.id)) OVER () AS min_cnt,
        MAX(COUNT(f.id)) OVER () AS max_cnt
    FROM activities a
    LEFT JOIN friends f
        ON a.name = f.activity
    GROUP BY a.id, a.name
)

SELECT
    name AS activity
FROM activity_cnt
WHERE cnt != max_cnt
  AND cnt != min_cnt;
