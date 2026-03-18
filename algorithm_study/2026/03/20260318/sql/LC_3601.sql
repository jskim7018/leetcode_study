SELECT
    d.driver_id,
    d.driver_name,
    ROUND(first_half_avg, 2) AS first_half_avg,
    ROUND(second_half_avg, 2) AS second_half_avg,
    ROUND(second_half_avg - first_half_avg, 2) AS efficiency_improvement
FROM (
    SELECT
        driver_id,
        SUM(
            IF(MONTH(trip_date) <= 6, distance_km / fuel_consumed, 0)
        ) / SUM(
            IF(MONTH(trip_date) <= 6, 1, 0)
        ) AS first_half_avg,
        SUM(
            IF(MONTH(trip_date) > 6, distance_km / fuel_consumed, 0)
        ) / SUM(
            IF(MONTH(trip_date) > 6, 1, 0)
        ) AS second_half_avg
    FROM trips
    GROUP BY driver_id
    HAVING
        first_half_avg < second_half_avg
) AS drivers_trips
LEFT JOIN drivers d
    ON drivers_trips.driver_id = d.driver_id
ORDER BY
    efficiency_improvement DESC,
    d.driver_name ASC;
