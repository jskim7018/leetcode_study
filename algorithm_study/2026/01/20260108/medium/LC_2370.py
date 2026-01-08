from collections import defaultdict
import bisect
from functools import cache


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        alph_indexes = defaultdict(list)

        for i, ch in enumerate(s):
            alph_indexes[ord(ch) - ord('a')].append(i)

        @cache
        def dp(idx: int) -> int:
            ret = 1
            ch_ord = ord(s[idx]) - ord('a')

            for new_alph in range(max(ch_ord-k, 0), min(ch_ord+k, 25) + 1):
                if new_alph in alph_indexes:
                    next_idx = bisect.bisect_left(alph_indexes[new_alph], idx+1)
                    if next_idx < len(alph_indexes[new_alph]):
                        ret = max(ret, dp(alph_indexes[new_alph][next_idx])+1)
            return ret

        ans = 0
        for indexes in alph_indexes.values():
            ans = max(ans, dp(indexes[0]))

        return ans
