CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      SELECT IFNULL(COUNT(user_id),0) FROM Purchases
      WHERE time_stamp >= startDate AND time_stamp <= endDate
      GROUP BY user_id
      HAVING SUM(amount) >= minAmount
  );
END