class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        char_to_coord = dict()
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        m = len(board)
        for i in range(m):
            s = board[i]
            for j in range(len(s)):
                char_to_coord[board[i][j]] = (i,j)

        ans = []
        curr = (0, 0)
        for ch in target:
            next = char_to_coord[ch]
            dy = curr[0] - next[0]
            dx = curr[1] - next[1]

            if dy < 0:
                dy_command = 'D'
            else:
                dy_command = 'U'
            if dx < 0:
                dx_command = 'R'
            else:
                dx_command = 'L'

            if ch == 'z':
                for i in range(abs(dx)):
                    ans.append(dx_command)
                for i in range(abs(dy)):
                    ans.append(dy_command)
            else:
                for i in range(abs(dy)):
                    ans.append(dy_command)
                for i in range(abs(dx)):
                    ans.append(dx_command)

            ans.append('!')
            curr = next

        return ''.join(ans)
