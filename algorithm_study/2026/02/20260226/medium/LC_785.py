from typing import List
import pytest


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # TODO: two coloring 방식으로 더 빠르고 간단하게 구현 가능
        # bipartite = two coloring problem

        n = len(graph)

        def dfs(v: int, curr_set_A: bool):
            st = set(graph[v])
            if curr_set_A:
                set_B.update(st)
            else:
                set_A.update(st)

            ret = True
            for u in graph[v]:
                if not visited[u]:
                    if curr_set_A and u in set_A:
                        return False
                    elif not curr_set_A and u in set_B:
                        return False
                    visited[u] = True
                    ret &= dfs(u, not curr_set_A)
            return ret

        visited = [False] * n
        set_A = set()
        set_B = set()
        ret = True
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                ret &= dfs(i, True)
        return ret


@pytest.mark.parametrize("input_graph, expected", [
    ([[1,2,3],[0,2],[0,1,3],[0,2]], False),
    ([[1,3],[0,2],[1,3],[0,2]], True)
])
def test_isBipartite(input_graph, expected):
    sol = Solution()
    assert sol.isBipartite(input_graph) == expected
