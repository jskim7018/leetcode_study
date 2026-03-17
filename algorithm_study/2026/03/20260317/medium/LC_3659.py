from typing import List
from collections import defaultdict


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        # 1. len(nums) must be divisible by k
        # 2. max freq must be less than or equal to k
        n = len(nums)

        if n % k != 0:
            return False

        group_cnt = n//k
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > group_cnt:
                return False

        return True
