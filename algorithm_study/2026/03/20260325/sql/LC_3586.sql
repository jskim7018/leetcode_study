SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(neg_date, test_date) AS recovery_time
FROM (
    SELECT
        *,
        LEAD(test_date, 1) OVER (
            PARTITION BY patient_id
            ORDER BY test_date ASC
        ) AS neg_date
    FROM (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY patient_id, result
                ORDER BY test_date ASC
            ) AS rn
        FROM covid_tests
    ) c_rn
    WHERE
        (rn = 1 AND result = 'Positive')
        OR result = 'Negative'
) c_w_neg
LEFT JOIN patients p USING (patient_id)
WHERE
    result = 'Positive'
    AND neg_date IS NOT NULL
ORDER BY
    recovery_time ASC,
    p.patient_name ASC;
