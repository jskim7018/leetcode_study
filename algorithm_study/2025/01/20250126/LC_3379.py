from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i, num in enumerate(nums):
            if num != 0:
                res_idx = (i + nums[i]) % n
                print(res_idx)
                result[i] = nums[res_idx]

        return result
