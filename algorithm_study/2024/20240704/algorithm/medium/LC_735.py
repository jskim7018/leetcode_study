from typing import List
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck = deque()

        ans = []
        for asteroid in asteroids:
            if asteroid >= 0:
                stck.append(asteroid)
            else:
                is_asteroid_destroyed = False
                while stck:
                    if stck[-1] < abs(asteroid):
                        stck.pop()
                    else:
                        is_asteroid_destroyed = True
                        if stck[-1] == abs(asteroid):
                            stck.pop()
                        break
                if not is_asteroid_destroyed:
                    ans.append(asteroid)

        return ans + list(stck)
