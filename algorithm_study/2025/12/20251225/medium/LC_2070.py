from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        q_with_idx = [[q, i, 0] for i, q in enumerate(queries)]
        q_with_idx.sort(key=lambda x: x[0])
        _max = 0
        q_idx = 0

        for (price, beauty) in items:
            while q_idx < len(q_with_idx) and price > q_with_idx[q_idx][0]:
                q_with_idx[q_idx][2] = _max
                q_idx += 1

            _max = max(_max, beauty)

        for i in range(q_idx, len(q_with_idx)):
            q_with_idx[i][2] = _max

        q_with_idx.sort(key=lambda x: x[1])

        return [q[2] for q in q_with_idx]
