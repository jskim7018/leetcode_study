from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 2:
            return 2
        else:
            binary = bin(max(nums))[2:]
            binary = binary.replace('0','1')

            max_num = int(binary,2)
            return max_num + 1
