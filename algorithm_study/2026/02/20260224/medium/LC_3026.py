from typing import List
import pytest


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # 같은거 왔을때 만약 사이가 positive면 그대로 둠. 아니면 현재 idx로 교체
        num_to_prev_prefix_sum = dict()
        prefix_sum = 0
        ans = float('-inf')
        for num in nums:
            # update
            if num not in num_to_prev_prefix_sum:
                num_to_prev_prefix_sum[num] = prefix_sum
            else:
                num_to_prev_prefix_sum[num] = min(num_to_prev_prefix_sum[num], prefix_sum)

            # check
            if num - k in num_to_prev_prefix_sum:
                ans = max(ans, prefix_sum + num - num_to_prev_prefix_sum[num-k])
            if num + k in num_to_prev_prefix_sum:
                ans = max(ans, prefix_sum + num - num_to_prev_prefix_sum[num + k])

            prefix_sum += num
        if ans == float('-inf'):
            return 0
        else:
            return ans


@pytest.mark.parametrize("input_nums, input_k, expected", [
    ([1,2,3,4,5,6], 1, 11),
    ([-1,3,2,4,5], 3, 11),
    ([-1,-2,-3,-4], 2, -6),
    ([1,1,6,2,-7,2], 1, 10),
    ([1,5], 2, 0)
])
def test_maximumSubarraySum(input_nums, input_k, expected):
    sol = Solution()
    assert sol.maximumSubarraySum(input_nums, input_k) == expected
