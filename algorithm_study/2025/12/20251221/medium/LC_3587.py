from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        odd_indexes = []
        even_indexes = []
        for i, num in enumerate(nums):
            if num % 2 == 0:
                even_indexes.append(i)
            else:
                odd_indexes.append(i)

        odd_n = len(odd_indexes)
        even_n = len(even_indexes)

        def get_min_after_placement(start_parity: int)->int:
            odd_idx = 0
            even_idx = 0
            ans = 0
            for i in range(0,n,2):
                if start_parity == 0:
                    ans += abs(i-even_indexes[even_idx])
                    even_idx += 1
                else:
                    ans += abs(i-odd_indexes[odd_idx])
                    odd_idx += 1
            return ans

        if n % 2 == 0 and odd_n == even_n:
            return min(get_min_after_placement(0), get_min_after_placement(1))
        elif n % 2 == 1:
            if odd_n == even_n+1:
                return get_min_after_placement(1)
            elif even_n == odd_n + 1:
                return get_min_after_placement(0)
            else:
                return -1
        else:
            return -1
