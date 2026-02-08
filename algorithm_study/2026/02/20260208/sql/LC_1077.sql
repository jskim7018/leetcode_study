WITH project_max AS (
    SELECT
        p.project_id,
        MAX(e.experience_years) AS max_exp_year
    FROM project p
    LEFT JOIN employee e
        ON p.employee_id = e.employee_id
    GROUP BY
        p.project_id
)

SELECT
    pm.project_id,
    e.employee_id
FROM employee e
LEFT JOIN project p
    ON e.employee_id = p.employee_id
LEFT JOIN project_max pm
    ON p.project_id = pm.project_id
WHERE
    e.experience_years = pm.max_exp_year;
