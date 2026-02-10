from typing import List
from collections import defaultdict
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # 가장 많은애 부터 처리? => 왜 되는지?
        # 안되는 상황은 사실상 가장 많은 애가 번갈아가지 못하는 상황
        # 그러므로 가장 많은 애를 먼저 처리해서 최대한 번갈아 갈 수 있게 해야 한다.
        # TODO: heap 없이도 가능함.

        counter = defaultdict(int)
        for b in barcodes:
            counter[b] += 1

        heap = [(-v,k) for k,v in counter.items()]
        heapq.heapify(heap)
        ans = []
        while heap:
            reinsert = None
            if len(ans) != 0 and ans[-1] == heap[0][1]:
                reinsert = heapq.heappop(heap)
            freq, v = heapq.heappop(heap)
            freq = -freq
            ans.append(v)
            freq -= 1
            if freq != 0:
                heapq.heappush(heap, (-freq, v))

            if reinsert is not None:
                heapq.heappush(heap, reinsert)

        return ans
