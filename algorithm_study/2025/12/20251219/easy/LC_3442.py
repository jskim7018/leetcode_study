from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)

        max_odd_freq = 0
        min_even_freq = float('inf')

        for v in counter.values():
            if v % 2 == 0:
                min_even_freq = min(min_even_freq, v)
            else:
                max_odd_freq = max(max_odd_freq, v)

        return max_odd_freq - min_even_freq
