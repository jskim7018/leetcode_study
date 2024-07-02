select abs((select max(salary) from
salaries
where department = 'Marketing')
-
(select max(salary) from
salaries
where department = 'Engineering')
) as salary_difference