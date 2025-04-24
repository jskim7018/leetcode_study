from typing import List
from collections import deque


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        maxim = max(skills)

        dq = deque([(v,i) for i,v in enumerate(skills)])

        curr_wins = 0

        while dq[0][0] != maxim:
            if dq[0][0] > dq[1][0]:
                curr_wins += 1
                tmp = dq.popleft()
                dq.append(dq.popleft())
                dq.appendleft(tmp)
            else:
                curr_wins = 1
                dq.append(dq.popleft())
            if curr_wins == k:
                return dq[0][1]

        return dq[0][1]
