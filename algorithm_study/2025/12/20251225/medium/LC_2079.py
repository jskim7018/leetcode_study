from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        curr_capacity = capacity
        ans = 0
        for i, p in enumerate(plants):
            if curr_capacity >= p:
                curr_capacity -= p
                ans += 1
            else:
                curr_capacity = capacity - p
                ans += (i+1) * 2 - 1

        return ans
