WITH pt_w_most_time_lot AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY car_id
            ORDER BY total_time DESC
        ) AS rn
    FROM (
        SELECT
            car_id,
            SUM(TIMESTAMPDIFF(SECOND, entry_time, exit_time)) AS total_time,
            lot_id
        FROM parkingtransactions
        GROUP BY
            car_id,
            lot_id
    ) AS pt
)

SELECT
    pt.car_id,
    SUM(pt.fee_paid) AS total_fee_paid,
    ROUND(
        SUM(pt.fee_paid) /
        SUM(TIMESTAMPDIFF(SECOND, pt.entry_time, pt.exit_time) / (60 * 60)),
        2
    ) AS avg_hourly_fee,
    pwm.lot_id AS most_time_lot
FROM parkingtransactions AS pt
LEFT JOIN pt_w_most_time_lot AS pwm
       ON pt.car_id = pwm.car_id
      AND pwm.rn = 1
GROUP BY
    pt.car_id
ORDER BY
    pt.car_id ASC;