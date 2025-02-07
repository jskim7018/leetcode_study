/*
from에서 ,를 사용하고 join을 아무것도 명시 하지 않으면 cross join이 된다.
*/
SELECT
	a.student_name AS member_a,
	b.student_name AS member_b,
	c.student_name AS member_c
FROM
	schoola a,
	schoolb b,
	schoolc c
WHERE
	a.student_id != b.student_id
	AND a.student_id != c.student_id
	AND b.student_id != c.student_id
	AND a.student_name != b.student_name
	AND a.student_name != c.student_name
	AND b.student_name != c.student_name