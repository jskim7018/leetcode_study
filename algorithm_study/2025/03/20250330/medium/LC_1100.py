from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)

        if n < k:
            return 0

        ans = 0

        cntr = Counter()
        for i in range(k):
            cntr[s[i]] += 1

        if len(cntr) == k:
            ans += 1

        for i in range(k,n):
            cntr[s[i-k]] -= 1
            if cntr[s[i-k]] == 0:
                del cntr[s[i-k]]
            cntr[s[i]] += 1
            if len(cntr) == k:
                ans += 1
        return ans
