from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        sweep = [0] * n
        for q in queries:
            start = q[0]
            end = q[1]
            sweep[start] -= 1
            if end + 1 < n:
                sweep[end + 1] += 1

        for i in range(n):
            if i-1 >=0:
                sweep[i] += sweep[i-1]
            nums[i] += sweep[i]
            if nums[i] > 0:
                return False
        return True
