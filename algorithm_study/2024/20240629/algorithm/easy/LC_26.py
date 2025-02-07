from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = '_'
            else:
                ans += 1

        null_pos = 0
        val_pos = 0
        while True:
            while null_pos < len(nums) and nums[null_pos] != '_':
                null_pos += 1
            while val_pos < len(nums) and (val_pos < null_pos or nums[val_pos] == '_'):
                val_pos += 1
            if null_pos < len(nums) and val_pos < len(nums):
                nums[null_pos], nums[val_pos] = nums[val_pos], nums[null_pos]
            else:
                break

        return ans

"""
아래 솔루션 참고. 훨씬 간결. swap 필요 없음. 비교하고 앞에 채워넣어주면 됨.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex = insertIndex + 1
        return insertIndex
"""