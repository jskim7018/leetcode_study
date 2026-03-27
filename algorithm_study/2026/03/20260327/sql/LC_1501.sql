SELECT
    country
FROM (
    SELECT
        c.duration,
        AVG(c.duration) OVER () AS total_avg,
        cty.name AS country
    FROM (
        SELECT caller_id, duration FROM calls
        UNION ALL
        SELECT callee_id, duration FROM calls
    ) c
    LEFT JOIN person p
        ON c.caller_id = p.id
    LEFT JOIN country cty
        ON cty.country_code = SUBSTR(p.phone_number, 1, 3)
) c
GROUP BY
    country
HAVING
    AVG(duration) > MAX(total_avg);