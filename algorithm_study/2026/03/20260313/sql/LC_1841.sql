WITH teams_w_points AS (
    SELECT
        t.team_name,
        COUNT(*) AS matches_played,

        SUM(
            CASE
                WHEN (
                        t.team_id = m.home_team_id
                        AND m.home_team_goals > m.away_team_goals
                     )
                  OR (
                        t.team_id = m.away_team_id
                        AND m.home_team_goals < m.away_team_goals
                     )
                THEN 3
                WHEN m.home_team_goals = m.away_team_goals
                THEN 1
                ELSE 0
            END
        ) AS points,

        SUM(
            CASE
                WHEN t.team_id = m.home_team_id
                THEN m.home_team_goals
                ELSE 0
            END
        )
        +
        SUM(
            CASE
                WHEN t.team_id = m.away_team_id
                THEN m.away_team_goals
                ELSE 0
            END
        ) AS goal_for,

        SUM(
            CASE
                WHEN t.team_id = m.home_team_id
                THEN m.away_team_goals
                ELSE 0
            END
        )
        +
        SUM(
            CASE
                WHEN t.team_id = m.away_team_id
                THEN m.home_team_goals
                ELSE 0
            END
        ) AS goal_against

    FROM teams t
    JOIN matches m
        ON t.team_id = m.home_team_id
        OR t.team_id = m.away_team_id

    GROUP BY t.team_id
)

SELECT
    *,
    goal_for - goal_against AS goal_diff
FROM teams_w_points
ORDER BY
    points DESC,
    goal_diff DESC,
    team_name ASC;