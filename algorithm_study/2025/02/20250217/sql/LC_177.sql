CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
DETERMINISTIC
BEGIN
    RETURN (
        SELECT 
            CASE 
                WHEN COUNT(*) = 0 THEN NULL 
                ELSE MAX(salary) 
            END
        FROM (
            SELECT 
                salary, 
                DENSE_RANK() OVER (ORDER BY salary DESC) AS ranking 
            FROM Employee
        ) RankedEmployees
        WHERE ranking = N
    );
END
