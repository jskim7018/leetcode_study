from collections import Counter


class Solution:
    def maxSameLengthRuns(self, s: str) -> int:
        counter = Counter()
        s += '-'
        maxim = 0
        cnt = 1
        for i in range(len(s[1:])):
            if s[i-1] == s[i]:
                cnt += 1
            else:
                counter[cnt] += 1
                maxim = max(maxim, counter[cnt])
                cnt = 1

        return maxim
