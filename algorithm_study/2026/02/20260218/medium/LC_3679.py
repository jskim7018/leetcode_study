from typing import List
from collections import defaultdict


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        counter = defaultdict(int)
        curr_used = set()

        ans = 0
        for i, ar in enumerate(arrivals):
            window_left = i-w
            if window_left >= 0:
                if window_left in curr_used:
                    counter[arrivals[window_left]] -= 1
                    curr_used.remove(window_left)

            if counter[ar] < m:
                counter[ar] += 1
                curr_used.add(i)
            else:
                ans += 1

        return ans
