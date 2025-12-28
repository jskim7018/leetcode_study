from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)

        ans = 0
        for i in range(0, 26):
            alph = chr(ord('a')+i)
            ans += abs(counter_s[alph] - counter_t[alph])

        return ans
