from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        minim_diff = float('inf')
        for n1, n2 in zip(nums1, nums2):
            ans += abs(n1-n2)
            if (n1 <= nums2[-1] <= n2 or
                n2 <= nums2[-1] <= n1):
                minim_diff = 1
            else:
                minim_diff = min(minim_diff,
                                 abs(n1 - nums2[-1]) + 1,
                                 abs(n2 - nums2[-1]) + 1)

        return ans + minim_diff
