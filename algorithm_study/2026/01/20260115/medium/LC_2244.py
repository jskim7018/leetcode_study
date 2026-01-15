from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)

        ans = 0
        for k, v in counter.items():
            if v == 1:
                return -1
            elif v % 3 == 0:
                ans += v // 3
            else:
                ans += (v // 3 - 1) + 2

        return ans
