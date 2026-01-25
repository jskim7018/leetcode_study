from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pos = []
        for num in nums:
            if num >= 0:
                pos.append(num)
        if not len(pos):
            return nums

        pos_idx = k % len(pos)
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                nums[i] = pos[pos_idx]
                pos_idx = (pos_idx + 1) % len(pos)

        return nums
