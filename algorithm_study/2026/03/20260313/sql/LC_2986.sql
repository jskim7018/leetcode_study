WITH transactions_w_prevs AS (
    SELECT
        *,
        LAG(spend, 1) OVER (
            PARTITION BY user_id
            ORDER BY transaction_date ASC
        ) AS prev_spend,

        LAG(spend, 2) OVER (
            PARTITION BY user_id
            ORDER BY transaction_date ASC
        ) AS prev_prev_spend,

        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY transaction_date ASC
        ) AS rn

    FROM transactions
)

SELECT
    user_id,
    spend AS third_transaction_spend,
    transaction_date AS third_transaction_date
FROM transactions_w_prevs
WHERE
    prev_spend < spend
    AND prev_prev_spend < spend
    AND rn = 3
ORDER BY
    user_id ASC;