from typing import List
from functools import cache
from sortedcontainers import SortedList


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        multiset = SortedList()
        minim_ops = [0] * n
        left_sum = 0
        right_sum = 0
        for i in range(x):
            multiset.add(nums[i])
        mid = multiset[x//2]

        for i, element in enumerate(multiset):
            if i < x//2:
                left_sum += element
            else:
                right_sum += element

        if x % 2 == 1:
            minim_ops[0] = abs(mid*(x//2) - left_sum) + abs(mid*(x//2) - (right_sum-mid))
        else:
            minim_ops[0] = abs(mid * (x // 2) - left_sum) + abs(mid * (x // 2) - right_sum)

        for i in range(1,n-x+1):
            prev_mid = multiset[x // 2]
            is_left_delete = False
            if nums[i-1] >= prev_mid:
                right_sum -= nums[i-1]
            else:
                is_left_delete = True
                left_sum -= nums[i-1]

            multiset.remove(nums[i-1])
            multiset.add(nums[i+x-1])

            aft_mid = multiset[x // 2]
            if is_left_delete:
                if nums[i+x-1] <= prev_mid:
                    left_sum += nums[i+x-1]
                else:
                    right_sum += nums[i+x-1]
                    right_sum -= prev_mid
                    left_sum += prev_mid
            else:
                if nums[i+x-1] >= prev_mid:
                    right_sum += nums[i+x-1]
                else:
                    if aft_mid != nums[i+x-1]:
                        left_sum += nums[i+x-1]
                    if aft_mid <= prev_mid and aft_mid != nums[i+x-1]:
                        left_sum -= aft_mid
                    right_sum += aft_mid

            if x % 2 == 1:
                minim_ops[i] = abs(aft_mid * (x // 2) - left_sum) + abs(aft_mid * (x // 2) - (right_sum - aft_mid))
            else:
                minim_ops[i] = abs(aft_mid * (x // 2) - left_sum) + abs(aft_mid * (x // 2) - right_sum)

        @cache
        def solve(i, k_) -> int:
            if k_ == 0:
                return 0
            if i + x > n:
                return float('inf')

            ret = solve(i+1, k_)

            ret = min(ret, solve(i+x, k_ - 1) + minim_ops[i])

            return ret
        ans = solve(0, k)
        solve.cache_clear()
        return ans
