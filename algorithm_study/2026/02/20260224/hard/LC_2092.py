from typing import List
from collections import defaultdict, deque
import pytest


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # 시간이 다를때는 간단. (이전 시간에 secret을 아는 사람이 그냥 알려줌)
        # 시간이 같은 것들이 여러개일때는?
        # 같은 시간에 대해서 그래프 만든 후 multi graph/multi bfs 문제. secret을 아는 애들을 시작으로 bfs
        # TODO: Multi-bfs 대신 union-find도 가능 (cleaner)

        knows_secret = [False] * n
        knows_secret[0] = True
        knows_secret[firstPerson] = True

        time_to_conn = defaultdict(list)

        for meeting in meetings:
            p1, p2, t = meeting
            time_to_conn[t].append((p1, p2))

        time_to_conn_list = [(t, conns) for t, conns in time_to_conn.items()]
        time_to_conn_list.sort()

        for _, edges in time_to_conn_list:
            graph = defaultdict(list)
            q = deque()
            curr_t_knows_secret = set()
            for e in edges:
                graph[e[0]].append(e[1])
                graph[e[1]].append(e[0])
                if knows_secret[e[0]]:
                    curr_t_knows_secret.add(e[0])
                if knows_secret[e[1]]:
                    curr_t_knows_secret.add(e[1])
            for e in curr_t_knows_secret:
                q.append(e)

            while q:
                v = q.popleft()

                for u in graph[v]:
                    if knows_secret[u]:
                        continue
                    knows_secret[u] = True
                    q.append(u)
        ans = []
        for i in range(n):
            if knows_secret[i]:
                ans.append(i)

        return ans


@pytest.mark.parametrize("input_n, input_meetings, input_firstPerson, expected", [
    (6, [[1,2,5],[2,3,8],[1,5,10]], 1, [0,1,2,3,5]),
    (4,[[3,1,3],[1,2,2],[0,3,3]],3,[0,1,3]),
    (5,[[3,4,2],[1,2,1],[2,3,1]], 1,[0,1,2,3,4])
])
def test_findAllPeople(input_n, input_meetings, input_firstPerson, expected):
    sol = Solution()
    assert sol.findAllPeople(input_n, input_meetings, input_firstPerson) == expected
