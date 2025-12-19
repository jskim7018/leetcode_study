from typing import List


class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        total_penalty = 0

        for e in daysLate:
            if e == 1:
                total_penalty += 1
            elif 2 <= e <= 5:
                total_penalty += 2 * e
            else:
                total_penalty += 3 * e

        return total_penalty
