from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        def dist_between_coord(x1,y1,x2,y2) -> float:
            return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

        directed_graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j:
                    if dist_between_coord(bombs[i][0], bombs[i][1],\
                                          bombs[j][0], bombs[j][1]) <= bombs[i][2]:
                        directed_graph[i].append(j)

        visited = set()
        def dfs(bomb_id: int):
            if bomb_id in visited:
                return
            visited.add(bomb_id)
            for next_bomb in directed_graph[bomb_id]:
                dfs(next_bomb)


        _max = 0
        for i in range(n):
            visited.clear()
            dfs(i)
            _max = max(_max, len(visited))

        return _max
