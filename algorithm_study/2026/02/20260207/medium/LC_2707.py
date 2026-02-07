from typing import List
from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        @cache
        def dp(idx: int) -> int:
            if idx >= n:
                return 0

            ret = dp(idx + 1) + 1
            for d in dictionary:
                is_start_d = s.startswith(d, idx)
                if is_start_d:
                    ret = min(ret, dp(idx + len(d)))
            return ret

        return dp(0)
