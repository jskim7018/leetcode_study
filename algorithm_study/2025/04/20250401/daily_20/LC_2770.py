from typing import List
from functools import cache


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def solve(idx) -> int:
            if idx >= n:
                return float('-inf')
            if idx == n-1:
                return 0

            ret = float('-inf')
            for i in range(idx+1, n):
                if -target <= nums[i] - nums[idx] <= target:
                    ret = max(ret, solve(i) + 1)
            return ret
        ans = solve(0)
        if ans == float('-inf'):
            return -1
        else:
            return ans
