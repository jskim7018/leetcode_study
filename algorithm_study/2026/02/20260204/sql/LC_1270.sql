SELECT
    e1.employee_id
FROM employees AS e1
LEFT JOIN employees AS e2
    ON e1.manager_id = e2.employee_id
LEFT JOIN employees AS e3
    ON e2.manager_id = e3.employee_id
LEFT JOIN employees AS e4
    ON e3.manager_id = e4.employee_id
WHERE
    (
        e2.employee_id = 1
        OR e3.employee_id = 1
        OR e4.employee_id = 1
    )
    AND e1.employee_id != 1;