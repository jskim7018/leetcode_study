from typing import List



class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int,
                          maxPrice: int, maxDistance: int) -> List[int]:

        ans = []

        for id, rating, vf, price, distance in restaurants:
            if price <= maxPrice and distance <= maxDistance:
                if veganFriendly == 1:
                    if vf == 1:
                        ans.append((rating, id))
                else:
                    ans.append((rating, id))

        ans.sort(reverse=True)

        return [id for _, id in ans]
