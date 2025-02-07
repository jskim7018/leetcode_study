SELECT name
FROM SalesPerson

EXCEPT

SELECT DISTINCT(s.name) 
FROM SalesPerson s
LEFT JOIN Orders o ON s.sales_id = o.sales_id 
JOIN Company c ON c.com_id = o.com_id
WHERE c.name = "RED";
