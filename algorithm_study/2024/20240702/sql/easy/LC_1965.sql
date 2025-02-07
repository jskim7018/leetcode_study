SELECT
	employee_id
FROM
	(
	SELECT
		*
	FROM
		employees
	LEFT JOIN salaries
			USING (employee_id)
UNION
	SELECT
		*
	FROM
		salaries
	LEFT JOIN employees
			USING (employee_id)) e
WHERE
	e.name IS NULL
	OR e.salary IS NULL
ORDER BY
	e.employee_id