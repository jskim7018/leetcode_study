from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # binary search 가능. 더 나은 방법이 있을까?
        # 모두 같은 속도라서 가능할 수도. 소수점 처리 때문에 안되나? 그럼 왜 안되지? 어떤 수학적 원리가 못하게 하는 것인가?
        if len(dist) > math.ceil(hour):
            return -1

        l = 1
        r = 10**7
        ans = -1
        while l <= r:
            mid = (l+r)//2
            hours_taken = 0
            for d in dist[:-1]:
                hours_taken += math.ceil(d/mid)
            hours_taken += dist[-1] / mid

            if hours_taken <= hour:
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans
