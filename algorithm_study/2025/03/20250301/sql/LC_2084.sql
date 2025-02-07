WITH Order0Customers AS (
    SELECT * 
    FROM Orders 
    WHERE order_type = 0
)

SELECT * 
FROM Order0Customers 
WHERE order_type != 1

UNION

SELECT * 
FROM Orders 
WHERE customer_id NOT IN (
    SELECT customer_id 
    FROM Orders 
    WHERE order_type = 0
);
