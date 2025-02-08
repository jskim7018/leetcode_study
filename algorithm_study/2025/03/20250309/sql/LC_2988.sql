SELECT 
    emp_name AS manager_name, 
    dep_id
FROM 
    (
        SELECT 
            *, 
            RANK() OVER (ORDER BY COUNT(*) DESC) AS ranking
        FROM 
            Employees
        GROUP BY 
            dep_id
    ) RankedDept
WHERE 
    ranking = 1
ORDER BY 
    dep_id ASC;
