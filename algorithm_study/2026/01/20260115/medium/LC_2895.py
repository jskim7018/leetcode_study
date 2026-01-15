from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()

        tasks.sort(reverse=True)

        tasks = [tasks[i] for i in range(0, len(tasks), 4)]

        ans = 0
        for p, t in zip(processorTime, tasks):
            ans = max(ans, p+t)

        return ans
