from typing import List
from sortedcontainers import SortedSet
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        target_arr_time = times[targetFriend][0]

        times.sort()

        available_seats = SortedSet()
        taken_seats = list() # (leave time, seat#)

        next_seat = 0
        for a,l in times:
            while taken_seats and taken_seats[0][0] <= a:
                seat = heapq.heappop(taken_seats)[1]
                available_seats.add(seat)
            if len(available_seats) == 0:
                curr_taken = next_seat
                next_seat += 1
            else:
                curr_taken = available_seats[0]
                available_seats.remove(curr_taken)
            heapq.heappush(taken_seats, (l, curr_taken))

            if a == target_arr_time:
                return curr_taken

        return -1
