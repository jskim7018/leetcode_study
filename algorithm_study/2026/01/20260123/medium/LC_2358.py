from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        # TODO: greedy loop가 더 빠르다? k(k+1)/2 ≤ n  ⇒  k ≈ √(2n)
        # For n = 100,000:
        # √n ≈ 447
        # log₂(n) ≈ 17
        # binary search가 이론적으로는 더 빠른듯.

        def conseq_sum_formula(num: int) -> int:
            return (num * (num+1)) //2

        l = 0
        r = n
        ans = 0
        while l <= r:
            group_cnt = (l+r)//2
            conseq_sum = conseq_sum_formula(group_cnt)

            if conseq_sum <= n:
                ans = group_cnt
                l = group_cnt + 1
            else:
                r = group_cnt - 1

        return ans
