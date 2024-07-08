select l.city
from listings l,  
(select avg(price) as national_avg from listings) n
group by l.city
having avg(l.price) > max(n.national_avg)
order by l.city

/*
join 없이 아래처럼 바로 select로 가능
inner 쿼리지만 속도 저하 없음.
SELECT city
FROM Listings
GROUP BY city
HAVING AVG(Price) > (
    SELECT avg(price)
    FROM Listings
)
ORDER BY city;
*/