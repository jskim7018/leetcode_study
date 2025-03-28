from typing import List
import heapq
import bisect


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        sorted_queries = [[v, i, 0] for i,v in enumerate(queries)]
        sorted_queries.sort()
        sorted_values = [v for v, _, _ in sorted_queries]

        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        visited = [[False]*n for _ in range(m)]

        def solve():
            heap = []

            heapq.heapify(heap)
            heapq.heappush(heap, (grid[0][0], 0, 0, grid[0][0]))
            visited[0][0] = True
            while heap:
                element = heapq.heappop(heap)
                y = element[1]
                x = element[2]
                curr_maxim = element[3]
                idx = bisect.bisect_left(sorted_values, curr_maxim+1)

                if idx < len(sorted_queries):
                    sorted_queries[idx][2] += 1

                for i in range(4):
                    ny = dy[i] + y
                    nx = dx[i] + x

                    if ny >= 0 and nx >= 0 and ny < m and nx < n and not visited[ny][nx]:
                        visited[ny][nx] = True
                        heapq.heappush(heap, (grid[ny][nx],ny, nx, max(curr_maxim, grid[ny][nx])))

        solve()
        for i in range(1, len(sorted_queries)):
            sorted_queries[i][2] += sorted_queries[i-1][2]

        sorted_queries.sort(key=lambda x: x[1])
        ans = [x[2] for x in sorted_queries]

        return ans
