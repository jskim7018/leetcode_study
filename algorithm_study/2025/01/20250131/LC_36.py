from typing import List
from pprint import pprint

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        pprint(board)
        # 1
        for i in range(m):
            st = set()
            for j in range(n):
                if board[i][j] in st and board[i][j] != '.':
                    return False
                else:
                    st.add(board[i][j])

        # 2
        for j in range(n):
            st = set()
            for i in range(m):
                if board[i][j] in st and board[i][j] != '.':
                    return False
                else:
                    st.add(board[i][j])

        # 3
        for i in range(0, m-2, 3):
            for j in range(0, n-2, 3):
                st = set()
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        if board[a][b] in st and board[a][b] != '.':
                            return False
                        else:
                            st.add(board[a][b])
        return True
