SELECT product_id, name
FROM Products
WHERE 
      name REGEXP '[^0-9][0-9]{3}[^0-9]'   -- match 3 digits surrounded by non-digits
   OR name REGEXP '^[0-9]{3}[^0-9]'        -- 3 digits at the start
   OR name REGEXP '[^0-9][0-9]{3}$'        -- 3 digits at the end
   OR name REGEXP '^[0-9]{3}$'             -- string is exactly 3 digits
ORDER BY product_id;

-- or

SELECT product_id, name
FROM Products
WHERE name REGEXP '(^|[^0-9])[0-9]{3}([^0-9]|$)'  -- exactly 3 digits not part of a longer digit sequence
ORDER BY product_id;
