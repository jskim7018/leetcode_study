SELECT seller_name
FROM Seller
WHERE seller_name NOT IN (
    SELECT s.seller_name
    FROM Orders o
    LEFT JOIN Seller s ON o.seller_id = s.seller_id
    WHERE YEAR(o.sale_date) = 2020
)
ORDER BY seller_name ASC;
