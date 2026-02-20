from typing import List
from collections import Counter
from functools import cache


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # TODO: 흥미로운 sliding window problem.
        # TODO: frequency counter 방식 꼭 정확히 이해하기.
        @cache
        def get_all_factors(num: int) -> List[int]:
            ret = []
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    ret.append(i)
                    if num // i > i:
                        ret.append(num // i)
                    else:
                        break
            return ret

        def get_gcd_from_counter(counter: Counter) -> int:
            max_v = 0
            max_k = 0
            for key, val in counter.items():
                if val == 0:
                    continue
                if val > max_v:
                    max_v = val
                    max_k = key
                elif val == max_v:
                    if key > max_k:
                        max_k = key
            return max_k

        def count_subarray_gcd(start: int, end: int) -> int:
            l = start
            counter = Counter()

            ret = 0
            for r in range(start, end+1):
                counter.update(get_all_factors(nums[r]))

                while l <= end and get_gcd_from_counter(counter) == k:
                    ret += end - r + 1
                    counter.subtract(get_all_factors(nums[l]))
                    l += 1
            return ret

        start = 0
        end = -1
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] % k == 0:
                end += 1
            if nums[i] % k != 0 or i == n-1:
                if start <= end:
                    ans += count_subarray_gcd(start, end)
                start = i + 1
                end = i

        return ans
