from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        counter = Counter(nums)

        ans = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] - k > nums[l]:
                l += 1
            window = r - l + 1
            print('l: ', l)
            print('r: ', r)
            print(window)
            same_cnt = counter[nums[r]]
            ans = max(ans, same_cnt + min(window-same_cnt, numOperations))

        return ans
