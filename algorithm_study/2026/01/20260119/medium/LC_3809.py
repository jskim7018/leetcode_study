from typing import List


class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:

        ans = (-1, -1)
        curr_q = -1
        for t in towers:
            x, y, q = t
            m_dist = abs(center[0] - x) + abs(center[1] - y)
            if m_dist <= radius:
                if curr_q < q:
                    curr_q = q
                    ans = (x, y)
                elif curr_q == q:
                    if (x,y) < ans:
                        ans = (x,y)

        return list(ans)
