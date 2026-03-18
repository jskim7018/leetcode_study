SELECT
    student_id,
    subject,
    first_score,
    latest_score
FROM (
    SELECT
        *,
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date ASC
        ) AS first_score,
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date DESC
        ) AS latest_score
    FROM scores
) AS score_w_first_last
WHERE latest_score > first_score
GROUP BY
    student_id,
    subject
HAVING COUNT(*) >= 2;
