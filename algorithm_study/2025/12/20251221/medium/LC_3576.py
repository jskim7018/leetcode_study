from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def canMakeEqualTo(nums: List[int], to: int, k: int) -> bool:
            curr_idx = 0
            while curr_idx + 1 < n:
                if nums[curr_idx] != to:
                    nums[curr_idx] *= -1
                    nums[curr_idx+1] *= -1
                    k -= 1
                    if k == 0:
                        break
                curr_idx += 1
            for i in range(curr_idx, n):
                if nums[i] != to:
                    return False
            return True

        return canMakeEqualTo(list(nums),1,k) or canMakeEqualTo(list(nums),-1,k)
