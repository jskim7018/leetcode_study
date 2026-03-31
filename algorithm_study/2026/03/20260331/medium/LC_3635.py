from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        # 둘중의 하나로 시작. 그리고 다음꺼를 가장 빠르게 끝나는 O(n)안에 구함.
        # can optimize O(n) lookup further with binary search
        min_land_end = float('inf')
        min_water_end = float('inf')

        for start, duration in zip(landStartTime, landDuration):
            min_land_end = min(min_land_end, start + duration)

        for start, duration in zip(waterStartTime, waterDuration):
            min_water_end = min(min_water_end, start + duration)

        ans = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            if start >= min_water_end:
                ans = min(ans, start + duration)
            else:
                ans = min(ans, min_water_end + duration)

        for start, duration in zip(waterStartTime, waterDuration):
            if start >= min_land_end:
                ans = min(ans, start + duration)
            else:
                ans = min(ans, min_land_end + duration)

        return ans
