WITH common_followers AS (
    SELECT
        r1.user_id AS user1_id,
        r2.user_id AS user2_id,
        COUNT(*) AS common_cnt,
        MAX(COUNT(*)) OVER () AS max_cnt
    FROM Relations r1
    JOIN Relations r2
        ON r1.follower_id = r2.follower_id
       AND r1.user_id < r2.user_id
    GROUP BY
        r1.user_id,
        r2.user_id
)

SELECT
    user1_id,
    user2_id
FROM common_followers
WHERE common_cnt = max_cnt;
