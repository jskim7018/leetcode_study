WITH friends AS (
    SELECT IF(user1_id = 1, user2_id, user1_id) AS friend_id
    FROM friendship
    WHERE user1_id = 1 OR user2_id = 1
)

SELECT DISTINCT l.page_id as recommended_page
FROM friends f
JOIN likes l ON l.user_id = f.friend_id
WHERE NOT EXISTS (
    SELECT 1
    FROM likes l2
    WHERE l2.user_id = 1
      AND l2.page_id = l.page_id
);