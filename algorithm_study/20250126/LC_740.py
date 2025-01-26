from typing import List
from collections import Counter
from functools import cache


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        c_nums = Counter(nums)
        new_nums = list(c_nums.items())
        new_nums = [(a[0], a[0]*a[1])for a in new_nums]
        n = len(new_nums)

        @cache
        def dp(i) -> int:
            if i >= n:
                return 0

            # not take current value
            ret = dp(i+1)

            # take current
            for next in range(i+1, n+1):
                if next >= n or new_nums[next][0] != new_nums[i][0] + 1:
                    ret = max(ret, new_nums[i][1] + dp(next))
            return ret
        return dp(0)
