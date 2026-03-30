WITH t_p AS (
    SELECT
        t.customer_id,
        t.transaction_date,
        t.amount,
        p.category
    FROM Transactions t
    JOIN Products p
        ON t.product_id = p.product_id
),

customer_stats AS (
    SELECT
        customer_id,
        ROUND(SUM(amount), 2) AS total_amount,
        COUNT(*) AS transaction_count,
        COUNT(DISTINCT category) AS unique_categories,
        ROUND(AVG(amount), 2) AS avg_transaction_amount,
        ROUND(COUNT(*) * 10 + SUM(amount) / 100, 2) AS loyalty_score
    FROM t_p
    GROUP BY customer_id
),

category_stats AS (
    SELECT
        customer_id,
        category,
        COUNT(*) AS cnt,
        MAX(transaction_date) AS last_date
    FROM t_p
    GROUP BY customer_id, category
),

ranked_category AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY cnt DESC, last_date DESC
        ) AS rn
    FROM category_stats
)

SELECT
    cs.customer_id,
    cs.total_amount,
    cs.transaction_count,
    cs.unique_categories,
    cs.avg_transaction_amount,
    rc.category AS top_category,
    cs.loyalty_score
FROM customer_stats cs
JOIN ranked_category rc
    ON cs.customer_id = rc.customer_id
WHERE rc.rn = 1
ORDER BY
    cs.loyalty_score DESC,
    cs.customer_id ASC;