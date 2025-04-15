from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)

        counter = defaultdict(int)
        l = 0
        ans = 0
        for r in range(n):
            counter[s[r]] += 1
            while len(counter) > 2:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            ans = max(ans, r-l+1)

        return ans
