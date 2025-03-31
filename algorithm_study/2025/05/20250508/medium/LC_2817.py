from typing import List
from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sorted_list = SortedList(nums)

        ans = float('inf')
        for i in range(x):
            sorted_list.remove(nums[i])
        for i in range(n-x):
            idx = sorted_list.bisect_left(nums[i])
            if idx <len(sorted_list):
               ans = min(ans, abs(nums[i] - sorted_list[idx]))
            if idx-1 >= 0:
                ans = min(ans, abs(nums[i] - sorted_list[idx-1]))
            sorted_list.remove(nums[i+x])

        return ans
