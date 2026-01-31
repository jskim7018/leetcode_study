from collections import defaultdict


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        # sliding window/two-pointer
        l = 0
        counter = defaultdict(int)
        ans = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            sub_str_len = r-l+1
            ans += sub_str_len

        return ans
