from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1 = sum(nums1)
        sum_2 = sum(nums2)

        nums1_zero_cnt = nums1.count(0)
        nums2_zero_cnt = nums2.count(0)

        if nums1_zero_cnt > 0 and nums2_zero_cnt > 0:
            return max(sum_1 + nums1_zero_cnt, sum_2+nums2_zero_cnt)
        elif nums1_zero_cnt == 0 and nums2_zero_cnt > 0:
            if sum_1 >= sum_2+nums2_zero_cnt:
                return sum_1
        elif nums1_zero_cnt > 0 and nums2_zero_cnt == 0:
            if sum_2 >= sum_1 + nums1_zero_cnt:
                return sum_2
        elif nums1_zero_cnt == 0 and nums2_zero_cnt == 0:
            if sum_1 == sum_2:
                return sum_1

        return -1
