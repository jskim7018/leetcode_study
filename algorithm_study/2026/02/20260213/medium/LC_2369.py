from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                if i - 2 >= 0:
                    dp[i] |= dp[i - 2]
                else:
                    dp[i] = True
            if i - 2 >= 0:
                if (nums[i] == nums[i - 1] == nums[i - 2]
                        or (nums[i - 2] + 1 == nums[i - 1]
                            and nums[i-1] + 1 == nums[i])):
                    if i - 3 >= 0:
                        dp[i] |= dp[i - 3]
                    else:
                        dp[i] = True
        return dp[n - 1]
