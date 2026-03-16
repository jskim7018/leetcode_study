WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER() AS rn
    FROM CoffeeShop
),
grp_cte AS (
    SELECT *,
           SUM(drink IS NOT NULL) OVER (ORDER BY rn) AS grp
    FROM cte
)

SELECT
    id,
    MAX(drink) OVER (PARTITION BY grp) AS drink
FROM grp_cte
ORDER BY rn;