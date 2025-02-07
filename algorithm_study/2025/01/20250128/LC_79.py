from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        def dfs(y, x, curr_word_idx) -> bool:
            if y >= m or x >=n or y < 0 or x < 0:
                return False
            if board[y][x] != word[curr_word_idx]:
                return False
            if curr_word_idx == len(word)-1:
                return True


            ret = False
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny >= m or nx >= n or ny < 0 or nx < 0:
                    continue

                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    ret = ret or dfs(ny, nx, curr_word_idx+1)
                    visited[ny][nx] = False
            return ret

        visited = [[False for _ in range(n)] for _ in range(m)]
        ans = False
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                ans = ans or dfs(i, j, 0)
                visited[i][j] = False
        return ans
