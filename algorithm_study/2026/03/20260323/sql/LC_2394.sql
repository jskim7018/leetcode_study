SELECT employee_id
FROM (
    SELECT 
        *,
        COALESCE(
            SUM(
                CEIL(
                    TIMESTAMPDIFF(SECOND, l.in_time, l.out_time) / 60.0
                )
            ) DIV 60,
            0
        ) AS hours_worked
    FROM employees e
    LEFT JOIN logs l USING (employee_id)
    GROUP BY employee_id
) e
WHERE hours_worked < needed_hours;