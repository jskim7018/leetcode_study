from typing import List
import bisect
import pytest


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        # monotonic strict incr stck + binary search
        # TODO: binary search도 필요 없이 가능.
        incr_stck = []
        n = len(nums)

        ans = 0
        for i in range(n):
            bigger_idx = bisect.bisect_right(incr_stck, (nums[i], i))
            if bigger_idx < len(incr_stck):
                ans = max(ans, i - incr_stck[bigger_idx][1] + 1)
            else:
                if not incr_stck or incr_stck[-1][0] != nums[i]:
                    incr_stck.append((nums[i], i))

        return ans


@pytest.mark.parametrize("input_nums, expected", [
    ([7,6,5,4,3,2,1,6,10,11], 8),
    ([57,55,50,60,61,58,63,59,64,60,63], 6),
    ([1,2,3,4], 0),
    ([5,1], 2),
    ([8,6,4,2,1,5,10], 6),
    ([5], 0)
])
def test_maxSubarrayLength(input_nums, expected):
    sol = Solution()
    assert sol.maxSubarrayLength(input_nums) == expected

