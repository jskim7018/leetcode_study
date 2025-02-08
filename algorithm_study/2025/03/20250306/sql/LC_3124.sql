SELECT 
    c.first_name, 
    rc.type,
    CONCAT(
        LPAD(FLOOR(rc.duration / 60 / 60) % 60, 2, '0'), ':', 
        LPAD(FLOOR(rc.duration / 60) % 60, 2, '0'), ':', 
        LPAD(rc.duration % 60, 2, '0')
    ) AS duration_formatted
FROM 
    (
        SELECT *,
            DENSE_RANK() OVER (PARTITION BY type ORDER BY duration DESC) AS ranking
        FROM Calls
    ) rc
LEFT JOIN Contacts c
    ON rc.contact_id = c.id
WHERE 
    ranking <= 3
ORDER BY 
    rc.type DESC, 
    rc.duration DESC, 
    c.first_name DESC;
