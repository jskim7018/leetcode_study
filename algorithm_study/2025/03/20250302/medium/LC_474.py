from typing import List
from functools import cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        bits_cnt = [(str.count('0'),str.count('1')) for str in strs]

        @cache
        def dp(idx, m, n) -> int:
            if idx >= len(bits_cnt):
                return 0

            ret = dp(idx+1, m, n)
            if m-bits_cnt[idx][0] >= 0 and n-bits_cnt[idx][1] >= 0:
                ret = max(ret, dp(idx+1, m-bits_cnt[idx][0], n-bits_cnt[idx][1])+1)
            return ret

        return dp(0, m, n)