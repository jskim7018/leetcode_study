WITH all_platforms AS (
    SELECT 'Android' AS platform
    UNION ALL
    SELECT 'IOS'
    UNION ALL
    SELECT 'Web'
),
all_experiments AS (
    SELECT 'Reading' AS experiment_name
    UNION ALL
    SELECT 'Programming'
    UNION ALL
    SELECT 'Sports'
),
platform_experiments AS (
    SELECT *
    FROM all_platforms
    CROSS JOIN all_experiments
),
experiment_counts AS (
    SELECT
        platform,
        experiment_name,
        COUNT(*) AS num_experiments
    FROM experiments
    GROUP BY
        platform,
        experiment_name
)

SELECT
    pe.platform,
    pe.experiment_name,
    COALESCE(ec.num_experiments, 0) AS num_experiments
FROM platform_experiments pe
LEFT JOIN experiment_counts ec
    ON pe.platform = ec.platform
   AND pe.experiment_name = ec.experiment_name;
