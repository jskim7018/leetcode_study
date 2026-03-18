SELECT
    user_id,
    prompt_count,
    avg_tokens
FROM (
    SELECT
        user_id,
        COUNT(*) AS prompt_count,
        ROUND(SUM(tokens) / COUNT(*), 2) AS avg_tokens,
        MAX(tokens) AS max_tokens
    FROM prompts
    GROUP BY user_id
    HAVING COUNT(*) >= 3
) AS user_stats
WHERE max_tokens > avg_tokens
ORDER BY
    avg_tokens DESC,
    user_id ASC;
