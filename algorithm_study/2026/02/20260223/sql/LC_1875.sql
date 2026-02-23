-- group by salary로 제거 unique
-- row_number 부여 (salary desc로)

WITH mult_salary AS (
    SELECT salary
    FROM employees
    GROUP BY salary
    HAVING COUNT(*) > 1
)

SELECT 
    e.*,
    DENSE_RANK() OVER (ORDER BY salary ASC) AS team_id
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM mult_salary ms
    WHERE ms.salary = e.salary
)
ORDER BY team_id ASC, employee_id ASC;