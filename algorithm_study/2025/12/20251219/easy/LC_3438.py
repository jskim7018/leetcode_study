from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)

        for i in range(1, n):
            if s[i-1] != s[i] and counter[s[i-1]] == int(s[i-1])\
                    and counter[s[i]] == int(s[i]):
                return s[i-1:i+1]
        return ""
