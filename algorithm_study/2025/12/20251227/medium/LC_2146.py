from typing import List
from collections import deque


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        m = len(grid)
        n = len(grid[0])

        def bfs(sy:int, sx: int) -> List[List[int]]:
            q = deque()
            q.append((sy, sx, 0))

            dy = [1,0,0, -1]
            dx = [0, -1,1,0]
            visited = [[False] * n for _ in range(m)]
            visited[sy][sx] = True
            end_dist = float('inf')
            ans = []
            while q:
                cy, cx, dist = q.popleft()

                if grid[cy][cx] >= 2 and pricing[0] <= grid[cy][cx] <= pricing[1]:
                    ans.append([dist, grid[cy][cx], cy, cx])
                    if len(ans) >= k:
                        end_dist = dist
                if dist > end_dist:
                    break

                for i in range(4):
                    ny = cy + dy[i]
                    nx = cx + dx[i]
                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        continue
                    if grid[ny][nx] == 0:
                        continue
                    if visited[ny][nx]:
                        continue
                    visited[ny][nx] = True

                    q.append((ny, nx, dist + 1))
            return ans

        ans = bfs(start[0], start[1])

        ans.sort()

        return [[y,x] for _,_,y,x in ans[:k]]
