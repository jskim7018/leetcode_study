from typing import List
import pytest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sliding window, 최초 negative를 까지의 product를 나눈다.
        n = len(nums)

        curr_prod = 1
        ans = max(nums)
        first_neg_prod = 0
        for r in range(n):
            ans = max(ans, nums[r])
            if nums[r] == 0:
                curr_prod = 1
                first_neg_prod = 0
                continue
            curr_prod *= nums[r]
            if curr_prod < 0:
                if first_neg_prod == 0:
                    first_neg_prod = curr_prod
                if curr_prod != first_neg_prod:
                    ans = max(ans, curr_prod//first_neg_prod)
            else:
                ans = max(ans, curr_prod)
        return ans


@pytest.mark.parametrize("input_nums, expected", [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
])
def test_maxProoduct(input_nums, expected):
    sol = Solution()

    assert sol.maxProduct(input_nums) == expected