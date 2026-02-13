WITH passenger_ids AS (
    SELECT
        passenger_id,
        COUNT(passenger_id) AS cnt
    FROM rides
    GROUP BY passenger_id
)

SELECT
    r.driver_id,
    COALESCE(p.cnt, 0) AS cnt
FROM rides r
LEFT JOIN passenger_ids p
    ON r.driver_id = p.passenger_id
GROUP BY r.driver_id;
