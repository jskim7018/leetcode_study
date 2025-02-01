from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        n = len(s)
        l = 0

        counter = Counter()
        for r in range(n):
            counter[s[r]] += 1
            while l < r and counter[s[r]] > 1:
                counter[s[l]] -= 1
                if counter[s[l]] <= 0:
                    del counter[s[l]]
                l += 1
            ans = max(ans, len(counter))

        return ans
