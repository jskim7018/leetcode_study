from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        curr_possible_up_to = 0
        ans = 0
        for c in coins:
            if curr_possible_up_to >= target:
                break
            while c > curr_possible_up_to+1:
                curr_possible_up_to += curr_possible_up_to + 1
                ans += 1
            curr_possible_up_to += c

        while curr_possible_up_to < target:
            curr_possible_up_to += curr_possible_up_to + 1
            ans += 1

        return ans
