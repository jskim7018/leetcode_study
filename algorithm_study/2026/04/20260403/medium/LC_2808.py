from typing import List
from collections import defaultdict


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        max_gaps = defaultdict(int)
        last_idx = dict()
        first_idx = dict()

        n = len(nums)
        nums_st = set()

        for i, num in enumerate(nums):
            nums_st.add(num)
            if num not in first_idx:
                first_idx[num] = i
                last_idx[num] = i
                continue

            gap = i - last_idx[num] - 1
            max_gaps[num] = max(max_gaps[num], gap//2 + gap % 2)

            last_idx[num] = i

        minim = float('inf')
        for k in nums_st:
            wrap_gap = first_idx[k] + n-last_idx[k]-1
            max_gaps[k] = max(max_gaps[k], wrap_gap//2 + wrap_gap % 2)
            minim = min(minim, max_gaps[k])

        return minim
