from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 51
        is_available = False
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                or_sum = 0
                for x in range(i, j+1):
                    or_sum |= nums[x]
                    if or_sum >= k:
                        ans = min(ans, j-i+1)
                        is_available = True
        if is_available:
            return ans
        else:
            return -1
