from typing import List


class Solution:

    # alternate between extremes
    def maxCaloriesBurnt(self, heights: List[int]) -> int:
        n = len(heights)

        heights.sort(reverse=True)

        max_group = []
        min_group = []

        if n % 2 == 0:
            maxim_size = n//2
        else:
            maxim_size = n//2 + 1

        for i in range(maxim_size):
            max_group.append(heights[i])
        for i in range(maxim_size, n):
            min_group.append(heights[i])

        min_group.sort()

        curr = 0
        ans = 0
        max_idx = 0
        min_idx = 0

        while max_idx < len(max_group) \
            or min_idx < len(min_group):
            if max_idx < len(max_group):
                ans += (max_group[max_idx] - curr) ** 2
                curr = max_group[max_idx]
                max_idx += 1
            if min_idx < len(min_group):
                ans += (min_group[min_idx] - curr) ** 2
                curr = min_group[min_idx]
                min_idx += 1

        return ans
