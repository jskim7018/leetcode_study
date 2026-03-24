SELECT
    seller_id,
    num_items
FROM (
    SELECT
        seller_id,
        COUNT(DISTINCT o.item_id) AS num_items,
        RANK() OVER (
            ORDER BY COUNT(DISTINCT o.item_id) DESC
        ) AS rnk
    FROM orders o
    LEFT JOIN items i USING (item_id)
    LEFT JOIN users u USING (seller_id)
    WHERE i.item_brand != u.favorite_brand
    GROUP BY seller_id
) o
WHERE rnk = 1
ORDER BY seller_id ASC;