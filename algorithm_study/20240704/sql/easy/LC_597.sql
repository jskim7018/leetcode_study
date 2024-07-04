SELECT
ROUND(
    IFNULL(
    (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS A)
    /
    (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS B),
    0)
, 2) AS accept_rate;

/*
distinct는 명시된 모든 column을 기준으로 판단된다. 이 경우 accept_date
를 명시하지 않았기에 해당 컬럼만 제외한 distinct값을 가져온다.

*/