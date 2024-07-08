# partition by 사용

select bike_number, end_time
from bikes
where ride_id in (select first_value(ride_id) over (partition by bike_number order by end_time desc) as bike_number from bikes)
order by end_time desc

/*
그냥 Max 사용 하면 됨. group by를 사용했기에 max를 사용하면 해당 group에서 max를 얻기 때문

SELECT bike_number, MAX(end_time) AS end_time FROM Bikes GROUP BY bike_number ORDER BY end_time DESC
*/