class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)

        if x < y:
            x, y = y, x

        if x == 1 and y == 0:
            return 3
        if x == 2 and y == 2:
            return 4

        d = max((x + 1) // 2, (x + y + 2) // 3)

        if (d % 2) != ((x + y) % 2):
            d += 1

        return d