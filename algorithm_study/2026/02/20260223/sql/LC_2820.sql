-- Get vote weight for voter
-- group by candidate and sum vote weights
-- Get most vote. and rank it with rank()
-- Then get rank 1

WITH votes_w_weight AS (
    SELECT
        *,
        1 / COUNT(candidate) OVER (PARTITION BY voter) AS vote_weight
    FROM votes
),
cand_w_rank AS (
    SELECT
        candidate,
        SUM(vote_weight) AS total_votes,
        RANK() OVER (
            ORDER BY SUM(vote_weight) DESC
        ) AS rnk
    FROM votes_w_weight
    GROUP BY candidate
)
SELECT
    candidate
FROM cand_w_rank
WHERE rnk = 1
ORDER BY candidate ASC;