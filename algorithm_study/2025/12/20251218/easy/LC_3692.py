from collections import Counter


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter = Counter(s)
        counter_f = Counter()

        for v, f in counter.items():
            counter_f[f] += 1

        maxim = 0
        maxim_f = 0
        for f, f2 in counter_f.items():
            if f2 > maxim:
                maxim = f2
                maxim_f = f
            elif f2 == maxim and f > maxim_f:
                maxim = f2
                maxim_f = f

        ans = ''
        for v, f in counter.items():
            if maxim_f == f:
                ans += v

        return ans
