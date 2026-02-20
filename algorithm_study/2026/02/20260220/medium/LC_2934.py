from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # 필수 swap 대상 구하고
        # 그대로일때 필수 swap 구함. 바꿨을때와 비교 후 min 반환
        n = len(nums1)
        max1 = nums1[n-1]
        max2 = nums2[n-1]

        swap_cnt = 0
        swap_n = n-1
        for i in range(n-1):
            if (max1 >= nums1[i] and max2 >= nums2[i] and
                max1 >= nums2[i] and max2 >= nums1[i]):
                swap_n -= 1
            elif max1 >= nums1[i] and max2 >= nums2[i]:
                continue
            elif max1 >= nums2[i] and max2 >= nums1[i]:
                swap_cnt += 1
            else:
                return -1
        print(swap_cnt)
        return min(swap_cnt, swap_n-swap_cnt+1)
