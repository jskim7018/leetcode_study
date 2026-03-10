from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        n = len(s)

        counter = defaultdict(int)

        l = 0
        ans = 0
        for r in range(n):
            counter[s[r]] += 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans
