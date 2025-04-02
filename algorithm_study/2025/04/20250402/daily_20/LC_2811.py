from typing import List
from itertools import accumulate
from functools import cache


# TODO: Check optimized solution
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)

        prefix_sum = list(accumulate(nums))

        @cache
        def solve(i, j) -> bool:
            if i == j:
                return True
            sum_ = prefix_sum[j]
            if i-1 >= 0:
                sum_ -= prefix_sum[i-1]
            if sum_ < m and not (i == 0 and j == n-1):
                return False
            ret = False
            for k in range(i+1,j+1):
                ret |= solve(i, k-1) and solve(k,j)
            return ret

        ans = solve(0, n-1)
        solve.cache_clear()

        return ans
