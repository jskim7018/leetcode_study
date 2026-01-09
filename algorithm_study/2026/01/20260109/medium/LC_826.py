from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        w_n = len(worker)

        profit_to_diff = [(p, d) for p, d in zip(profit, difficulty)]
        profit_to_diff.sort(key=lambda x: (-x[0], x[1]))
        worker.sort()

        worker_idx = 0

        ans = 0
        for p, d in profit_to_diff:
            while worker_idx < w_n and d <= worker[-1-worker_idx]:
                ans += p
                worker_idx += 1
            if worker_idx >= w_n:
                break
        return ans
