SELECT
    *,
    IF(credit >= 0, "No", "Yes") AS credit_limit_breached
FROM (
    SELECT
        u.user_id,
        u.user_name,
        u.credit
            - SUM(IF(t.paid_by = u.user_id, t.amount, 0))
            + SUM(IF(t.paid_to = u.user_id, t.amount, 0)) AS credit
    FROM users u
    LEFT JOIN transactions t
        ON u.user_id = t.paid_by
        OR u.user_id = t.paid_to
    GROUP BY
        u.user_id,
        u.user_name
) u_trans;