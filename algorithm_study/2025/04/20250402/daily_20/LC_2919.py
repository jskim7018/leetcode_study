from typing import List
from functools import cache


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def solve(idx, dist_k) -> int:
            if idx >= n:
                return 0

            ret = float('inf')
            if nums[idx] >= k:
                ret = solve(idx+1, 1)
            else:
                ret = min(ret, solve(idx+1, 1) + k-nums[idx])
            if dist_k != 3:
                ret = min(ret, solve(idx+1, dist_k+1))

            return ret

        ans = float('inf')
        for i in range(3):
            ans = min(ans, solve(i, 3))

        return ans
