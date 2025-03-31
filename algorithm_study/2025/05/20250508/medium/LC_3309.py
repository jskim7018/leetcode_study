from functools import cache
from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = Counter(s)

        @cache
        def get_substring_cnt(n):
            if n == 0:
                return 0
            return get_substring_cnt(n-1) + n

        ans = 0
        for v in counter.values():
            ans += get_substring_cnt(v)

        return ans
