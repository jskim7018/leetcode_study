update salary
set sex = case
when sex = 'm' then 'f'
when sex = 'f' then 'm'
end

/*
update statement에서 case문 활용
*/