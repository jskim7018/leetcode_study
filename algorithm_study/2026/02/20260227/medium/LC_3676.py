from typing import List
import pytest


class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        # decreasing stack. bowl의 오른쪽은 항상 더 작아야 함.
        # binary search to find left most same or smaller.
        n = len(nums)
        decr_stck = []
        ans = 0
        for i in range(n):
            cnt = 0
            while decr_stck and decr_stck[-1] <= nums[i]:
                if len(decr_stck) >= 2:
                    cnt += 1
                decr_stck.pop()
            ans += cnt

            decr_stck.append(nums[i])

        return ans


@pytest.mark.parametrize("input_nums, expected", [
    ([2,5,3,1,4], 2),
    ([5,1,2,3,4], 3),
    ([1000000000,999999999,999999998], 0)
])
def test_bowlSubarrays(input_nums, expected):
    sol = Solution()
    assert sol.bowlSubarrays(input_nums) == expected
