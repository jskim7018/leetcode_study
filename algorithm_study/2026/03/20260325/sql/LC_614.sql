SELECT
    followee AS follower,
    COUNT(follower) AS num
FROM follow f
WHERE EXISTS (
    SELECT 1
    FROM follow
    WHERE follower = f.followee
)
GROUP BY
    followee
ORDER BY
    follower ASC;
