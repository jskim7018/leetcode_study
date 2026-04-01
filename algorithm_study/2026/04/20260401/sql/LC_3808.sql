SELECT
    user_id,
    reaction AS dominant_reaction,
    ROUND(cnt * 1.0 / total_cnt, 2) AS reaction_ratio
FROM (
    SELECT
        user_id,
        reaction,
        cnt,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY cnt DESC
        ) AS rn,
        SUM(cnt) OVER (
            PARTITION BY user_id
        ) AS total_cnt
    FROM (
        SELECT
            user_id,
            reaction,
            COUNT(*) AS cnt
        FROM reactions
        GROUP BY
            user_id,
            reaction
    ) r
) r_stat
WHERE
    rn = 1
    AND total_cnt >= 5
    AND cnt * 1.0 / total_cnt >= 0.6
ORDER BY
    reaction_ratio DESC,
    user_id ASC;
