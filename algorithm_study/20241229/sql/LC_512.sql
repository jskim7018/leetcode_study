SELECT player_id, device_id
FROM (
    SELECT *, 
           ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS row_num
    FROM Activity
) AS a1
WHERE row_num = 1;
