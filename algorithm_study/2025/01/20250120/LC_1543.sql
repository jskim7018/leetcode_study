SELECT 
    LOWER(TRIM(product_name)) AS product_name, 
    DATE_FORMAT(sale_date, '%Y-%m') AS sale_date, 
    COUNT(product_name) AS total
FROM 
    Sales
GROUP BY 
    TRIM(product_name), 
    YEAR(sale_date), 
    MONTH(sale_date)
ORDER BY 
    TRIM(product_name) ASC, 
    sale_date ASC;
