from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0
        r = max(candies)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            cnt = 0
            isPossible = False
            if mid != 0:
                for candy in candies:
                    cnt += candy//mid
                    if cnt >= k:
                        isPossible = True
                        break
            else:
                isPossible = True

            if isPossible:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans
