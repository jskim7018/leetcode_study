SELECT 
    ad_id, 
    ROUND(
        IFNULL(
            COUNT(CASE WHEN action = 'Clicked' THEN 1 END) / 
            COUNT(CASE WHEN action IN ('Viewed', 'Clicked') THEN 1 END), 0) * 100, 2) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id ASC;
