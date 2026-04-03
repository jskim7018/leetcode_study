from functools import cache


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        # 완탐 가능해 보임.
        # Time complexity 계산으로 정확히 증명 할 수 있어야 함.

        n = len(s)

        # Precompute power of 5
        pow_of_5 = set()
        curr = 1
        pow_of_5.add(curr)
        while curr <= pow(2, 15):
            curr *= 5
            pow_of_5.add(curr)

        @cache
        def dp(idx: int):
            if idx >= n:
                return 0
            if s[idx] == '0':
                return float('inf')

            ret = float('inf')
            curr = 0
            for i in range(idx, n):
                curr = curr << 1
                if s[i] == '1':
                    curr += 1
                if curr in pow_of_5:
                    ret = min(ret, dp(i+1) + 1)
            return ret

        ans = dp(0)
        if ans == float('inf'):
            return -1
        else:
            return dp(0)
