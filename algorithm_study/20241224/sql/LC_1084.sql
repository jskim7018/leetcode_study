SELECT DISTINCT p.product_id, p.product_name
FROM Sales s
LEFT JOIN Product p
    ON s.product_id = p.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date) BETWEEN '2019-01-01' AND '2019-03-31'
    AND MAX(s.sale_date) BETWEEN '2019-01-01' AND '2019-03-31';
