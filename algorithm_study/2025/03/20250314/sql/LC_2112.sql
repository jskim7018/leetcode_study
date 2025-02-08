WITH NormalizedFlights AS (
    SELECT 
        departure_airport AS airport_id, 
        flights_count
    FROM 
        Flights

    UNION ALL

    SELECT 
        arrival_airport AS airport_id, 
        flights_count
    FROM 
        Flights
)

SELECT 
    airport_id
FROM 
    (
        SELECT 
            *,
            RANK() OVER (ORDER BY SUM(flights_count) DESC) AS ranking
        FROM 
            NormalizedFlights
        GROUP BY 
            airport_id
    ) RankedFlights
WHERE 
    ranking = 1;
