from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stck = []

        for num in nums:
            stck.append(num)
            while len(stck) >= 2 and stck[-1] == stck[-2]:
                popped = stck.pop()
                stck[-1] += popped

        return stck
