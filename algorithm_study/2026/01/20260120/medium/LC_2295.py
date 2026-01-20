from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {v: i for i, v in enumerate(nums)}

        for old, new in operations:
            i = pos[old]
            nums[i] = new
            pos[new] = i
            del pos[old]

        return nums
