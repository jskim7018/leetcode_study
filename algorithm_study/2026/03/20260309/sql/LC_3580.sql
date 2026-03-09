WITH employee_3_pf_reviews AS (
    SELECT
        e.employee_id,
        e.name,
        pr.rating,
        LAG(rating, 1) OVER (
            PARTITION BY pr.employee_id
            ORDER BY review_date ASC
        ) AS prev_rating,
        LAG(rating, 2) OVER (
            PARTITION BY pr.employee_id
            ORDER BY review_date ASC
        ) AS prev_prev_rating,
        ROW_NUMBER() OVER (
            PARTITION BY pr.employee_id
            ORDER BY review_date DESC
        ) AS rn
    FROM performance_reviews pr
    LEFT JOIN employees e
        ON pr.employee_id = e.employee_id
)

SELECT
    employee_id,
    name,
    rating - prev_prev_rating AS improvement_score
FROM employee_3_pf_reviews
WHERE
    prev_prev_rating IS NOT NULL
    AND rn = 1
    AND prev_rating > prev_prev_rating
    AND rating > prev_rating
ORDER BY
    improvement_score DESC,
    name ASC;