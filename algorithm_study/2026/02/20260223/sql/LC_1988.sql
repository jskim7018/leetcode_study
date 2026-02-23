SELECT 
    school_id, 
    COALESCE(
        (
            SELECT score
            FROM exam
            WHERE student_count <= s.capacity
            ORDER BY student_count DESC, score ASC
            LIMIT 1
        ),
        -1
    ) AS score
FROM schools s;