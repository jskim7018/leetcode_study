from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = sum(nums[:2])

        ans = 1
        idx = 2
        while idx < len(nums)-1:
            if sum(nums[idx:idx+2]) == score:
                idx += 2
                ans += 1
            else:
                break
        return ans
