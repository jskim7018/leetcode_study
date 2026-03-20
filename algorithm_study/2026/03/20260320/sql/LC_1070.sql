SELECT 
    product_id,
    first_year,
    quantity,
    price
FROM (
    SELECT 
        product_id,
        year,
        quantity,
        price,
        MIN(year) OVER (
            PARTITION BY product_id 
            ORDER BY year ASC
        ) AS first_year
    FROM sales
) s
WHERE year = first_year;