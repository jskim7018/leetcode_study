SELECT 
    tp.team_id, tp.name, 
    CAST(ROW_NUMBER() OVER (
        ORDER BY tp.points DESC, tp.name ASC
    ) AS SIGNED)
    -
    CAST(ROW_NUMBER() OVER (
        ORDER BY (tp.points + pc.points_change) DESC, tp.name ASC
    ) AS SIGNED)
     AS rank_diff
FROM teampoints tp
LEFT JOIN pointschange pc
    ON tp.team_id = pc.team_id;