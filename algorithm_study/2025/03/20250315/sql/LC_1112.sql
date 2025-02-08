SELECT 
    student_id, 
    course_id, 
    grade
FROM 
    (
        SELECT 
            *,
            RANK() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS ranking
        FROM 
            Enrollments
    ) RankedEnrollments
WHERE 
    ranking = 1
ORDER BY 
    student_id ASC;
