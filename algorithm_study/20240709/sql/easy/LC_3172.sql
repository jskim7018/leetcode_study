select user_id
from emails e left join texts t on e.email_id = t.email_id
where t.signup_action = 'Verified' and datediff(t.action_date,e.signup_date)=1
order by user_id