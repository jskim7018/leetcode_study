from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        total_xor = 0
        if len(nums2)%2==1:
            for num in nums1:
                total_xor ^= num
        if len(nums1)%2==1:
            for num in nums2:
                total_xor ^= num

        return total_xor
