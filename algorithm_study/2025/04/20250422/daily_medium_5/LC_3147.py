from typing import List
from functools import lru_cache

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        @lru_cache(maxsize=None)
        def solve(idx: int) -> int:
            if idx >= n:
                return 0
            ret = solve(idx + k) + energy[idx]

            return ret

        ans = float('-inf')

        for i in range(n):
            ans = max(ans, solve(i))

        return ans
