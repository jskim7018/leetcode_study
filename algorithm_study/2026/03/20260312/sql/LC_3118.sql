-- VIP가 없어도 최종 결과에는 0으로라도 표시되어서 나와야함.
-- 이때 없는 것들을 어떻게 고정해서 넣어 둘 수 있을까?
WITH RECURSIVE weeks AS (
    SELECT 1 AS week_of_month
    UNION ALL
    SELECT week_of_month + 1
    FROM weeks
    WHERE week_of_month < 4
),

memberships AS (
    SELECT 'Premium' AS membership
    UNION ALL
    SELECT 'VIP' AS membership
),

week_w_membership AS (
    SELECT *
    FROM weeks w
    CROSS JOIN memberships m
),

nov_total AS (
    SELECT
        (DATEDIFF(p.purchase_date, '2023-11-01') DIV 7) + 1 AS week_of_month,
        u.membership,
        p.amount_spend
    FROM purchases p
    LEFT JOIN users u
        ON p.user_id = u.user_id
    WHERE WEEKDAY(p.purchase_date) = 4
)

SELECT
    w.week_of_month,
    w.membership,
    COALESCE(SUM(n.amount_spend), 0) AS total_amount
FROM week_w_membership w
LEFT JOIN nov_total n
    ON w.week_of_month = n.week_of_month
   AND w.membership = n.membership
GROUP BY
    w.week_of_month,
    w.membership
ORDER BY
    w.week_of_month ASC,
    w.membership ASC;