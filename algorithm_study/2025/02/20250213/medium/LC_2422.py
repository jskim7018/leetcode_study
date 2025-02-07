from typing import List
from collections import deque


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        ans = 0
        while l<r:
            if nums[l] > nums[r]:
                nums[r-1] += nums[r]
                r-=1
                ans += 1
            elif nums[l] < nums[r]:
                nums[l+1] += nums[l]
                l+=1
                ans += 1
            else:
                l+=1
                r-=1
        return ans
