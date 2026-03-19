from typing import List
import math


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        nums_sum = sum(nums)

        abs_diff = abs(nums_sum - goal)

        return math.ceil(abs_diff / limit)
