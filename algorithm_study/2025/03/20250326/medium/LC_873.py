from typing import List
from functools import lru_cache

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        mp = {arr[i]:i for i in range(n)}
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                prev_idx = i
                idx = j
                cnt = 2
                found = True
                while found:
                    found = False
                    to_find = arr[idx] + arr[prev_idx]

                    if to_find in mp:
                        prev_idx = idx
                        idx = mp[to_find]
                        found = True
                        cnt += 1
                ans = max(ans, cnt)

        if ans <= 2:
            return 0
        else:
            return ans