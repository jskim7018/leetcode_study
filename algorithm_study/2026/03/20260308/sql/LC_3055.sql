SELECT 
    policy_id,
    state,
    fraud_score
FROM (
    SELECT
        *,
        PERCENT_RANK() OVER (
            PARTITION BY state
            ORDER BY fraud_score DESC
        ) AS percentile_rank
    FROM Fraud
) AS PercentileFraud
WHERE percentile_rank <= 0.05
ORDER BY
    state ASC,
    fraud_score DESC,
    policy_id ASC;