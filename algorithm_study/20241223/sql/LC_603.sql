SELECT seat_id 
FROM Cinema c1
WHERE free = 1 AND 1 IN (
    SELECT free
    FROM Cinema c2 WHERE c1.seat_id-1 = c2.seat_id OR c1.seat_id+1 = c2.seat_id)