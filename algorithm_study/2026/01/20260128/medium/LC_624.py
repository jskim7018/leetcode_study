from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # TODO: global min, max과 current min, max 사용시 heap을 안써도됨. 이전에 나온 것들과 지금 있는 것의 min max 구하면 되기 때문.
        global_min = float('inf')
        global_max = float('-inf')
        ans = 0
        for i, arr in enumerate(arrays):
            curr_min = arr[0]
            curr_max = arr[-1]

            ans = max(ans, global_max - curr_min, curr_max - global_min)

            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)

        return ans
