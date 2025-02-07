from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        i = j = 0

        counter = Counter()
        counter[s[i]] = 1
        while j < len(s): # two pointer
            for val in counter.values():
                if val > 2:
                    counter[s[i]] -= 1
                    i += 1
                    break
            else:
                ans = max(ans, j - i + 1)
                j += 1
                if j < len(s):
                    counter[s[j]] += 1

        return ans
