WITH BinList AS (
    SELECT '[0-5>' AS bin
    UNION ALL
    SELECT '[5-10>'
    UNION ALL
    SELECT '[10-15>'
    UNION ALL
    SELECT '15 or more'
),
AggregatedData AS (
    SELECT 
        CASE
            WHEN duration/60 < 5 THEN '[0-5>'
            WHEN duration/60 >= 5 AND duration/60 < 10 THEN '[5-10>'
            WHEN duration/60 >= 10 AND duration/60 < 15 THEN '[10-15>'
            ELSE '15 or more'
        END AS bin,
        COUNT(*) AS total
    FROM Sessions
    GROUP BY bin
)
SELECT 
    BinList.bin, 
    COALESCE(AggregatedData.total, 0) AS total
FROM BinList
LEFT JOIN AggregatedData
ON BinList.bin = AggregatedData.bin;
