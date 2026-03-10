WITH matches_w_points AS (
    SELECT *,
           CASE 
               WHEN host_goals > guest_goals THEN 3
               WHEN host_goals = guest_goals THEN 1
               ELSE 0
           END AS host_points,
           CASE 
               WHEN guest_goals > host_goals THEN 3
               WHEN host_goals = guest_goals THEN 1
               ELSE 0
           END AS guest_points
    FROM matches
)

SELECT t.team_id,
       t.team_name, 
       COALESCE(
           SUM(
               CASE 
                   WHEN m.host_team = t.team_id THEN host_points
                   ELSE guest_points
               END
           ), 0
       ) AS num_points 
FROM teams t 
LEFT JOIN matches_w_points m
       ON t.team_id = m.host_team 
       OR t.team_id = m.guest_team
GROUP BY t.team_id, t.team_name
ORDER BY num_points DESC, t.team_id ASC;