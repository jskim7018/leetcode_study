from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1

        nums.append(k)
        st = set(nums)

        return len(st)-1
