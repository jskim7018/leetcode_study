from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        num_to_indexes = defaultdict(list)

        for i, num in enumerate(nums):
            num_to_indexes[num].append(i)
        ans = float('inf')
        for indexes in num_to_indexes.values():
            for i in range(2, len(indexes)):
                ans = min(ans, abs(indexes[i-2]-indexes[i]) * 2)
        if ans == float('inf'):
            return -1
        else:
            return ans
