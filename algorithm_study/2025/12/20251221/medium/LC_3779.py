from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)

        left_pointer = 0

        remaining_size = n
        ans = 0
        while left_pointer < n:
            if remaining_size == len(counter):
                break
            else:
                counter[nums[left_pointer]] -= 1
                if counter[nums[left_pointer]] == 0:
                    del counter[nums[left_pointer]]
                if left_pointer + 1 < n:
                    counter[nums[left_pointer+1]] -= 1
                    if counter[nums[left_pointer+1]] == 0:
                        del counter[nums[left_pointer+1]]
                if left_pointer + 2 < n:
                    counter[nums[left_pointer+2]] -= 1
                    if counter[nums[left_pointer+2]] == 0:
                        del counter[nums[left_pointer+2]]
                remaining_size -= 3
                ans += 1

            left_pointer += 3

        return ans
