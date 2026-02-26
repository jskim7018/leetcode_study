from typing import List
import pytest


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # no need to delete positive.
        # 왼쪽 오른쪽 suffix, prefix max 구함.
        # TODO: no del, one del, 2가지 variable로 해결 가능.
        # 변형 kadane's algorithm problem
        n = len(arr)
        no_del = arr[0]
        one_del = float('-inf')

        ans = arr[0]
        for i in range(1, n):
            new_no_del = arr[i]
            if no_del > 0:
                new_no_del += no_del
            new_one_del = max(one_del + arr[i], no_del)

            no_del = new_no_del
            one_del = new_one_del

            ans = max(ans, no_del, one_del)

        return ans


@pytest.mark.parametrize("input_arr, expected", [
    ([1,-2,0,3], 4),
    ([1,-2,-2,3], 3),
    ([-1,-1,-1,-1], -1),
    ([-50], -50)
])
def test_maximumSum(input_arr, expected):
    sol = Solution()
    assert sol.maximumSum(input_arr) == expected
