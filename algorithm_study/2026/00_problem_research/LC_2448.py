from typing import List
import pytest


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Convex (U - shaped function) 하게 total cost가 형성됨. binary search move toward decreasing
        # TODO: try solving with median way.
        def get_total_cost(target: int):
            ret = 0
            for i, num in enumerate(nums):
                diff = abs(num - target)
                ret += cost[i] * diff
            return ret

        l, r = min(nums), max(nums)
        ans = float('inf')
        while l <= r:
            mid = (l+r)//2
            curr_total_cost = get_total_cost(mid)
            right_total_cost = get_total_cost(mid + 1)
            ans = min(ans, curr_total_cost)
            if right_total_cost < curr_total_cost:
                l = mid + 1
            else:
                r = mid - 1
        return ans


@pytest.mark.parametrize("input_nums, input_cost, expected", [
    ([1,3,5,2], [2,3,1,14], 8),
    ([2,2,2,2,2],[4,2,8,1,3],0),
    ([5],[10],0),
    ([5,10,14],[1,2,2],13)
])
def test_minCost(input_nums, input_cost, expected):
    sol = Solution()
    assert sol.minCost(input_nums, input_cost) == expected
