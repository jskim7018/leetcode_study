from typing import List
from functools import cache


class Solution:

    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def set_bit_cnt(num: int) -> int:
            ret = 0
            while num > 0:
                ret += num % 2
                num //= 2
            return ret

        nums_with_idx = [(num, i) for i, num in enumerate(nums)]

        nums_with_idx.sort()

        curr_set_bit = set_bit_cnt(nums_with_idx[0][0])
        same_idx_st = {nums_with_idx[0][1]}
        same_sorted_idx_st = {0}
        for i in range(1, n):
            if set_bit_cnt(nums_with_idx[i][0]) == curr_set_bit:
                same_idx_st.add(nums_with_idx[i][1])
                same_sorted_idx_st.add(i)
            else:
                if same_sorted_idx_st != same_idx_st:
                    return False
                same_idx_st.clear()
                same_sorted_idx_st.clear()
                same_idx_st = {nums_with_idx[i][1]}
                same_sorted_idx_st = {i}
                curr_set_bit = set_bit_cnt(nums_with_idx[i][0])

        if same_sorted_idx_st != same_sorted_idx_st:
            return False

        return True
