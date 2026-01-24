from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort()
        rem_left, rem_right = toBeRemoved

        ans = []
        for interval in intervals:
            left, right = interval

            if right <= rem_left or rem_right <= left:
                ans.append(interval)
            else:
                if left < rem_left:
                    ans.append([left, rem_left])
                if right > rem_right:
                    ans.append([rem_right, right])

        return ans
