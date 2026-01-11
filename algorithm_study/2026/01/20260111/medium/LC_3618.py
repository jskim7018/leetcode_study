from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        is_prime = [False, False] + ([True] * (n-2))

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                j = i
                while i*j < n:
                    is_prime[i*j] = False
                    j += 1

        p_indice_sum = 0
        non_p_indice_sum = 0

        for i in range(n):
            if is_prime[i]:
                p_indice_sum += nums[i]
            else:
                non_p_indice_sum += nums[i]

        return abs(p_indice_sum - non_p_indice_sum)
