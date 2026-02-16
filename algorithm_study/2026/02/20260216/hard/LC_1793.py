from typing import List


class Solution:
    def maximumScore(self, nums: List[int],  k: int) -> int:
        incr_stck = []  # (num, start idx)
        nums.append(0)  # sentinel
        ans = 0
        for i, num in enumerate(nums):
            s_idx = i
            while incr_stck and incr_stck[-1][0] >= num:
                last_num, last_s_idx = incr_stck.pop()
                if last_s_idx <= k < i:
                    ans = max(ans, last_num * (i - last_s_idx))
                s_idx = last_s_idx

            incr_stck.append([num, s_idx])

        return ans
