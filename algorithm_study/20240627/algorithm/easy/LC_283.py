class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0, 0
        while True:
            while i < len(nums) and nums[i] != 0:
                i += 1
            while j<= i or (j < len(nums) and nums[j] == 0):
                j += 1
            if i>=len(nums) or j>=len(nums):
                break
            nums[i], nums[j] = nums[j], nums[i]

        return nums
