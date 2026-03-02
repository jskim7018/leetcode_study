-- 1. Group by hour
WITH hour_to_calls AS (
    SELECT
        city,
        HOUR(call_time) AS hour,
        COUNT(*) AS number_of_calls
    FROM calls
    GROUP BY
        city,
        HOUR(call_time)
),
city_max_calls AS (
    SELECT
        city,
        MAX(number_of_calls) AS max_calls
    FROM hour_to_calls
    GROUP BY city
)

SELECT
    htc.city,
    htc.hour AS peak_calling_hour,
    htc.number_of_calls
FROM hour_to_calls htc
LEFT JOIN city_max_calls cmc
    ON htc.city = cmc.city
WHERE htc.number_of_calls = cmc.max_calls
ORDER BY
    peak_calling_hour DESC,
    city DESC;