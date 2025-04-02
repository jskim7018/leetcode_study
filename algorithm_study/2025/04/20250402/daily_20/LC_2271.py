from typing import List
from itertools import accumulate
import bisect

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        n = len(tiles)
        tiles.sort()
        tiles_left = [a for a,b in tiles]
        prefix_sum = list(accumulate([b-a+1 for a,b in tiles]))

        ans = 0
        for i in range(n):
            right = tiles[i][0] + carpetLen

            r = bisect.bisect_left(tiles_left, right)
            r -= 1

            sum_ = prefix_sum[r] - max(tiles[r][1] - right + 1, 0)
            if i-1 >= 0:
                sum_ -= prefix_sum[i-1]
            ans = max(ans, sum_)

        return ans
