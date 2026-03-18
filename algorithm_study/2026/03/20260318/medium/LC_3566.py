from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        product = 1
        for num in nums:
            product *= num

        if target * target != product:
            return False

        def dfs(i: int, curr: int):
            if curr == target:
                return True
            if curr > target:
                return False
            if i >= n:
                return False

            return dfs(i+1, curr * nums[i]) or dfs(i+1, curr)

        return dfs(0, 1)
