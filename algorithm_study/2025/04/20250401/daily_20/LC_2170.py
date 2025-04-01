from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        evens_arr = [nums[i] for i in range(0,n,2)]
        odd_arr = [nums[i] for i in range(1,n,2)]
        cntr_even_pos = Counter(evens_arr)
        cntr_odd_pos = Counter(odd_arr)

        even_pos = cntr_even_pos.most_common(2)
        odd_pos = cntr_odd_pos.most_common(2)

        even_n = len(evens_arr)
        odd_n = len(odd_arr)

        ret = min(even_n, odd_n)
        if len(even_pos) >= 1 and len(odd_pos) >= 1 and even_pos[0][0] != odd_pos[0][0]:
            ret = even_n-even_pos[0][1] + odd_n-odd_pos[0][1]
        else:
            if len(odd_pos) >= 2:
                ret = even_n-even_pos[0][1] + odd_n-odd_pos[1][1]
            if len(even_pos) >= 2:
                ret = min(ret, even_n-even_pos[1][1] + odd_n-odd_pos[0][1])
        return ret

