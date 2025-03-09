from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        curr_alt_size = 1
        ans = 0
        for i in range(1, n+k-1):
            i = i % n
            if colors[i] != colors[i-1]:
                curr_alt_size += 1
            else:
                curr_alt_size = 1

            if curr_alt_size >= k:
                ans += 1

        return ans
