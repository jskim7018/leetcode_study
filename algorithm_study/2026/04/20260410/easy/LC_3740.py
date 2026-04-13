from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        num_to_indexes = defaultdict(list)

        minim = float('inf')
        for i, num in enumerate(nums):
            num_to_indexes[num].append(i)

            if len(num_to_indexes[num]) >= 3:
                a = num_to_indexes[num][-1]
                b = num_to_indexes[num][-2]
                c = num_to_indexes[num][-3]
                minim = min(minim, abs(a-b) + abs(b-c) + abs(a-c))

        if minim == float('inf'):
            return -1
        else:
            return minim
