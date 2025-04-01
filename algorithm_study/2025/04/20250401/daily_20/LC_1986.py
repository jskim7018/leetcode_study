from typing import List
from functools import cache


# TODO Check optimized DP. no need curr_session_time in solve
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        @cache
        def solve(bit_set, curr_session_time) -> int:
            if bit_set <= 0:
                return 1

            ret = float('inf')
            for i in range(n):
                if (bit_set >> i) & 1 == 1:
                    bit_set &= ~(1 << i)
                    if tasks[i] <= curr_session_time:
                        ret = min(ret, solve(bit_set, curr_session_time-tasks[i]))
                    else:
                        ret = min(ret, solve(bit_set, sessionTime - tasks[i]) + 1)
                    bit_set |= 1 << i
            return ret

        return solve(2**n-1,sessionTime)
