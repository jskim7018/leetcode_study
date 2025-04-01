from typing import List


# TODO: Understand Lee's solution
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        suffix_max=[[]] * n
        suffix_min=[[]] * n

        for i in range(n-1,-1,-1):
            suffix_max[i] = [nums[i],i]
            suffix_min[i] = [nums[i],i]
            if i < n-1:
                if suffix_max[i][0] < suffix_max[i+1][0]:
                    suffix_max[i][0] = suffix_max[i+1][0]
                    suffix_max[i][1] = suffix_max[i+1][1]
                if suffix_min[i][0] > suffix_min[i+1][0]:
                    suffix_min[i][0] = suffix_min[i+1][0]
                    suffix_min[i][1] = suffix_min[i+1][1]

        for i in range(n-indexDifference):
            val = nums[i]
            if abs(suffix_max[i+indexDifference][0] - val) >= valueDifference:
                return [i, suffix_max[i+indexDifference][1]]

            if abs(suffix_min[i+indexDifference][0] - val) >= valueDifference:
                return [i, suffix_min[i + indexDifference][1]]

        return [-1,-1]
