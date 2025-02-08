WITH CompanyMax AS (
    SELECT 
        company_id, 
        MAX(salary) AS max_salary
    FROM 
        Salaries
    GROUP BY 
        company_id
)

SELECT 
    s.company_id, 
    s.employee_id, 
    s.employee_name,
    CASE
        WHEN max_salary BETWEEN 1000 AND 10000 THEN ROUND(s.salary * 0.76)
        WHEN max_salary > 10000 THEN ROUND(s.salary * 0.51)
        ELSE s.salary
    END AS salary
FROM 
    Salaries s
LEFT JOIN 
    CompanyMax c ON s.company_id = c.company_id;
