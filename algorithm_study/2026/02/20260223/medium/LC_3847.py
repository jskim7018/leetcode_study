from typing import List
import pytest


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player1 = 0
        player2 = 0

        is_p1_active = True

        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 1:
                is_p1_active = not is_p1_active
            if (i+1) % 6 == 0:
                is_p1_active = not is_p1_active

            if is_p1_active:
                player1 += nums[i]
            else:
                player2 += nums[i]

        return player1 - player2


@pytest.mark.parametrize("nums_input, expected", [
    ([1,2,3], 0),
    ([2,4,2,1,2,1], 4),
    ([1], -1),
    ([2,2,2,2], 8),
    ([1,2,2,2], -7),
    ([2,2,2,2,2,10], 0)
])
def test_scoreDifference(nums_input, expected):
    sol = Solution()
    assert sol.scoreDifference(nums_input) == expected
