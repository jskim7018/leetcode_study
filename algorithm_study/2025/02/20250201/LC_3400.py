from typing import List


class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:

        def get_matching_cnt(nums1, nums2) -> int:
            cnt = 0
            for num1, num2 in zip(nums1, nums2):
                if num1 == num2:
                    cnt += 1

            return cnt

        ans = 0
        for i in range(len(nums1)):
            new_nums1 = nums1[i:len(nums1)] + nums1[0:i]
            ans = max(ans, get_matching_cnt(new_nums1, nums2))

        return ans
