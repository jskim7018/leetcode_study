from typing import List
from functools import cache

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def solve(l, r, target) -> int:
            if l >= r:
                return 0
            ret = 0
            if sum(nums[l:l+2]) == target:
                ret = max(ret, solve(l+2, r, target) + 1)
            if sum(nums[r-1:r+1]) == target:
                ret = max(ret, solve(l, r-2, target) + 1)
            if nums[l] + nums[r] == target:
                ret = max(ret, solve(l+1, r-1, target) + 1)

            return ret

        return max(solve(0, n-1, nums[0] + nums[1]), solve(0,n-1, nums[0]+nums[-1]),
                   solve(0,n-1, nums[-1]+nums[-2]))
