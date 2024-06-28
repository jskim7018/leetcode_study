delete p1 from
person p1,
person p2
where p1.email = p2.email and p1.id > p2.id

/*
delete는 위 문법 처럼 대상 테이블과 
다른 비교 테이블 지정 후 조건을 명시 가능.
inner query는 안된다.
*/