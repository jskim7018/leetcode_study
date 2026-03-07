from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 사실상 cycle detection on directed graph.
        # in-degree 없는 애들로 모두 시작해서 한다.
        # cycle detection 안하고 그냥 in-dgree 없는 애들 모두 순회하고
        # 순회한 갯수와 numCourses가 맞는지 확인만 하면 된다.

        graph = defaultdict(list)
        in_degrees = defaultdict(int)

        for p in prerequisites:
            a, b = p
            graph[b].append(a)
            in_degrees[a] += 1

        def bfs():
            visited_cnt = 0

            q = deque()
            for i in range(numCourses):
                if in_degrees[i] == 0:
                    q.append(i)

            while q:
                v = q.popleft()
                visited_cnt += 1

                for u in graph[v]:
                    in_degrees[u] -= 1
                    if in_degrees[u] == 0:
                        q.append(u)

            return visited_cnt == numCourses

        return bfs()
