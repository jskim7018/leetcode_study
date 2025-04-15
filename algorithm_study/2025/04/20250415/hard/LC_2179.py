from typing import List
from sortedcontainers import SortedList


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_to_idx = dict()

        sorted_list = SortedList()
        for i, v in enumerate(nums2):
            nums2_to_idx[v] = i

        ans = 0
        number_to_cnt = dict()
        for v in nums1[::-1]:
            idx2 = nums2_to_idx[v]
            sorted_list.add(idx2)

            right_cnt = len(sorted_list) - sorted_list.bisect_left(idx2) - 1
            number_to_cnt[v] = right_cnt

        sorted_list.clear()
        for num in nums1:
            idx2 = nums2_to_idx[num]
            sorted_list.add(idx2)
            left_cnt = sorted_list.bisect_left(idx2)
            ans += number_to_cnt[num] * left_cnt

        return ans
