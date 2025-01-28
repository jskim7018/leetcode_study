from typing import List
from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(10005)
        def dp(i) -> int:
            if i == n-1:
                return 0

            ret = float('inf')
            for jump in range(1, nums[i]+1):
                if jump + i < n:
                    ret = min(ret, 1 + dp(jump+i))
                else:
                    break
            return ret

        return dp(0)