WITH posts_feb_2024 AS (
    SELECT *
    FROM posts
    WHERE post_date BETWEEN '2024-02-01' AND '2024-02-28'
),
posts_feb_stat AS (
    SELECT
        *,
        COUNT(post_id) OVER (
            PARTITION BY user_id
            ORDER BY post_date
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) AS seven_day_posts,
        COUNT(post_id) OVER (PARTITION BY user_id) / 4 AS avg_weekly_posts
    FROM posts_feb_2024
)

SELECT
    user_id,
    MAX(seven_day_posts) AS max_7day_posts,
    MAX(avg_weekly_posts) AS avg_weekly_posts
FROM posts_feb_stat
GROUP BY user_id
HAVING MAX(seven_day_posts) >= MAX(avg_weekly_posts) * 2
ORDER BY user_id;
