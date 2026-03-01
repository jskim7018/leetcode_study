from typing import List
from functools import cache


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 뒤에서부터 가기면됨.
        # 미리 모든 애들의 다음으로 갈 것을 구하기.
        n = len(nums)

        @cache
        def get_aft_operation(num: int) -> int:
            for i in range(2, int(num ** 0.5)+1):
                if num % i == 0:
                    return i
            return num

        prev = float('inf')

        ans = 0
        for i in range(n-1,-1,-1):
            num = nums[i]
            while num > prev:
                nxt_num = get_aft_operation(num)
                if nxt_num == num:
                    return -1
                num = nxt_num
                ans += 1
            prev = num

        return ans
