from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int,
                  color: str) -> bool:
        n = len(board)
        m = len(board[0])

        def check_by_direction(y: int, x: int) -> bool:
            middle_found = False

            i = rMove + y
            j = cMove + x
            while i < n and j < m and i >= 0 and j >= 0:
                next = board[i][j]
                if next == '.':
                    return False
                elif next != color:
                    middle_found = True
                elif next == color:
                    if middle_found:
                        return True
                    else:
                        return False

                i += y
                j += x
            return False

        dy = [1, -1, 0, 0, 1, 1, -1, -1]
        dx = [0, 0, 1, -1, 1, -1, 1, -1]

        for i in range(8):
            if check_by_direction(dy[i], dx[i]):
                return True

        return False
