SELECT
    'bear' AS word,
    COUNT(*) AS count
FROM files
WHERE content LIKE '% bear %'

UNION ALL

SELECT
    'bull' AS word,
    COUNT(*) AS count
FROM files
WHERE content LIKE '% bull %';