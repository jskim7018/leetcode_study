from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        minim = float('inf')
        for start_idx in range(3):
            nums1_idx = start_idx
            nums2_idx = 0
            diff = nums2[nums2_idx] - nums1[nums1_idx]
            delete = 0
            del_limit = 2-start_idx
            isPossible = False
            while nums2_idx < len(nums2):
                if nums2[nums2_idx] - nums1[nums1_idx] == diff:
                    nums2_idx += 1
                    nums1_idx += 1
                else:
                    delete += 1
                    nums1_idx += 1
                    if delete > del_limit:
                        break
                if nums2_idx >= len(nums2):
                    isPossible = True
                    break

            if isPossible:
                minim = min(minim, nums2[0] - nums1[start_idx])
        return minim
