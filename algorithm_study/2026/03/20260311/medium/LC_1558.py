from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 1은 알아서 하면 되고
        # 2를 몇번 곱했는지 최대 구하고, 총 사용한 1 갯수도 구함.
        # 각각에 대해서 최대 구함. O(n*logn)

        max_mult2_cnt = 0
        ans = 0

        for num in nums:
            curr_mult2_cnt = 0
            while num > 0:
                if num % 2 == 0:
                    num //= 2
                    curr_mult2_cnt += 1
                else:
                    num -= 1
                    ans += 1
            max_mult2_cnt = max(max_mult2_cnt, curr_mult2_cnt)

        ans += max_mult2_cnt
        return ans
