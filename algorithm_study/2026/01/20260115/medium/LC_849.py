from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)

        first = -1
        last = -1
        prev = -1

        ans = 0
        for i in range(n):
            if seats[i] == 1:
                if first == -1:
                    first = i
                last = i
                if prev != -1:
                    m_seat_cnt = i - prev - 1
                    ans = max(ans, m_seat_cnt // 2 + m_seat_cnt % 2)
                prev = i

        ans = max(ans, first, n-last-1)

        return ans
