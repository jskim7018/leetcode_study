from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for e in edges:
            dist[e[0]][e[1]] = e[2]
            dist[e[1]][e[0]] = e[2]

        # floyd warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        minim = float('inf')
        minim_city = -1

        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[j][i] <= distanceThreshold:
                    cnt += 1
            if cnt <= minim:
                minim = cnt
                minim_city = i

        return minim_city
