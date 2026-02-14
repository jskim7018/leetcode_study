SELECT
    user_id,
    gender
FROM (
    SELECT
        user_id,
        gender,
        CASE
            WHEN gender = 'female' THEN 0
            WHEN gender = 'other'  THEN 1
            WHEN gender = 'male'   THEN 2
        END AS sex_order,
        ROW_NUMBER() OVER (
            PARTITION BY gender
            ORDER BY user_id
        ) AS rn
    FROM genders
) AS genders_order
ORDER BY
    rn,
    sex_order,
    user_id;
