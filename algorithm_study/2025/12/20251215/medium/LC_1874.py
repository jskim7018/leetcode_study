from typing import List


# This is a classic greedy + rearrangement inequality problem.
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)

        ans = 0
        for i in range(len(nums1)):
            ans += nums1[i] * nums2[i]
        #return sum(a * b for a, b in zip(nums1, nums2))

        return ans

