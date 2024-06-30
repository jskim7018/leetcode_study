select date_format(order_date, "%Y-%m") as month, 
count(distinct order_id) as order_count, 
count(distinct customer_id) as customer_count
from orders
where invoice > 20
group by year(order_date), month(order_date)



/*
아래 처럼 숫자를 사용해서 column을 명시할 수 있음. 
중복으로 처리한거를 다시 작성하지 않아도 되게 됨.
select date_format(order_date, "%Y-%m") as month, 
count(distinct order_id) as order_count, 
count(distinct customer_id) as customer_count
from orders
where invoice > 20
group by 1
혹은 1을 month로 적어도 됨.
*/