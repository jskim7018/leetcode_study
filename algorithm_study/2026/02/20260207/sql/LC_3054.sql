SELECT
    N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N EXISTS (SELECT P FROM tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM tree
ORDER BY N ASC;
