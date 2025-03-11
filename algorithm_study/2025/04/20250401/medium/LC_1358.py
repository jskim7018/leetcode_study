from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        counter = Counter()
        r = 0

        ans = 0
        for i in range(n):

            if i > 0:
                counter[s[i-1]] -= 1
                if counter[s[i-1]] == 0:
                    del counter[s[i-1]]

            while len(counter) < 3 and r < n:
                counter[s[r]] += 1
                r += 1

            if len(counter) >= 3:
                ans += n-r+1

        return ans
