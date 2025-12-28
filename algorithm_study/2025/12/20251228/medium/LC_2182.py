import heapq
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        heap = []

        for ch, v in counter.items():
            heap.append([-ord(ch), v])

        heapq.heapify(heap)

        ans = ''
        befbef = None
        while heap:
            bef = heapq.heappop(heap)
            ch = chr(-bef[0])
            if befbef is not None:
                bef[1] -= 1
                to_add = 1
                if bef[1] == 0:
                    bef = None
            elif bef[1] > repeatLimit:
                bef[1] -= repeatLimit
                to_add = repeatLimit
            else:
                to_add = bef[1]
                bef = None
            ans += to_add * ch
            if befbef is not None:
                heapq.heappush(heap, befbef)
                befbef = None
                if bef is not None:
                    heapq.heappush(heap, bef)
            elif bef is not None:
                befbef = bef

        return ans
