SELECT 
    b.book_id, 
    b.name
FROM books b
LEFT JOIN (
    SELECT 
        book_id, 
        SUM(quantity) AS total_quantity
    FROM orders
    WHERE dispatch_date >= '2018-06-24'
    GROUP BY book_id
) o USING (book_id)
WHERE 
    b.available_from <= '2019-05-23'
    AND (total_quantity IS NULL OR total_quantity < 10);
