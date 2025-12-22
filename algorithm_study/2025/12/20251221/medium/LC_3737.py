from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            target_cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_cnt += 1
                if target_cnt >= (j-i+1)//2 + 1:
                    ans += 1
        return ans
