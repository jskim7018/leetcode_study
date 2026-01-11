from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums

        curr_len = 1
        ans = []
        for i in range(1, n):
            curr_power = nums[i]
            if nums[i] == nums[i - 1]+1:
                curr_len += 1
            else:
                curr_len = 1
            if curr_len >= k:
                ans.append(curr_power)
            elif curr_len < k and i+1 >= k:
                ans.append(-1)

        return ans
