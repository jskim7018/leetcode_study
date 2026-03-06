from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        for interval in intervals:
            left, right = interval
            if not ans or ans[-1][1] < left:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], right)

        return ans
