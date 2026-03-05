WITH feb_hash AS (
    SELECT
        REGEXP_SUBSTR(tweet, '#[A-Za-z0-9]+') AS hashtag
    FROM tweets
    WHERE tweet_date >= '2024-02-01'
      AND tweet_date <  '2024-03-01'
)

SELECT
    hashtag,
    COUNT(hashtag) AS hashtag_count
FROM feb_hash
GROUP BY hashtag
ORDER BY
    hashtag_count DESC,
    hashtag DESC
LIMIT 3;