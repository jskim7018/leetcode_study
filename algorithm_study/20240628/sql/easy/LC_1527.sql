# Write your MySQL query statement below
select * 
from patients
where conditions like 'DIAB1%' 
or conditions like '% DIAB1%'

/*
like 연산자를 잘 활용하자
*/