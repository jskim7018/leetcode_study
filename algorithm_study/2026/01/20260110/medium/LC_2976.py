from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str],
                    changed: List[str], cost: List[int]) -> int:
        alph_cnt = 26

        dist = [[float('inf')] * alph_cnt for _ in range(alph_cnt)]

        for i in range(alph_cnt):
            dist[i][i] = 0

        for o, ch, c in zip(original, changed, cost):
            u = ord(o)-ord('a')
            v = ord(ch)-ord('a')
            dist[u][v] = min(dist[u][v], c)

        # floyd warshall
        for k in range(alph_cnt):
            for i in range(alph_cnt):
                for j in range(alph_cnt):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        ans = 0
        for s, t in zip(source, target):
            s_num = ord(s) - ord('a')
            t_num = ord(t) - ord('a')
            if dist[s_num][t_num] != float('inf'):
                ans += dist[s_num][t_num]
            else:
                return -1

        return ans
