SELECT 
    customer_id, 
    name 
FROM
    (
        SELECT 
            c.customer_id, 
            c.name
        FROM 
            Orders o
        LEFT JOIN 
            Product p ON o.product_id = p.product_id
        LEFT JOIN 
            Customers c ON o.customer_id = c.customer_id
        WHERE 
            YEAR(o.order_date) = 2020 
            AND (MONTH(o.order_date) = 6 OR MONTH(o.order_date) = 7)
        GROUP BY 
            c.customer_id, 
            YEAR(o.order_date), 
            MONTH(o.order_date)
        HAVING 
            SUM(p.price * o.quantity) >= 100
    ) tmp
GROUP BY 
    name
HAVING 
    COUNT(name) >= 2;
