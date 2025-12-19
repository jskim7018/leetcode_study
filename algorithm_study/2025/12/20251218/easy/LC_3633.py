from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)

        ans = float('inf')
        for i in range(n):
            land_end_time = landStartTime[i] + landDuration[i]
            for j in range(m):
                ans = min(ans, max(land_end_time,waterStartTime[j]) + waterDuration[j])

        for i in range(m):
            water_end_time = waterStartTime[i] + waterDuration[i]
            for j in range(n):
                ans = min(ans, max(water_end_time,landStartTime[j]) + landDuration[j])

        return ans
