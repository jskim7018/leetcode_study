from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        curr_mass = mass

        asteroids.sort()

        for a in asteroids:
            if curr_mass >= a:
                curr_mass += a
            else:
                return False

        return True
