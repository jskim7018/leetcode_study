SELECT
    WEEK(purchase_date, 1)
      - WEEK(
            DATE_SUB(
                purchase_date,
                INTERVAL DAY(purchase_date) - 1 DAY
            ),1) + 1 AS week_of_month,
    purchase_date,
    SUM(amount_spend) AS total_amount
FROM purchases
WHERE WEEKDAY(purchase_date) = 4
GROUP BY purchase_date
ORDER BY week_of_month ASC;
