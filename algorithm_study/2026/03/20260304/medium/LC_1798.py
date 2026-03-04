from typing import List
import pytest


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        curr_high = 0

        for c in coins:
            if c > curr_high+1:
                break
            else:
                curr_high += c

        return curr_high + 1


@pytest.mark.parametrize("input_coins, expected", [
    ([1,3], 2),
    ([1,1,1,4], 8),
    ([1,4,10,3,1], 20),
    ([1], 2),
    ([5], 1)
])
def test_getMaximumConsecutive(input_coins, expected):
    sol = Solution()

    assert sol.getMaximumConsecutive(input_coins) == expected
