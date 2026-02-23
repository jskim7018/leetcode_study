-- event_type 별로 average occurrences 구함
-- (SUM(occurrences) / COUNT(business_id))
-- occurrences가 평균보다 큰 business를 찾음

WITH event_avg_occ AS (
    SELECT
        event_type,
        SUM(occurrences) / COUNT(business_id) AS avg_occ
    FROM events
    GROUP BY event_type
)

SELECT
    e.business_id
FROM events e
JOIN event_avg_occ eao
    ON e.event_type = eao.event_type
WHERE e.occurrences > eao.avg_occ
GROUP BY e.business_id
HAVING COUNT(e.business_id) > 1;