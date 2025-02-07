from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        can_go = 0

        i = 0
        while i < n:
            if i == n-1:
                return True
            can_go = max(can_go, nums[i])
            if can_go == 0:
                return False
            else:
                i += 1
                can_go -= 1

        return False
