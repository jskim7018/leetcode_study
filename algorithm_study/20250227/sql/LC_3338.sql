SELECT emp_id, dept
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS ranking
    FROM employees
) RankedEmployees
WHERE ranking = 2
ORDER BY emp_id ASC;
