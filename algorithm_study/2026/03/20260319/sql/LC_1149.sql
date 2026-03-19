SELECT DISTINCT
    viewer_id AS id
FROM
    views
GROUP BY
    viewer_id,
    view_date
HAVING
    COUNT(DISTINCT article_id) >= 2
ORDER BY id asc;
