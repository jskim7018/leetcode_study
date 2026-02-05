from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:

        graph = defaultdict(list)

        for p in prerequisites:
            graph[p[0]].append(p[1])

        dp = [[False] * numCourses for _ in range(numCourses)]

        def set_prerequisites(c1: int):
            if local_visited[c1]:
                return
            local_visited[c1] = True
            dp[start][c1] = True
            for u in graph[c1]:
                set_prerequisites(u)

        ans = []
        visited = [False] * numCourses
        for q in queries:
            start = q[0]
            if not visited[start]:
                local_visited = [False] * numCourses
                set_prerequisites(start)
                visited[start] = True
            ans.append(dp[q[0]][q[1]])

        return ans
