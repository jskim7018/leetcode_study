from typing import List
import math


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()

        ans = 0
        for i in range(len(workers)):
            ans = max(ans,math.ceil(jobs[i]/workers[i]))

        return ans
