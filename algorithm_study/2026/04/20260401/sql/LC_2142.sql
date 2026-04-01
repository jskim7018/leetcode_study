SELECT
    bus_id,
    SUM(
        CASE
            WHEN rn = 1 AND passenger_id IS NOT NULL THEN 1
            ELSE 0
        END
    ) AS passengers_cnt
FROM (
    SELECT
        b.bus_id,
        p.passenger_id,
        ROW_NUMBER() OVER (
            PARTITION BY p.passenger_id
            ORDER BY b.arrival_time ASC
        ) AS rn
    FROM buses b
    LEFT JOIN passengers p
        ON b.arrival_time >= p.arrival_time
) bp
GROUP BY
    bus_id
ORDER BY
    bus_id ASC;
