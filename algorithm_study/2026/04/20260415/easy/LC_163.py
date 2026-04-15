from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]

        if nums[0] > lower:
            nums.insert(0, lower - 1)
        if nums[-1] < upper:
            nums.append(upper+1)  # sentinel

        n = len(nums)

        ans = []
        for i in range(1, n):
            cand_l = nums[i-1]+1
            cand_r = nums[i] - 1

            if cand_l > cand_r:
                continue
            if lower > cand_r:
                continue
            if upper < cand_l:
                break

            maxim_l = max(cand_l, lower)
            minim_r = min(cand_r, upper)

            ans.append([maxim_l, minim_r])

        return ans
