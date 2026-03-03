from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        # Initial OR of all numbers
        ans = 0
        for row in grid:
            for num in row:
                ans |= num

        # Try removing bits from high to low
        for bit in range(17, -1, -1):  # since grid[i][j] <= 1e5 (~17 bits)
            if not (ans & (1 << bit)):
                continue

            candidate = ans ^ (1 << bit)
            # Check feasibility
            possible = True
            for row in grid:
                found = False
                for num in row:
                    if (num | candidate) == candidate:
                        found = True
                        break
                if not found:
                    possible = False
                    break

            if possible:
                ans = candidate

        return ans