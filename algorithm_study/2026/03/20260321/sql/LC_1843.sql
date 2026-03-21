WITH trans_months AS (
    SELECT 
        a.account_id,
        a.max_income,
        YEAR(day) * 12 + MONTH(day) AS month_id,
        SUM(IF(type = 'creditor', amount, 0)) AS month_total
    FROM transactions t
    LEFT JOIN accounts a USING (account_id)
    GROUP BY account_id, month_id
    HAVING month_total > a.max_income
),
trans_w_grp AS (
    SELECT 
        *,
        month_id
        - ROW_NUMBER() OVER (
            PARTITION BY account_id 
            ORDER BY month_id
        ) AS grp
    FROM trans_months
)

SELECT DISTINCT account_id
FROM trans_w_grp
GROUP BY account_id, grp
HAVING COUNT(*) >= 2;
