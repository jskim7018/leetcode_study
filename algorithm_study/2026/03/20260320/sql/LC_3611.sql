SELECT 
    m.employee_id,
    e.employee_name,
    e.department,
    COUNT(*) AS meeting_heavy_weeks
FROM (
    SELECT 
        employee_id,
        DATE_SUB(meeting_date, INTERVAL WEEKDAY(meeting_date) DAY) AS curr_week_monday,
        SUM(duration_hours) AS week_meeting_hours
    FROM meetings
    GROUP BY 
        employee_id,
        curr_week_monday
    HAVING week_meeting_hours > 20
) m
LEFT JOIN employees e 
    ON m.employee_id = e.employee_id
GROUP BY 
    m.employee_id,
    e.employee_name,
    e.department
HAVING meeting_heavy_weeks >= 2
ORDER BY 
    meeting_heavy_weeks DESC,
    e.employee_name ASC;