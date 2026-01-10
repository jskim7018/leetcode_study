from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        chalk_sum = sum(chalk)

        remainder_chalks = k % chalk_sum

        for i in range(n):
            if remainder_chalks < chalk[i]:
                return i
            remainder_chalks -= chalk[i]

        return -1
