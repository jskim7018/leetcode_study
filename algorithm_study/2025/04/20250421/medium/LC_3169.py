from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        bef_end = -1
        meeting_days = 0
        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            if start <= bef_end:
                start = bef_end + 1
            meeting_days += max(0, end-start + 1)

            bef_end = max(bef_end, end)

        return days - meeting_days
