SELECT
    p.product_id,
    p.price * (100 - COALESCE(d.discount, 0)) / 100 AS final_price,
    p.category
FROM products AS p
LEFT JOIN discounts AS d
    ON p.category = d.category
ORDER BY p.product_id ASC;
