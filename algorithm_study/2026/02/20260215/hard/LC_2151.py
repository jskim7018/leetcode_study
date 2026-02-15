from typing import List
from collections import defaultdict, deque


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        # 완탐도 가능. 모든 경우의 수 적용 후 모순 없는 것 중 가장 good의 갯수가 큰 것이 답.
        # 모순 확인 법은 good들이 가리키는 사람들이 모두 일관되면 됨.
        # bitmask로 good혹은 bad 경우의 수를 모두 만들 수 있음.

        n = len(statements)

        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if statements[i][j] != 2:
                    graph[i].append((j, statements[i][j]))

        # TODO: 사실 정해진 good과 bad를 검증만 하면 되기에 굳이 bfs를 사용할 필요 없음.
        # TODO: 그냥 간단히 검증만 진행하면됨.
        def bfs(mask: int) -> int:
            q = deque()
            is_goods = [0] * n  # 0 - bad, 1 - good, 2 - dont know

            for i in range(n):
                is_good = (mask >> i) & 1
                if is_good:
                    q.append(i)
                    is_goods[i] = 1

            while q:
                v = q.popleft()

                for u, w in graph[v]:
                    if is_goods[u] == 1:
                        q.append(u)
                    elif w != is_goods[u]:  # 모순 (contradiction)
                        return -1
            good_cnt = 0
            for i in range(n):
                if is_goods[i] == 1:
                    good_cnt += 1
            return good_cnt

        bitmask = 0
        ans = 0
        while bitmask <= 2**n-1:
            ans = max(ans, bfs(bitmask))
            bitmask += 1

        return ans
