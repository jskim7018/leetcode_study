from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        is_new_interval_appended = False
        for interval in intervals:
            s = interval[0]
            e = interval[1]
            if not is_new_interval_appended:
                if (s <= newInterval[0] <= e or s <= newInterval[1] <= e\
                        or newInterval[0] <= s <= newInterval[1] or \
                        newInterval[0] <= e <= newInterval[1]):
                    newInterval[0] = min(newInterval[0], s)
                    newInterval[1] = max(newInterval[1], e)
                    continue
                elif newInterval[1] < s:
                    ans.append(newInterval)
                    is_new_interval_appended = True
            ans.append(interval)

        if not is_new_interval_appended:
            ans.append(newInterval)

        return ans
