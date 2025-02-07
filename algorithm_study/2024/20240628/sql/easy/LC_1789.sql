select employee_id, department_id
from employee
where primary_flag = 'Y' union
select employee_id, department_id  
from employee 
group by employee_id 
having count(*)=1

/*
두 가지 다른 형식의 조건을 만족할때 두번 
inner select 보다 select를 두번하고 union 
하는게 훨씬 빠르다.
O(N^2) vs O(N Log N)
*/