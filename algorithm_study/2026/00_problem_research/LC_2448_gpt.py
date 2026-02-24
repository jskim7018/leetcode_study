from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Pair and sort
        # TODO: 아직 확실하게 이해는 안되는데 나중에 수학적으로 확실하게 이해할 필요가 있어 보인다.
        # TODO: medium 자체와 medium 관련 문제 확실히 이해하기.
        pairs = sorted(zip(nums, cost))

        total_weight = sum(cost)
        cumulative = 0

        # Find weighted median
        median = 0
        for num, c in pairs:
            cumulative += c
            if cumulative >= total_weight / 2:
                median = num
                break

        # Compute total cost
        result = 0
        for num, c in pairs:
            result += abs(num - median) * c

        return result