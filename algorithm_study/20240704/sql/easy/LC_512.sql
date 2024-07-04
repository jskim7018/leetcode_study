SELECT DISTINCT
  A.player_id,
  FIRST_VALUE(A.device_id) OVER (
    PARTITION BY
      A.player_id
    ORDER BY
      A.event_date
  ) AS device_id
FROM
  Activity A

/*
Window Function 개념 이해하기. (window_function() over ... partition by)
What is Window Function??

SELECT column1, column2, ..., 
       window_function() OVER (PARTITION BY columnX ORDER BY columnY)
FROM table_name;
*/

/*
WITH
  ranked_logins AS (
    SELECT
      A.player_id,
      A.device_id,
      RANK() OVER (
        PARTITION BY
          A.player_id
        ORDER BY
          A.event_date
      ) AS rnk
    FROM
      Activity A
  )
SELECT
  RL.player_id,
  RL.device_id
FROM
  ranked_logins RL
WHERE
  RL.rnk = 1;
*/


/*
기본 개념을 활용해서 아래 inner 쿼리로 해결도 가능

SELECT
  A1.player_id,
  A1.device_id
FROM
  Activity A1
WHERE
  (A1.player_id, A1.event_date) IN (
    SELECT
      A2.player_id,
      MIN(A2.event_date)
    FROM
      Activity A2
    GROUP BY
      A2.player_id
  );
*/