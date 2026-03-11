WITH cinema_w_len AS (
    SELECT DISTINCT 
           c1.seat_id, 
           CASE 
               WHEN c2.seat_id IS NULL THEN 
                   (c1.seat_id - (MIN(c1.seat_id) OVER (ORDER BY c2.seat_id ASC)) + 1)
               ELSE 
                   c1.seat_id - MAX(c2.seat_id) OVER (PARTITION BY c1.seat_id)
           END AS consecutive_seats_len
    FROM cinema c1
    LEFT JOIN cinema c2 
           ON c1.seat_id > c2.seat_id 
          AND c2.free = 0
    WHERE c1.free = 1
)

SELECT 
    seat_id - consecutive_seats_len + 1 AS first_seat_id,
    seat_id AS last_seat_id,
    consecutive_seats_len
FROM (
    SELECT *,
           MAX(consecutive_seats_len) OVER() AS max_len
    FROM cinema_w_len
) c
WHERE consecutive_seats_len = max_len;