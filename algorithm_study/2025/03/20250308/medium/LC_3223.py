from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)

        ans = 0
        for v in counter.values():
            if v % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans
