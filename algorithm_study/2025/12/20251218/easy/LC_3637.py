from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        slope_changes = []
        curr_slope = ''
        for i in range(1, n):
            if nums[i] > nums[i-1] and curr_slope != 'i':
                slope_changes.append('i')
                curr_slope = 'i'
            elif nums[i] < nums[i-1] and curr_slope != 'd':
                slope_changes.append('d')
                curr_slope = 'd'
            elif nums[i] == nums[i-1]:
                return False

            if len(slope_changes) > 3:
                return False

        if len(slope_changes) != 3:
            return False
        if slope_changes[0] == 'i' and slope_changes[1] == 'd' \
            and slope_changes[2] == 'i':
            return True

        return False
