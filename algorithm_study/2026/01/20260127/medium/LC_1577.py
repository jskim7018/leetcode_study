from typing import List
from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pair_mult_counter1 = defaultdict(int)
        pair_mult_counter2 = defaultdict(int)

        n1 = len(nums1)
        n2 = len(nums2)
        nums1.sort()
        nums2.sort()
        nums1_max_pair = nums1[-1]
        if len(nums1) > 1:
            nums1_max_pair *= nums1[-2]
        nums2_max_pair = nums2[-1]
        if len(nums2) > 1:
            nums2_max_pair *= nums2[-2]

        for i in range(n1):
            for j in range(i+1, n1):
                pair_mult_counter1[nums1[i] * nums1[j]] += 1

        for i in range(n2):
            for j in range(i+1, n2):
                pair_mult_counter2[nums2[i] * nums2[j]] += 1

        ans = 0
        for i in range(n1):
            sqrd = nums1[i] ** 2
            if sqrd > nums2_max_pair:
                break
            ans += pair_mult_counter2[nums1[i] ** 2]
        for i in range(n2):
            sqrd = nums2[i] ** 2
            if sqrd > nums1_max_pair:
                break
            ans += pair_mult_counter1[nums2[i] ** 2]

        return ans
