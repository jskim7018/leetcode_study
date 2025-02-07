select tweet_id
from tweets
where length(content) >140 or
length(content) - length(replace(content,'#',''))>3 or
length(content) - length(replace(content,'@',''))>3
order by
tweet_id asc

/*
replace를 한 후에 length를 빼서 갯수를 셀 수 있다.
*/