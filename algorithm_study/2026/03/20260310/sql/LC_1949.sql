WITH all_friends AS (
    SELECT user1_id AS user_id, user2_id AS friend_id FROM Friendship
    UNION ALL
    SELECT user2_id, user1_id FROM Friendship
),
common_friends AS (
    SELECT 
        f1.user_id AS user1_id,
        f2.user_id AS user2_id,
        COUNT(*) AS common_friend
    FROM all_friends f1
    JOIN all_friends f2
        ON f1.friend_id = f2.friend_id
        AND f1.user_id < f2.user_id
    GROUP BY f1.user_id, f2.user_id
)

SELECT 
    f.user1_id,
    f.user2_id,
    c.common_friend
FROM Friendship f
JOIN common_friends c
    ON f.user1_id = c.user1_id
    AND f.user2_id = c.user2_id
WHERE c.common_friend >= 3;