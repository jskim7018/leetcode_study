select a.machine_id, round(avg(b.timestamp-a.timestamp), 3) as processing_time
from activity a join activity b
on a.machine_id = b.machine_id and a.process_id = b.process_id
and a.activity_type = 'start' and b.activity_type = 'end'
group by machine_id

/*
아래 처럼 join을 직접적으로 하지 않아도 할 수 있다. from에 여러개의 테이블을 명시하여 where
문에서 조건을 맞춰서 쿼리하여 join 없이도 가능.
SELECT a.machine_id, 
       ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a, 
     Activity b
WHERE 
    a.machine_id = b.machine_id
AND 
    a.process_id = b.process_id
AND 
    a.activity_type = 'start'
AND 
    b.activity_type = 'end'
GROUP BY machine_id
*/