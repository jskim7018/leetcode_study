SELECT
    COUNT(*) AS accounts_count
FROM (
    SELECT
        s.account_id
    FROM subscriptions AS s
    LEFT JOIN streams AS st
        ON s.account_id = st.account_id
    WHERE
        s.start_date <= '2021-12-31'
        AND s.end_date >= '2021-01-01'
    GROUP BY
        s.account_id
    HAVING
        MAX(st.stream_date) <= '2020-12-31'
        OR MIN(st.stream_date) >= '2022-01-01'
) AS inactive_2021_sub;
