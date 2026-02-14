from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # MST problem
        # Prim으로 풀어보자.
        # node 하나에서 시작. 해당 edge들을 heap에 넣음
        # heap에서 제일 작은거 꺼냄.
        # 그다음 해당 node의 edge들을 넣음. (새로운 node가 있는 것들만)
        # 더이상 사용할 edge가 없으면 끝.
        # 모든 node 연결되었는지 확인. 되었다면 sum 반환, 안되었다면 -1.
        graph = defaultdict(list)

        for c in connections:
            graph[c[0]].append((c[1],c[2]))
            graph[c[1]].append((c[0],c[2]))

        def prim() -> int:
            connected = [False] * (n+1)
            connected[1] = True
            heap = []

            for u, w in graph[1]:
                heap.append((w, u))

            heapq.heapify(heap)
            ret = 0
            while heap:
                w, v = heapq.heappop(heap)
                if connected[v]:
                    continue

                ret += w
                connected[v] = True

                for u, w in graph[v]:
                    if not connected[u]:
                        heapq.heappush(heap, (w,u))

            for i in range(1,n+1):
                if not connected[i]:
                    return -1
            return ret

        return prim()
