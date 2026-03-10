WITH ranked AS (
    SELECT
        team_name,
        (wins * 3 + draws) AS points,
        RANK() OVER (ORDER BY (wins * 3 + draws) DESC) AS position,
        COUNT(*) OVER () AS total_teams
    FROM TeamStats
)

SELECT
    team_name,
    points,
    position,
    CASE
        WHEN position <= CEIL(total_teams * 0.33) THEN 'Tier 1'
        WHEN position <= CEIL(total_teams * 0.66) THEN 'Tier 2'
        ELSE 'Tier 3'
    END AS tier
FROM ranked
ORDER BY points DESC, team_name ASC;