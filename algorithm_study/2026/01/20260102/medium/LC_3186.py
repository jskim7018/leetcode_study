from typing import List
from collections import Counter
from functools import cache


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)

        same_power_add = []

        for k, v in counter.items():
            same_power_add.append((k, k*v))

        n = len(same_power_add)
        same_power_add.sort()

        @cache
        def dp(idx: int) -> int:
            if idx >= n:
                return 0

            ret = dp(idx + 1)

            next_idx = idx + 1
            while next_idx < n and same_power_add[next_idx][0] <= same_power_add[idx][0] + 2:
                next_idx += 1
            ret = max(ret, dp(next_idx) + same_power_add[idx][1])

            return ret

        return dp(0)
