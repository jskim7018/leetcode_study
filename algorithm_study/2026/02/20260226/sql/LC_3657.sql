-- 1. count
-- 2. max, min datediff
-- 3. sum
WITH cust_transaction_agg AS (
    SELECT
        customer_id,
        SUM(CASE 
                WHEN transaction_type = 'purchase' THEN 1 
                ELSE 0 
            END) AS purchase_cnt,
        DATEDIFF(MAX(transaction_date), MIN(transaction_date)) + 1 AS active_days,
        100 * SUM(CASE 
                      WHEN transaction_type = 'refund' THEN 1 
                      ELSE 0 
                  END) / COUNT(*) AS refund_rate
    FROM customer_transactions
    GROUP BY customer_id
)

SELECT customer_id
FROM cust_transaction_agg
WHERE purchase_cnt >= 3
  AND active_days >= 30
  AND refund_rate < 20
ORDER BY customer_id ASC;