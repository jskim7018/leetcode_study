from typing import List
import pytest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sliding window, 최초 negative를 까지의 product를 나눈다.
        if not nums:
            return 0

        curr_max = curr_min = result = nums[0]

        for num in nums[1:]:
            temp_max = max(num, num * curr_max, num * curr_min)
            curr_min = min(num, num * curr_max, num * curr_min)
            curr_max = temp_max
            result = max(result, curr_max)

        return result

@pytest.mark.parametrize("input_nums, expected", [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
])
def test_maxProoduct(input_nums, expected):
    sol = Solution()

    assert sol.maxProduct(input_nums) == expected