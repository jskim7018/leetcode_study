from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_loc = dict()

        ans = float('inf')
        for i, card in enumerate(cards):
            if card in last_loc:
                ans = min(ans, i - last_loc[card] + 1)
            last_loc[card] = i

        if ans == float('inf'):
            return -1
        else:
            return ans
