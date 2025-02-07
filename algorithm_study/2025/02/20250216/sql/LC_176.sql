WITH RankedEmployees AS (
    SELECT 
        salary, 
        DENSE_RANK() OVER (ORDER BY salary DESC) AS ranking 
    FROM Employee
)
SELECT 
    CASE 
        WHEN COUNT(*) = 0 THEN NULL 
        ELSE MAX(salary) 
    END AS SecondHighestSalary
FROM RankedEmployees
WHERE ranking = 2;