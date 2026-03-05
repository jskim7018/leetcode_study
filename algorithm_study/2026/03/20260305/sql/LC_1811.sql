WITH prev_contests_id AS (
    SELECT
        u.user_id,
        c.contest_id,
        LAG(c.contest_id, 2) OVER (
            PARTITION BY u.user_id
            ORDER BY c.contest_id ASC
        ) AS prevs_contest
    FROM users u
    LEFT JOIN contests c
        ON u.user_id = c.gold_medal
        OR u.user_id = c.silver_medal
        OR u.user_id = c.bronze_medal
),

interview_cand AS (
    SELECT DISTINCT user_id
    FROM prev_contests_id
    WHERE contest_id - prevs_contest = 2
),

gold_medal_3 AS (
    SELECT
        gold_medal AS user_id
    FROM contests
    GROUP BY gold_medal
    HAVING COUNT(gold_medal) >= 3
)

SELECT DISTINCT
    u.name,
    u.mail
FROM users u
LEFT JOIN interview_cand ic
    ON u.user_id = ic.user_id
LEFT JOIN gold_medal_3 gm
    ON u.user_id = gm.user_id
WHERE ic.user_id IS NOT NULL
   OR gm.user_id IS NOT NULL;