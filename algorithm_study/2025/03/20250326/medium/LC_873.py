from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        st = set(arr)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                cnt = 2
                prev, curr = arr[i], arr[j]
                next = prev + curr
                while next in st:
                    prev = curr
                    curr = next
                    cnt += 1
                    next = prev + curr
                    ans = max(ans, cnt)

        if ans <= 2:
            return 0
        else:
            return ans