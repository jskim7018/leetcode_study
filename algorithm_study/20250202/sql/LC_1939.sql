SELECT DISTINCT o1.user_id
FROM Confirmations o1
LEFT JOIN Confirmations o2 
    ON o1.user_id = o2.user_id
WHERE 
    ABS(TIMESTAMPDIFF(SECOND, o1.time_stamp, o2.time_stamp)) <= 24 * 60 * 60
    AND o1.time_stamp <> o2.time_stamp;
