from typing import List, Optional
from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # row, col 독립적.
        # kahn 알고리즘 처럼 in-degree 0인 것부터 처리.
        # in-degree 0 이 없지만 모두 처리 못했으면 불가능.
        # 나머지는 그냥 뒤에 임의로 넣으면 딘다.

        def get_orders(conditions: List[List[int]]) -> Optional[List[int]]:
            graph = defaultdict(list)
            in_degree = [0] * (k+1)

            for c in conditions:
                graph[c[0]].append(c[1])
                in_degree[c[1]] += 1

            ret = []
            q = deque()
            for i in range(1, k+1):
                if in_degree[i] == 0:
                    q.append(i)

            while q:
                v = q.popleft()
                ret.append(v)

                for u in graph[v]:
                    in_degree[u] -= 1
                    if in_degree[u] == 0:
                        q.append(u)
            for i in range(1, k+1):
                if in_degree[i] > 0:
                    return None
            return ret

        row_order = get_orders(rowConditions)
        col_order = get_orders(colConditions)

        if row_order is None or col_order is None:
            return []

        coords = [[0] * 2 for _ in range(k+1)]
        for i in range(len(row_order)):
            coords[row_order[i]][0] = i
        for i in range(len(col_order)):
            coords[col_order[i]][1] = i

        ans = [[0]*k for _ in range(k)]
        n = len(coords)
        for i in range(1,n):
            ans[coords[i][0]][coords[i][1]] = i

        return ans
