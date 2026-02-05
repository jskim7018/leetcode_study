from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sorting problem
        graph = defaultdict(list)
        in_degrees = defaultdict(int)
        total_edges = 0

        for p in prerequisites:
            graph[p[1]].append(p[0])
            in_degrees[p[0]] += 1
            total_edges += 1

        ans = []

        def bfs():
            nonlocal total_edges

            q = deque()
            for i in range(numCourses):
                if not in_degrees[i]:
                    q.append(i)

            while q:
                curr = q.popleft()
                ans.append(curr)
                for u in graph[curr]:
                    in_degrees[u] -= 1
                    total_edges -= 1
                    if not in_degrees[u]:
                        q.append(u)
        bfs()
        if total_edges:
            return []
        else:
            return ans
