select tweet_id
from tweets
where char_length(content) > 15

/* 
 https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&envId=top-sql-50
 diff between length() and char_length
*/