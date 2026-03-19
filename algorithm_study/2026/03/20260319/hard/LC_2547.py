from typing import List
from functools import cache


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # 분해 갯수와 cost는 비례한다. (k만큼)
        # unique value가 많을 수록 좋다. (즉, 분해를 많이하면 unique가 많아지기에 좋음.)
        # k가 n/2 보다 크면 무조건 전체 string 그대로 사용이 좋음.

        # 그리디하게 k를 사용하는 것이 이득인지 아닌지 판단?
        # 같은 크기까지 왔을때 쓰는게 좋은가 아니면 하나 더 작을때 쓰는게 좋은가?

        # 각 위치마다 2가지 선택지. 그냥 먹을건지 아니면 k를 쓰고 먹을건지.
        # num의 크기가 작아서 bitmap set 사용해서 dp 가능해보임.
        # dp[i][j] -> i -> 현재 num 위치, j -> bitmap set.
        n = len(nums)

        @cache
        def dp(idx: int, bitset_2: int, bitset_1: int) -> int:
            if idx >= n:
                return k

            num = nums[idx]

            bit_pos = 1 << num
            if (bitset_1 & bit_pos) == 0:
                ret = dp(idx + 1, bitset_2, bitset_1 | bit_pos)
            else:
                cost = 2
                if (bitset_2 & bit_pos) > 0:
                    cost = 1
                else:
                    bitset_2 |= bit_pos
                ret = min(dp(idx + 1, bitset_2, bitset_1) + cost,
                          dp(idx+1, 0, bit_pos) + k)

            return ret

        return dp(0, 0, 0)
