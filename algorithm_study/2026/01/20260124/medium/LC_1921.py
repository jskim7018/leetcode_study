from typing import List
import math


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        reach_times = [math.ceil(d/s) for d,s in zip(dist, speed)]
        reach_times.sort()

        ans = 0
        curr_time = 0
        for rt in reach_times:
            if rt <= curr_time:
                break
            else:
                ans += 1
            curr_time += 1

        return ans
