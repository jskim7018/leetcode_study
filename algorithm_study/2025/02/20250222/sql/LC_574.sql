SELECT name
FROM (
    SELECT 
        c.name,
        RANK() OVER (ORDER BY COUNT(c.id) DESC) AS ranking
    FROM Candidate c
    LEFT JOIN Vote v ON c.id = v.candidateId
    GROUP BY c.id
) RankedCandidates
WHERE ranking = 1;
