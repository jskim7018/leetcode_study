WITH user_friends AS (
    SELECT user_id1, user_id2
    FROM friends
    UNION ALL
    SELECT user_id2 AS user_id1, user_id1 AS user_id2
    FROM friends
)
SELECT f.user_id1, f.user_id2
FROM friends f
WHERE NOT EXISTS (
    SELECT 1
    FROM user_friends uf1
    JOIN user_friends uf2
      ON uf1.user_id2 = uf2.user_id2
    WHERE uf1.user_id1 = f.user_id1
      AND uf2.user_id1 = f.user_id2
      AND uf1.user_id2 NOT IN (f.user_id1, f.user_id2)
)
ORDER BY f.user_id1 ASC, f.user_id2 ASC;