from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digit_sum_to_nums = []

        mp = {}
        for i, num in enumerate(nums):
            mp[i] = num
            digit_sum = 0
            tmp_num = num
            while tmp_num > 0:
                digit_sum += tmp_num % 10
                tmp_num //= 10
            digit_sum_to_nums.append((digit_sum, num, i))

        digit_sum_to_nums.sort(key=lambda x: (x[0], x[1]))
        num_to_sorted_idx = {num:i  for i, (_,num,_) in enumerate(digit_sum_to_nums)}
        ans = 0
        n = len(nums)
        i = 0
        while i < n:
            idx_to_go = num_to_sorted_idx[nums[i]]
            if i != idx_to_go:
                nums[i], nums[idx_to_go] = nums[idx_to_go], nums[i]
                ans += 1
            else:
                i += 1

        return ans
