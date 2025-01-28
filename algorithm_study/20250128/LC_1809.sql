SELECT session_id
FROM Playback
WHERE session_id NOT IN (
    SELECT DISTINCT(p.session_id)
    FROM Playback p
    LEFT JOIN Ads a
    ON p.customer_id = a.customer_id
    WHERE p.start_time <= a.timestamp 
      AND p.end_time >= a.timestamp
);
