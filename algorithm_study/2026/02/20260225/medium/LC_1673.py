from typing import List
import pytest


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # 가장 min 가능하다면 순서대로 넣는다.
        # 왼쪽에서 순서대로 한다. 별도로 정렬해둬서 curr_min_idx로 현재 min 가리킨다.
        # 만약 현재 min이면 바로 넣는다.
        # 현재 min이 아닐때는 min을 유지한다. 그러다가 넣어야 할때 (사이즈 문제)생기면 넣는다.
        # montonic incr stack 사용? 만약 빼도 되면 빼고 넣는다.
        n = len(nums)

        incr_stck = []
        for i in range(n):
            max_poss_len = len(incr_stck) + n-i

            if max_poss_len != k:
                while max_poss_len > k and incr_stck and incr_stck[-1] > nums[i]:
                    incr_stck.pop()
                    max_poss_len = len(incr_stck) + n - i
            if len(incr_stck) < k:
                incr_stck.append(nums[i])

        return incr_stck


@pytest.mark.parametrize("input_nums, input_k, expected", [
    ([3,5,2,6], 2, [2,6]),
    ([2,4,3,3,5,4,9,6], 4, [2,3,3,4]),
    ([1], 1, [1]),
    ([5,6,3,2], 3, [5,3,2])
])
def test_mostCompetitive(input_nums, input_k, expected):
    sol = Solution()
    assert sol.mostCompetitive(input_nums, input_k) == expected
