from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))

        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i-1
        return -1
