WITH proj_skill_cnt AS (
    SELECT 
        project_id, 
        COUNT(*) AS cnt
    FROM projects
    GROUP BY project_id
),
proj_cand_score AS (
    SELECT 
        p.project_id, 
        c.candidate_id, 
        100 + SUM(
            CASE 
                WHEN c.proficiency > p.importance THEN 10
                WHEN c.proficiency < p.importance THEN -5
                ELSE 0
            END
        ) AS score,
        cnt
    FROM projects p
    LEFT JOIN candidates c 
        ON p.skill = c.skill
    LEFT JOIN proj_skill_cnt psc 
        ON p.project_id = psc.project_id
    GROUP BY p.project_id, c.candidate_id, cnt
    HAVING COUNT(*) = cnt
)
SELECT 
    project_id, 
    candidate_id, 
    score
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY project_id 
            ORDER BY score DESC, candidate_id ASC
        ) AS rn
    FROM proj_cand_score
) p
WHERE rn = 1
ORDER BY project_id;