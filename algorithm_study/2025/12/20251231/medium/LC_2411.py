from typing import List
from collections import Counter


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)

        bit_counter = Counter()
        for idx, num in enumerate(nums):
            i = 0
            while num > 0:
                if num % 2 > 0:
                    bit_counter[i] += 1
                num //= 2
                i += 1

        curr_bit_counter = Counter()

        ans = []
        r = -1
        for idx, num in enumerate(nums):
            if idx - 1 >= 0:
                i = 0
                num = nums[idx-1]
                while num > 0:
                    if num % 2 > 0:
                        curr_bit_counter[i] -= 1
                        if curr_bit_counter[i] == 0:
                            del curr_bit_counter[i]
                        bit_counter[i] -= 1
                        if bit_counter[i] == 0:
                            del bit_counter[i]
                    num //= 2
                    i += 1

            while r < idx or (r+1 < n and len(curr_bit_counter) != len(bit_counter)):
                r += 1
                i = 0
                num = nums[r]
                while num > 0:
                    if num % 2 > 0:
                        curr_bit_counter[i] += 1
                    num //= 2
                    i += 1
            ans.append(r-idx + 1)
        return ans
