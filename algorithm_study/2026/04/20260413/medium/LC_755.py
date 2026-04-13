from typing import List


class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)

        for _ in range(volume):
            cand = k
            for i in range(k-1, -1, -1):
                if heights[i] > heights[cand]:
                    break
                elif heights[i] < heights[cand]:
                    cand = i

            if cand != k:
                heights[cand] += 1
            else:
                for i in range(k+1, n):
                    if heights[i] > heights[cand]:
                        break
                    elif heights[i] < heights[cand]:
                        cand = i

                heights[cand] += 1

        return heights
