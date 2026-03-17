from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO: Need to try solving in O(log (m+n)).

        nums = nums1 + nums2

        nums.sort()

        n = len(nums)

        if n % 2 == 1:
            return nums[n//2]
        else:
            return (nums[n//2-1] + nums[n//2])/2.0
