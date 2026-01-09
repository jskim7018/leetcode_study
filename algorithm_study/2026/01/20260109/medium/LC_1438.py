from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        l = 0

        sorted_list = SortedList()
        ans = 0
        for r in range(n):
            sorted_list.add(nums[r])
            while l < r and sorted_list[-1] - sorted_list[0] > limit:
                sorted_list.remove(nums[l])
                l += 1
            ans = max(ans, len(sorted_list))
        return ans
