from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        hidden = [0] * (n+1)

        for i in range(n):
            hidden[i+1] += hidden[i]
            hidden[i+1] += differences[i]

        minim = min(hidden)
        maxim = max(hidden)

        x = lower-minim
        maxim_lowest = x + maxim

        return max(0, upper - maxim_lowest + 1)
