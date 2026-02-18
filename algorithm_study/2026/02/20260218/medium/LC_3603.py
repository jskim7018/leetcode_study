from typing import List
import heapq


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        # 시작과 끝이 아니면 무조건 waitCost 비용 듬.
        # 그냥 시작과 끝이 아니면 waitCost도 이동비용에 포함 시켜서 dijkstra 돌림.
        # TODO: DP도 가능? dp가 더 빠른가? dp는 O(V+E)라서 더 빠르다. dijkstra는 (O(V+E)log(V))

        def dijkstra() -> int:
            dy = [0, 1]
            dx = [1, 0]
            heap = [(1, (0, 0))]  # dist, (y, x)
            costs = [[float('inf')] * n for _ in range(m)]

            while heap:
                cost, (y, x) = heapq.heappop(heap)

                if costs[y][x] < cost:
                    continue

                for i in range(2):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        continue

                    new_cost = cost + (ny+1) * (nx+1)
                    if ny == m-1 and nx == n-1:
                        return new_cost

                    new_cost += waitCost[ny][nx]
                    if costs[ny][nx] > new_cost:
                        costs[ny][nx] = new_cost
                        heapq.heappush(heap, (new_cost, (ny,nx)))
            return -1

        return dijkstra()
