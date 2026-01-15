from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        cnt = 1
        ans = 1

        turb_state = 0 # 1 if right is greater, -1 if right is lesser.

        for i in range(1, n):
            curr_turb_state = arr[i] - arr[i-1]
            if curr_turb_state > 0:
                curr_turb_state = 1
            elif curr_turb_state < 0:
                curr_turb_state = -1

            if curr_turb_state == 0:
                cnt = 1
            elif curr_turb_state != turb_state:
                cnt += 1
            else:
                cnt = 2
            turb_state = curr_turb_state
            ans = max(ans, cnt)

        return ans



