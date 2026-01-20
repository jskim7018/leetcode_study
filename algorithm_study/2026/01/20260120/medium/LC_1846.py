from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        curr = 0
        for a in arr:
            if a > curr:
                curr += 1

        return curr
