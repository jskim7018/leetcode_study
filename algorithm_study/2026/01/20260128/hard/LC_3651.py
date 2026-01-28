from typing import List
import heapq


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        grid_val_n_coord = list()
        for i in range(m):
            for j in range(n):
                grid_val_n_coord.append((grid[i][j], (i, j)))
        grid_val_n_coord.sort()
        k_to_grid = dict()
        # TODO: 직접 저장할 필요 없이 index만 가지고 있으면 됨.
        for i in range(1, k+1):
            k_to_grid[i] = 0

        def dijkstra() -> int:
            heap = []

            visited = [[[float('inf') for _ in range(k+1)] for _ in range(n)] for _ in range(m)]

            heap.append((0, (0, 0), 0))
            visited[0][0][0] = 0
            while k > 0 and k_to_grid[1] < len(grid_val_n_coord) and \
                    grid_val_n_coord[k_to_grid[1]][0] <= grid[0][0]:
                heap.append((0, grid_val_n_coord[k_to_grid[1]][1], 1))
                k_to_grid[1] += 1
            heapq.heapify(heap)
            while heap:
                dist, (y, x), used_k = heapq.heappop(heap)
                if y == m-1 and x == n-1:
                    return dist
                while k > used_k and k_to_grid[used_k+1] < len(grid_val_n_coord) and \
                        grid_val_n_coord[k_to_grid[used_k+1]][0] <= grid[y][x]:
                    ny, nx = grid_val_n_coord[k_to_grid[used_k+1]][1]
                    k_to_grid[used_k+1] += 1
                    if visited[ny][nx][used_k+1] > dist:
                        visited[ny][nx][used_k + 1] = dist
                        heapq.heappush(heap, (dist, (ny, nx), used_k + 1))

                if y + 1 < m and visited[y+1][x][used_k] > dist+grid[y+1][x]:
                    visited[y + 1][x][used_k] = dist+grid[y+1][x]
                    heapq.heappush(heap, (dist+grid[y+1][x], (y+1, x), used_k))
                if x + 1 < n and visited[y][x+1][used_k] > dist+grid[y][x+1]:
                    visited[y][x + 1][used_k] = dist+grid[y][x+1]
                    heapq.heappush(heap, (dist+grid[y][x+1], (y, x+1), used_k))

        return dijkstra()
