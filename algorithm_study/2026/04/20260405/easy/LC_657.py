class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y = 0
        x = 0

        for m in moves:
            if m == 'U':
                y -= 1
            elif m == 'D':
                y += 1
            elif m == 'L':
                x -= 1
            else:
                x += 1

        return y == 0 and x == 0
