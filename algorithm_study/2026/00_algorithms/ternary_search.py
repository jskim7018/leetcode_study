from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # ternary search는 mid1,mid2 이렇게 2개가 있음. 나눌때 3등분으로 나눔.
        # reference problem (LC_2448)
        def compute(x: int) -> int:
            total = 0
            for n, c in zip(nums, cost):
                total += abs(n - x) * c
            return total

        left = min(nums)
        right = max(nums)

        while right - left > 2:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            cost1 = compute(mid1)
            cost2 = compute(mid2)

            if cost1 < cost2:
                right = mid2 - 1
            else:
                left = mid1 + 1

        # Final brute force on small interval
        answer = float('inf')
        for x in range(left, right + 1):
            answer = min(answer, compute(x))

        return answer