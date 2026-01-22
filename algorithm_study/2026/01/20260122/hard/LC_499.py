from typing import List
import heapq


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])

        def bfs() -> str:
            dy = [1, 0, 0, -1]
            dx = [0, -1, 1, 0]
            instrs = ['d', 'l', 'r', 'u']
            heap = []
            least_instr = dict()
            visited = [[[float('inf') for _ in range(4)] for _ in range(n)] for _ in range(m)]
            for i in range(4):
                heap.append((0, tuple(ball), i, instrs[i]))
                visited[ball[0]][ball[1]][i] = 0
                least_instr[(ball[0], ball[1], i)] = instrs[i]

            shortest_to_hole = float('inf')
            heapq.heapify(heap)
            ans = "impossible"
            while heap:
                dist, curr, d, instr = heapq.heappop(heap)
                y, x = curr

                ny = y + dy[d]
                nx = x + dx[d]
                if dist > shortest_to_hole:
                    return ans

                traveled = 0
                if (y, x) == tuple(hole):
                    if dist < shortest_to_hole:
                        ans = instr
                        shortest_to_hole = dist
                    elif dist == shortest_to_hole:
                        if ans == "impossible" or instr < ans:
                            ans = instr
                while not (ny >= m or nx >= n or nx < 0 or ny < 0 or maze[ny][nx] == 1):
                    y = ny
                    x = nx
                    if (y, x) == tuple(hole):
                        if dist+traveled < shortest_to_hole:
                            ans = instr
                            shortest_to_hole = dist + traveled
                        elif dist+traveled == shortest_to_hole:
                            if ans == "impossible" or instr < ans:
                                ans = instr
                    ny = y + dy[d]
                    nx = x + dx[d]
                    traveled += 1

                if traveled == 0:
                    continue
                for nd in range(4):
                    if dist + traveled < visited[y][x][nd] or (dist+traveled == visited[y][x][nd] and
                                                               (y,x,nd) in least_instr and instr < least_instr[(y,x,nd)]):
                        visited[y][x][nd] = dist + traveled
                        least_instr[(y,x,nd)] = instr
                        heapq.heappush(heap, (dist + traveled, (y, x), nd, instr + instrs[nd]))
            return ans

        return bfs()