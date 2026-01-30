from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        possible_combs = [0] * (amount+1)
        possible_combs[0] = 1
        for c in coins:
            if c > amount:
                break
            for i in range(c, len(possible_combs)):
                possible_combs[i] += possible_combs[i - c]

        return possible_combs[amount]
