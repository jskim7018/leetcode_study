from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1

        curr_pos = n+m-1

        while curr_pos >= 0 and (j>=0):
            if i<0 and j>=0:
                while j>=0:
                    nums1[curr_pos] = nums2[j]
                    j-=1
                    curr_pos -= 1
            elif nums1[i] >= nums2[j]:
                nums1[curr_pos], nums1[i] = nums1[i], nums1[curr_pos]
                i-=1
            else:
                nums1[curr_pos] = nums2[j]
                j-=1

            curr_pos -= 1

        return nums1