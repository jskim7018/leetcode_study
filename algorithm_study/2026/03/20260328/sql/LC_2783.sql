SELECT
    flight_id,
    LEAST(COUNT(p.passenger_id), f.capacity) AS booked_cnt,
    GREATEST(0, COUNT(p.passenger_id) - f.capacity) AS waitlist_cnt
FROM flights f
LEFT JOIN passengers p
    USING (flight_id)
GROUP BY flight_id
ORDER BY flight_id ASC;
