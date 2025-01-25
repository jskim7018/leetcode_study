from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:

        ans = 0
        for a,b in zip(arr,brr):
            ans += abs(a-b)

        arr.sort()
        brr.sort()

        ans_with_k = k

        for a,b in zip(arr,brr):
            ans_with_k += abs(a-b)

        return min(ans, ans_with_k)
