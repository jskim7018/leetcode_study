from typing import List
from collections import defaultdict


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        counter = defaultdict(int)

        r = 0
        l = 0

        ans = float('inf')
        curr_sum = 0
        while r < n:
            while curr_sum < k and r < n:
                if nums[r] not in counter:
                    curr_sum += nums[r]
                counter[nums[r]] += 1
                r += 1

            while curr_sum >= k:
                ans = min(ans, r-l)
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                    curr_sum -= nums[l]
                l += 1
        if ans == float('inf'):
            return -1
        else:
            return ans
