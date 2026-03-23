from typing import List
from functools import cache


class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        # bitmask dp. dp[i][j] -> i curr pos, j -> bitmask
        n = len(nums)
        @cache
        def dp(idx: int, curr: int) -> int:
            if idx >= n:
                if curr == target:
                    return 0
                else:
                    return float('inf')

            return min(dp(idx + 1, curr ^ nums[idx]),
                      dp(idx + 1, curr) + 1)

        ans = dp(0,0)
        if ans == float('inf'):
            return -1
        else:
            return ans
