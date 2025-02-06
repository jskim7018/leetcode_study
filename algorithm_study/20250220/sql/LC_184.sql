WITH RankedEmployee AS (
    SELECT *,
        RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS ranking
    FROM EMPLOYEE
)

SELECT 
    d.name AS Department, 
    re.name AS Employee, 
    re.salary AS Salary
FROM RankedEmployee re
LEFT JOIN Department d ON re.departmentId = d.id
WHERE ranking = 1;