from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        nums.append(-1) # sentinel
        n = len(nums)

        ans = 0

        alt_cnt = 1

        for i in range(1, n):
            if nums[i] == -1 or nums[i] == nums[i-1]:
                ans += (alt_cnt * (alt_cnt+1)) // 2
                alt_cnt = 1
            elif nums[i] != nums[i-1]:
                alt_cnt += 1

        return ans
