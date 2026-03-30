WITH ranked_students AS (
    SELECT
        student_id,
        department_id,
        mark,
        RANK() OVER (
            PARTITION BY department_id
            ORDER BY mark DESC
        ) AS rnk,
        COUNT(*) OVER (
            PARTITION BY department_id
        ) AS dep_stud_cnt
    FROM students
)

SELECT
    student_id,
    department_id,
    ROUND(
        COALESCE(
            (rnk - 1) * 100 / (dep_stud_cnt - 1),
            0
        ),
        2
    ) AS percentage
FROM ranked_students;