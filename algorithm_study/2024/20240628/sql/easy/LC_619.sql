# Write your MySQL query statement below
select max(num) as num
from mynumbers
where num in 
(select max(num) from mynumbers 
group by num
having count(num) = 1)

/*
Can be done without where.
Just directly use the table in from.

select max(num) as num
from (
	select num
	from number
	group by num
	having count(*) = 1
) t
*/