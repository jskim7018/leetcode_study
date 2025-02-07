select state, group_concat(city order by city separator ", ") as cities
from cities
group by state
order by state

/*
group_concat 등 함수안에서 keyword가 들어가는 방식들에 대해서 확실히 익히기.
*/