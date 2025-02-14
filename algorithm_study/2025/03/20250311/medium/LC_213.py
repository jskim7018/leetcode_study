from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(idx, isFirstRobbed) -> int:
            if idx >= n:
                return 0

            ret = 0
            if not (isFirstRobbed and idx == n - 1):
                ret = dp(idx + 2, isFirstRobbed or idx == 0) + nums[idx]

            ret = max(ret, dp(idx+1, isFirstRobbed))

            return ret

        return dp(0, False)
