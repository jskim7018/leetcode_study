WITH unique_logins AS (
    SELECT DISTINCT *
    FROM logins
),
logins_group AS (
    SELECT
        id,
        login_date,
        DATE_SUB(
            login_date,
            INTERVAL ROW_NUMBER() OVER (
                PARTITION BY id
                ORDER BY login_date
            ) DAY
        ) AS grp
    FROM unique_logins
)
SELECT DISTINCT
    l.id,
    a.name
FROM logins_group AS l
LEFT JOIN accounts AS a
    USING (id)
GROUP BY
    l.id,
    l.grp,
    a.name
HAVING COUNT(*) >= 5
ORDER BY
    l.id ASC;