from collections import Counter
from functools import cache


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        @cache
        def solve(idx) -> int:
            if idx >= n:
                return 0

            ret = float('inf')
            counter = Counter()
            for i in range(idx, n):
                counter[s[i]] += 1
                if len(set(counter.values())) == 1:
                    ret = min(ret, solve(i+1) + 1)

            return ret

        return solve(0)
