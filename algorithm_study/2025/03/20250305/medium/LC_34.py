from typing import List
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1]

        return [-1,-1]