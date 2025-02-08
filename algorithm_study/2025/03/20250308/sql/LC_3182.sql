SELECT 
    student_id 
FROM 
    (
        SELECT 
            s.student_id, 
            s.major
        FROM 
            enrollments e
        LEFT JOIN 
            students s ON e.student_id = s.student_id
        LEFT JOIN 
            courses c ON e.course_id = c.course_id
        WHERE 
            grade = 'A' AND s.major = c.major
        GROUP BY 
            e.student_id
        HAVING 
            COUNT(e.student_id) = 
            (
                SELECT 
                    COUNT(*)
                FROM 
                    courses
                WHERE 
                    major = s.major
                GROUP BY 
                    major
            )
        ORDER BY 
            s.student_id ASC
    ) TopStudents;
