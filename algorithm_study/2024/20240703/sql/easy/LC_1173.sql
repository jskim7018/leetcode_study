select 
round(sum(case when datediff(order_date, customer_pref_delivery_date)=0 then 1
else 0 end)/count(*)*100,2) as immediate_percentage
from delivery


/*
avg 함수를 활용할 수 있음. 식을 계산하여 True면 1 아니면 0을 반환하고, 해당 결과의 
평균을 구하여 바로 구할 수 있음.
SELECT ROUND(
    100 * AVG(order_date = customer_pref_delivery_date), 
    2) AS immediate_percentage
FROM 
    Delivery;
*/