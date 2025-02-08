SELECT 
    city_id, 
    day, 
    degree 
FROM 
    (
        SELECT 
            city_id, 
            day, 
            degree,
            RANK() OVER (PARTITION BY city_id ORDER BY degree DESC, day ASC) AS ranking
        FROM 
            Weather
    ) RankedWeather
GROUP BY 
    city_id
ORDER BY 
    city_id ASC;
