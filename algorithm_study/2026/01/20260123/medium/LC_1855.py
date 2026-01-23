from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        n2_idx = 0

        ans = 0
        for i in range(n1):
            while n2_idx < n2 and (nums2[n2_idx] >= nums1[i] or n2_idx < i):
                n2_idx += 1
            if nums1[i] <= nums2[n2_idx-1]:
                ans = max(ans, (n2_idx-1) - i)

        return ans
