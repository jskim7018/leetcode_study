from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nextVisit)
        time_taken = [0] * n

        time = 0
        for i, v in enumerate(nextVisit):
            time_taken[i] = time
            time += time_taken[i]
            if v >= 0:
                time -= time_taken[v]
            time += 2
            time %= mod

        return time_taken[n-1]
