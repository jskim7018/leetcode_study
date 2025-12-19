class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        max_cargo = n*n

        if max_cargo * w <= maxWeight:
            return max_cargo
        else:
            return maxWeight//w
