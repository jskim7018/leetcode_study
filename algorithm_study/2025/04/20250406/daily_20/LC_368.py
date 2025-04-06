from typing import List
from functools import cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        @cache
        def solve(idx) -> tuple[int]:
            ret = []
            for i in range(idx+1, n):
                if nums[i] % nums[idx] != 0:
                    continue
                solved = solve(i)
                if len(solved) > len(ret):
                    ret = solved
            ret = list(ret)
            ret.append(nums[idx])
            return tuple(ret)

        ans = ()
        for i in range(n):
            solved = solve(i)
            if len(solved) > len(ans):
                ans = solved
        ans = list(ans)
        ans.sort()
        return ans
