from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            for i in range(len(nums1)):
                if nums1[i] != nums2[i]:
                    return -1
            return 0

        if sum(nums1) != sum(nums2):
            return -1

        ans = 0
        for i in range(len(nums1)):
            if nums1[i] % k != nums2[i] % k:
                return -1

            if nums1[i] < nums2[i]:
                ans += (nums2[i] - nums1[i]) // k

        return ans
