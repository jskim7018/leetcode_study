WITH UnpivotChampionship AS (
    SELECT Wimbledon AS player_id FROM Championships
    UNION ALL
    SELECT Fr_open AS player_id FROM Championships
    UNION ALL
    SELECT US_open AS player_id FROM Championships
    UNION ALL
    SELECT Au_open AS player_id FROM Championships
)

SELECT 
    p.player_id, 
    p.player_name, 
    COUNT(p.player_name) AS grand_slams_count
FROM UnpivotChampionship u
LEFT JOIN Players p ON u.player_id = p.player_id
GROUP BY p.player_name;
