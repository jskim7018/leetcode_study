SELECT
    fuel_type,
    driver_id,
    avg_rating AS rating,
    total_distance AS distance
FROM (
    SELECT
        d.driver_id,
        v.fuel_type,
        ROUND(AVG(t.rating),2) AS avg_rating,
        SUM(t.distance) AS total_distance,
        SUM(d.accidents) AS total_accidents,
        ROW_NUMBER() OVER (
            PARTITION BY v.fuel_type
            ORDER BY
                AVG(t.rating) DESC,
                SUM(t.distance) DESC,
                SUM(d.accidents) ASC
        ) AS rn
    FROM drivers d
    LEFT JOIN vehicles v
        ON d.driver_id = v.driver_id
    LEFT JOIN trips t
        ON t.vehicle_id = v.vehicle_id
    GROUP BY
        d.driver_id,
        v.fuel_type
) f
WHERE rn = 1 AND fuel_type IS NOT NULL
AND avg_rating IS NOT NULL
AND total_distance IS NOT NULL
ORDER BY
    fuel_type ASC;
