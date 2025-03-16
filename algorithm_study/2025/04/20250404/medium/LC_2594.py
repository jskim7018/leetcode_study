from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        ranks.sort(reverse=True)
        # solve with binary search
        l = 1
        r = max(ranks) * cars*cars
        ans = 0
        while l <= r:
            mid = (l+r)//2
            isPossible = False
            tmp_cars = cars
            for rank in ranks:
                cars_repaired = math.floor((mid/rank) ** 0.5)
                tmp_cars -= cars_repaired
                if tmp_cars <= 0:
                    isPossible = True
                    break

            if isPossible:
                ans = mid
                r = mid-1
            else:
                l = mid+1


        return ans
    