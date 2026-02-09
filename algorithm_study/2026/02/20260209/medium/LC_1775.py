from typing import List
from collections import defaultdict
import math


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # greedy
        # TODO: 'gain' 이라는 데이터를 중점으로 하면 더 깔끔해질 수 있음.
        nums1_idx = 0
        nums2_idx = 0

        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)
        diff = abs(nums1_sum - nums2_sum)

        nums1_counter = defaultdict(int)
        nums2_counter = defaultdict(int)

        for num in nums1:
            nums1_counter[num] += 1
        for num in nums2:
            nums2_counter[num] += 1
        freq_nums1 = list(nums1_counter.items())
        freq_nums2 = list(nums2_counter.items())

        if diff == 0:
            return 0
        elif nums1_sum < nums2_sum:
            freq_nums1, freq_nums2 = freq_nums2, freq_nums1

        n1 = len(freq_nums1)
        n2 = len(freq_nums2)
        freq_nums1.sort(reverse=True)
        freq_nums2.sort()

        ops_cnt = 0
        while diff > 0:
            nums1_poss = 0
            nums2_poss = 0
            if nums1_idx < n1:
                nums1_poss = freq_nums1[nums1_idx][0] - 1
            if nums2_idx < n2:
                nums2_poss = 6 - freq_nums2[nums2_idx][0]

            if nums1_poss == 0 and nums2_poss == 0:
                return -1
            elif nums1_poss >= nums2_poss:
                if nums1_poss * freq_nums1[nums1_idx][1] >= diff:
                    ops_cnt += math.ceil(diff / nums1_poss)
                else:
                    ops_cnt += freq_nums1[nums1_idx][1]
                diff -= nums1_poss * freq_nums1[nums1_idx][1]
                nums1_idx += 1
            elif nums1_poss < nums2_poss:
                if nums2_poss * freq_nums2[nums2_idx][1] >= diff:
                    ops_cnt += math.ceil(diff / nums2_poss)
                else:
                    ops_cnt += freq_nums2[nums2_idx][1]
                diff -= nums2_poss * freq_nums2[nums2_idx][1]
                nums2_idx += 1

        return ops_cnt
