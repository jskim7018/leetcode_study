from typing import List
from sortedcontainers import SortedList
import pytest


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # dp[i][j] -> i까지 했을떄 최대. j가 max(rewardValues)를 넘어가면 멈춰도 됨.
        n = len(rewardValues)
        maxim = max(rewardValues)
        rewardValues.sort()

        st = SortedList()
        st.add(0)
        ans = 0
        for i in range(n):
            new_st = SortedList(st)
            for e in st:
                if e < rewardValues[i]:
                    next_val = e + rewardValues[i]
                    if next_val < maxim:
                        new_st.add(next_val)
                    ans = max(ans, next_val)
                else:
                    break
            st = new_st
        return ans


@pytest.mark.parametrize("input_rewardValues, expected",[
    ([1,1,3,3], 4),
    ([1,6,4,3,2], 11)
])
def test_maxTotalReward(input_rewardValues, expected):
    sol = Solution()
    assert sol.maxTotalReward(input_rewardValues) == expected
