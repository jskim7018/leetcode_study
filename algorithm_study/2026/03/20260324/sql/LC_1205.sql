WITH transactions_w_chargebacks AS (
    SELECT *
    FROM transactions

    UNION ALL

    SELECT
        t.id,
        t.country,
        'chargeback' AS state,
        t.amount,
        c.trans_date
    FROM chargebacks c
    LEFT JOIN transactions t
        ON c.trans_id = t.id
)

SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    SUM(IF(state = 'approved', 1, 0)) AS approved_count,
    SUM(IF(state = 'approved', amount, 0)) AS approved_amount,
    SUM(IF(state = 'chargeback', 1, 0)) AS chargeback_count,
    SUM(IF(state = 'chargeback', amount, 0)) AS chargeback_amount
FROM transactions_w_chargebacks
GROUP BY
    month,
    country
HAVING
    approved_count != 0
    OR approved_amount != 0
    OR chargeback_count != 0
    OR chargeback_amount != 0;