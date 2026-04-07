class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        res = 0

        # start from last internal node → go upward
        for i in range(n // 2 - 1, -1, -1):
            left = 2 * i + 1
            right = 2 * i + 2

            # difference we must fix
            res += abs(cost[left] - cost[right])

            # propagate max path sum upward
            cost[i] += max(cost[left], cost[right])

        return res
