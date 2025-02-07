SELECT 
    SUBSTRING_INDEX(email, '@', -1) AS email_domain,
    COUNT(id) AS count
FROM Emails
WHERE SUBSTRING_INDEX(email, '.', -1) = 'com'
GROUP BY email_domain
ORDER BY email_domain ASC;
