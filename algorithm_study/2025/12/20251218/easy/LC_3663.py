from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counter = Counter()

        _min = float('inf')
        _min_v = float('inf')
        while n > 0:
            digit = n%10
            counter[digit] += 1

            n //= 10

        for v, f in counter.items():
            if f < _min:
                _min = f
                _min_v = v
            elif f == _min and \
                v < _min_v:
                _min_v = v

        return _min_v
