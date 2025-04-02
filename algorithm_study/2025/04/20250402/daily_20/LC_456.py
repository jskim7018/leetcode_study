from typing import List
from sortedcontainers import SortedList


# TODO: Check optimized solution. Study bisect left and right thoroughly.
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)

        sorted_list = SortedList()

        for i in range(1,n):
            sorted_list.add(nums[i])

        minim = float('inf')
        for i in range(1,n-1):
            minim = min(minim, nums[i-1])
            sorted_list.remove(nums[i])
            if minim < nums[i]:
                r = sorted_list.bisect_right(nums[i]-1)-1
                if r >= 0:
                    if sorted_list[r] < nums[i] and sorted_list[r] > minim:
                        return True
        return False
