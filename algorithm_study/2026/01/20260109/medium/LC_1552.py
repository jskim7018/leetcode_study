from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)

        position.sort()

        l = 0
        r = max(position) - min(position)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            cnt = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= mid:
                    curr = position[i]
                    cnt += 1
                    if cnt >= m:
                        break
            if cnt >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

