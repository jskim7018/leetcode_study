from typing import List
from collections import deque


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # consecutive이기에 sliding window 가능
        # sum은 쉽게 sliding window 가능, max만 sliding 윈도우로 동적으로 유지하면 됨.
        # max sliding window는 monotonic stack -> decreasing monotonic queue
        n = len(chargeTimes)
        mono_queue = deque()
        run_cost_sum = 0
        ans = 0

        l = 0
        for r in range(n):
            while mono_queue and mono_queue[-1] < chargeTimes[r]:
                mono_queue.pop()
            mono_queue.append(chargeTimes[r])

            run_cost_sum += runningCosts[r]

            k = r-l+1
            curr = mono_queue[0] + run_cost_sum * k
            while curr > budget:
                if mono_queue[0] == chargeTimes[l]:
                    mono_queue.popleft()
                run_cost_sum -= runningCosts[l]

                l += 1
                if not mono_queue:
                    break
                else:
                    k = r-l+1
                    curr = mono_queue[0] + run_cost_sum * k
            ans = max(ans, r-l+1)

        return ans
