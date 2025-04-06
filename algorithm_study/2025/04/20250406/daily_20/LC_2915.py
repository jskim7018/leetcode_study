from typing import List
from functools import cache


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def solve(idx, curr_target) -> float:
            if curr_target == 0:
                return 0
            if curr_target < 0:
                return float('-inf')
            if idx >= n:
                return float('-inf')

            ret = solve(idx+1, curr_target)
            ret = max(ret, solve(idx+1, curr_target-nums[idx]) + 1)
            return ret

        ans = solve(0, target)
        solve.cache_clear()

        if ans == float('-inf'):
            return -1
        else:
            return ans
