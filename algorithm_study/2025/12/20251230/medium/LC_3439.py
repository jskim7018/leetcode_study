from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        suffix_sum = [0] * n

        for i in range(0, n):
            suffix_sum[-1-i] = endTime[-1-i] - startTime[-1-i]
            if i != 0:
                suffix_sum[-1-i] += suffix_sum[-i]

        curr = 0
        ans = 0
        for i in range(n):
            tmp_ans = 0
            right = eventTime
            tmp_ans -= suffix_sum[i]
            if i + k < n:
                right = startTime[i+k]
                tmp_ans += suffix_sum[i+k]
            tmp_ans += right - curr
            ans = max(ans, tmp_ans)

            curr = endTime[i]
        return ans
