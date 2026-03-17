WITH stores_inventory AS (
    SELECT *,
           ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY price ASC) AS rn,
           COUNT(*) OVER(PARTITION BY store_id) AS cnt
    FROM stores s
    LEFT JOIN inventory i
    USING (store_id)
),
store_w_min_max AS (
    SELECT store_id,
           store_name,
           location,
           SUM(IF(rn = 1, inventory_id, 0)) AS min_inventory_id,
           SUM(IF(rn = cnt, inventory_id, 0)) AS max_inventory_id
    FROM stores_inventory
    WHERE cnt >= 3
    GROUP BY store_id, store_name, location
)
SELECT s.store_id,
       s.store_name,
       s.location,
       i2.product_name AS most_exp_product,
       i1.product_name AS cheapest_product,
       ROUND(i1.quantity / i2.quantity, 2) AS imbalance_ratio
FROM store_w_min_max s
LEFT JOIN inventory i1 
       ON s.min_inventory_id = i1.inventory_id
LEFT JOIN inventory i2 
       ON s.max_inventory_id = i2.inventory_id
WHERE i2.quantity < i1.quantity
ORDER BY imbalance_ratio DESC,
         s.store_name ASC;