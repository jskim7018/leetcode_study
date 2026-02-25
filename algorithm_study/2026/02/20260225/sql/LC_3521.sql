WITH product_pair AS (
    SELECT 
        pp1.product_id AS p_id1,
        pp2.product_id AS p_id2,
        SUM(pp1.quantity) AS p1_quantity,
        SUM(pp2.quantity) AS p2_quantity
    FROM productpurchases pp1
    JOIN productpurchases pp2
        ON pp1.user_id = pp2.user_id 
       AND pp1.product_id < pp2.product_id
    GROUP BY pp1.user_id, pp1.product_id, pp2.product_id
)

SELECT 
    p.p_id1 AS product1_id,
    p.p_id2 AS product2_id, 
    pf1.category AS product1_category,
    pf2.category AS product2_category,
    COUNT(*) AS customer_count 
FROM product_pair p
LEFT JOIN productinfo pf1 
    ON p.p_id1 = pf1.product_id
LEFT JOIN productinfo pf2 
    ON p.p_id2 = pf2.product_id
WHERE p.p1_quantity > 0 AND p.p2_quantity > 0
GROUP BY 
    p.p_id1, 
    p.p_id2,
    pf1.category,
    pf2.category
HAVING COUNT(*) >= 3
ORDER BY 
    customer_count DESC, 
    product1_id ASC,
    product2_id ASC;