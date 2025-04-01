from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        curr = 0

        line_sweep = [0] * n

        for i in range(n):
            num = nums[i]
            curr += line_sweep[i]

            if num > curr:
                diff = num-curr
                if i+k<n:
                    line_sweep[i+k] -= diff
                elif i+k>n:
                    return False
                curr = num
            elif num < curr:
                return False

        return True
