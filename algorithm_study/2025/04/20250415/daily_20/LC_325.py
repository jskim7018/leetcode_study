from typing import List
from itertools import accumulate

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        val_to_idx = dict()

        prefix_sum = list(accumulate(nums))

        maxim = 0
        val_to_idx[0] = -1
        for i in range(len(nums)):
            v_to_find = prefix_sum[i]-k
            if v_to_find in val_to_idx:
                maxim = max(maxim, i-val_to_idx[v_to_find])
            if prefix_sum[i] not in val_to_idx:
                val_to_idx[prefix_sum[i]] = i

        return maxim
