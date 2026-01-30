from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        sorted_from = 0
        n = len(nums)
        ans = []
        for i in range(1, k):
            if nums[i-1]+1 != nums[i]:
                sorted_from = i
        if sorted_from == 0:
            ans.append(nums[k-1])
        else:
            ans.append(-1)

        for i in range(k, n):
            if nums[i-1]+1 != nums[i]:
                sorted_from = i

            if sorted_from <= i-(k-1):
                ans.append(nums[i])
            else:
                ans.append(-1)
        return ans
