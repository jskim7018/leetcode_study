from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)  # sentinel
        n = len(nums)

        def no_zero_max_len(l: int, r: int) -> int:
            neg_cnt = 0
            first_neg = -1
            last_neg = -1

            for i in range(l, r+1):
                if nums[i] < 0:
                    neg_cnt += 1
                    if first_neg == -1:
                        first_neg = i
                    last_neg = i
            total_length = r-l+1
            if neg_cnt % 2 == 0:
                return total_length
            else:
                return max(r-first_neg,
                           last_neg-l)

        curr_l = 0
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                if curr_l <= i-1:
                    ans = max(ans, no_zero_max_len(curr_l, i - 1))
                curr_l = i + 1

        return ans
