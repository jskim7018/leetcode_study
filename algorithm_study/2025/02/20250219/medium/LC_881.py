from typing import List
from collections import deque

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        dq = deque(people)

        boats = 0
        while dq:
            if len(dq) == 1:
                dq.pop()
                boats += 1
            else:
                if dq[0] + dq[-1] <= limit:
                    dq.popleft()
                    dq.pop()
                else:
                    dq.pop()
                boats += 1

        return boats
