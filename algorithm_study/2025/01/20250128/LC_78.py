from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        subset = []
        def all_subsets(idx, nums:List[int]):
            if idx > n:
                return
            if idx == n:
                ans.append(list(subset))
                return

            all_subsets(idx+1, nums)

            subset.append(nums[idx])
            all_subsets(idx+1, nums)
            subset.pop()

        all_subsets(0, nums)

        return ans
