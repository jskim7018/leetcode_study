from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        n = len(s)
        l = 0
        ans = 0
        for r in range(n):
            counter[s[r]] += 1
            while len(counter) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            ans = max(ans, r-l + 1)

        return ans
