SELECT
    SUM(WEEKDAY(submit_date) IN (5, 6)) AS weekend_cnt,
    SUM(WEEKDAY(submit_date) NOT IN (5, 6)) AS working_cnt
FROM tasks;
