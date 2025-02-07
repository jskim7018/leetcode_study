from typing import List
from itertools import pairwise

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if all(x<y for x,y in pairwise(nums[:i] + nums[j+1:])):
                    ans += 1

        return ans


