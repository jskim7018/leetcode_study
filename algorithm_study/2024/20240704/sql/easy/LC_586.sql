/*
group by function을 order by에서도 사용이 가능.
일부분만 추출하기 위해서 limit 사용이 가능. 
limit으로 top max 혹은 min을 추출 가능.
*/

select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1