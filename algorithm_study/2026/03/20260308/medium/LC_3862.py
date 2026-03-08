import pytest


class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prod_suffix = [-1] * n

        for i in range(n-1, -1,-1):
            prod_suffix[i] = nums[i]
            if i + 1 < n:
                prod_suffix[i] *= prod_suffix[i+1]
            if prod_suffix[i] > 10**14:
                break

        left = 0

        for i in range(n):
            right = 1
            if i + 1 < n:
                right = prod_suffix[i+1]
            if left == right:
                return i
            left += nums[i]

        return -1


@pytest.mark.parametrize("input_nums, expected", [
    ([2,1,2], 1),
    ([2,8,2,2,5], 2),
    ([1], -1)
])
def test_smallestBalancedIndex(input_nums, expected):
    sol = Solution()

    assert sol.smallestBalancedIndex(input_nums) == expected