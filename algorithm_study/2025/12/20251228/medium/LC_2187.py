from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = min(time) * totalTrips

        ans = 0
        while l <= r:
            m = (l+r)//2
            trips = 0
            for t in time:
                trips += m//t
            if trips >= totalTrips:
                r = m-1
                ans = m
            elif trips < totalTrips:
                l = m+1

        return ans
