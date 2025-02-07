select employee_id, team_size
from employee e join 
(select team_id, count(*) as team_size
from employee
group by team_id) t on e.team_id = t.team_id


/*
partion을 사용한 더 짧은 방법도 있음.
-> over partition by
SELECT 
    employee_id, 
    COUNT(*) OVER(PARTITION BY team_id) AS team_size
FROM Employee
*/