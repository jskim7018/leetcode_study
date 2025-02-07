SELECT DISTINCT user_id 
FROM (
    SELECT user_id 
    FROM Loans
    WHERE loan_type = 'Refinance'
    
    INTERSECT
    
    SELECT user_id 
    FROM Loans
    WHERE loan_type = 'Mortgage'
) users
ORDER BY user_id ASC;
