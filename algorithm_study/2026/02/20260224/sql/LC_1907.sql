SELECT
    'Low Salary' AS category,
    COUNT(IF(income < 20000, income, NULL)) AS accounts_count
FROM accounts

UNION

SELECT
    'Average Salary' AS category,
    COUNT(
        IF(income >= 20000 AND income <= 50000, income, NULL)
    ) AS accounts_count
FROM accounts

UNION

SELECT
    'High Salary' AS category,
    COUNT(IF(income > 50000, income, NULL)) AS accounts_count
FROM accounts;