from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        counter2 = Counter(s)
        counter1 = Counter()
        ans = 0
        for i in range(0, len(s)-1):
            counter1[s[i]] += 1
            counter2[s[i]] -= 1
            if counter2[s[i]] == 0:
                del counter2[s[i]]

            if len(counter1) == len(counter2):
               ans += 1
        return ans
