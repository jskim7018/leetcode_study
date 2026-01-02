from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        mp = dict()

        sorted_list = SortedList()

        ans = [-1] * n

        for i in range(n):
            if rains[i] == 0:
                sorted_list.add(i)
            else:
                if rains[i] in mp:
                    idx = sorted_list.bisect_left(mp[rains[i]])
                    if idx >= len(sorted_list):
                        return []
                    else:
                        ans[sorted_list[idx]] = rains[i]
                        sorted_list.remove(sorted_list[idx])
                mp[rains[i]] = i

        while sorted_list:
            ans[sorted_list.pop()] = 1

        return ans
