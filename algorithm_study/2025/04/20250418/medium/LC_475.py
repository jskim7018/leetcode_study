from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        curr_heater = 0
        houses.sort()
        heaters.sort()
        ans = 0

        for i, house in enumerate(houses):
            while curr_heater < len(heaters) and heaters[curr_heater] < house:
                curr_heater += 1

            heater_dist = float('inf')
            if curr_heater - 1 >= 0:
                heater_dist = abs(house - heaters[curr_heater-1])
            if curr_heater < len(heaters):
                heater_dist = min(heater_dist,
                                         abs(house - heaters[curr_heater]))
            ans = max(ans, heater_dist)

        return ans
