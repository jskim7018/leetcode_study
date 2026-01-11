from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indexes = list()

        for i, num in enumerate(nums):
            if num == x:
                indexes.append(i)

        ans = []
        for q in queries:
            idx = q-1
            if idx >= len(indexes):
                ans.append(-1)
            else:
                ans.append(indexes[idx])

        return ans
