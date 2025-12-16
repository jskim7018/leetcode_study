from typing import List
from collections import Counter


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        counter_from_right = Counter(nums)
        counter_from_left = Counter()

        counter_from_right[nums[0]] -= 1
        counter_from_left[nums[0]] += 1

        ans = 0
        for num in nums[1:]:
            counter_from_right[num] -= 1

            ans += (counter_from_left[num*2] *
                    counter_from_right[num*2])
            ans %= mod

            counter_from_left[num] += 1

        return ans
