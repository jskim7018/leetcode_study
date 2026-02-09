SELECT
    SUM(IFNULL(b.apple_count,0)) + SUM(IFNULL(c.apple_count,0)) AS apple_count,
    SUM(IFNULL(b.orange_count,0)) + SUM(IFNULL(c.orange_count,0)) AS orange_count
FROM boxes AS b
LEFT JOIN chests AS c
    ON b.chest_id = c.chest_id;
