from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # max는 sum(gaps)
        # Min은 max(gap)이 0 이면 0 min(gaps)이 1이면 1, else 2

        arr = [a,b,c]
        arr.sort()

        gaps = [arr[1] - arr[0] - 1, arr[2] - arr[1] - 1]

        gaps.sort()

        ans = [0, 0]
        _sum = sum(gaps)
        # max 부터
        ans[1] = _sum

        # m
        if _sum == 0:
            ans[0] = 0
        else:
            if gaps[0] <= 1 or gaps[1] <= 1:
                ans[0] = 1
            else:
                ans[0] = 2

        return ans
