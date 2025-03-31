from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        next_possible_height = maximumHeight[0]

        ans = 0
        for height in maximumHeight:
            if next_possible_height <= 0:
                return -1
            if height <= next_possible_height:
                ans += height
                next_possible_height = height-1
            else:
                ans += next_possible_height
                next_possible_height -= 1

        return ans
