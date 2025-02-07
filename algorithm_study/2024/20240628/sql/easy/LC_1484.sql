select 
sell_date, 
count(distinct product) as num_sold,
GROUP_CONCAT(distinct product order by product separator ',') as products
from activities
group by sell_date


/*
group_concat을 사용하여 문자열을 aggregate 할 수 있다
*/