WITH post_table AS (
    SELECT DISTINCT sub_id
    FROM Submissions
    WHERE parent_id IS NULL
)

SELECT 
    p.sub_id AS post_id, 
    COUNT(DISTINCT s.sub_id) AS number_of_comments
FROM 
    post_table p
LEFT JOIN 
    Submissions s 
ON 
    p.sub_id = s.parent_id
GROUP BY 
    p.sub_id;
