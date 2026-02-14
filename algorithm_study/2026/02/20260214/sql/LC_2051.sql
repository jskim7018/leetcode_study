WITH member_conv_rate AS (
    SELECT
        m.member_id,
        m.name,
        100 * SUM(IF(charged_amount, 1, 0)) / COUNT(v.visit_id) AS conv_rate
    FROM members m
    LEFT JOIN visits v
        ON m.member_id = v.member_id
    LEFT JOIN purchases p
        ON v.visit_id = p.visit_id
    GROUP BY m.member_id, m.name
)

SELECT
    member_id,
    name,
    CASE
        WHEN conv_rate >= 80 THEN 'Diamond'
        WHEN conv_rate >= 50 THEN 'Gold'
        WHEN conv_rate >= 0  THEN 'Silver'
        ELSE 'Bronze'
    END AS category
FROM member_conv_rate;
