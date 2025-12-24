from typing import List
from collections import defaultdict
import bisect


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        mp = defaultdict(lambda: 0)

        for s, _, val in events:
            mp[s] = max(mp[s], val)

        starts = list(mp.keys())
        starts.sort()

        for i in range(len(events)-2, -1, -1):
            mp[events[i][0]] = max(mp[events[i][0]], events[i][2], mp[events[i+1][0]])

        ans = 0
        for e in events:
            curr = e[2]
            end = e[1]
            right = bisect.bisect_left(starts, end+1)

            if right < len(starts):
                curr += mp[starts[right]]

            ans = max(ans, curr)

        return ans
