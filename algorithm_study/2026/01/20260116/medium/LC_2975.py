from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7

        hFences = hFences + [1, m]
        vFences = vFences + [1, n]

        hFences.sort()
        vFences.sort()

        h_len = len(hFences)
        v_len = len(vFences)

        v_width_set = set()

        for i in range(v_len):
            for j in range(i + 1, v_len):
                v_width_set.add(vFences[j] - vFences[i])

        ans = -1
        for i in range(h_len):
            for j in range(i + 1, h_len):
                height = hFences[j] - hFences[i]
                if height in v_width_set:
                    ans = max(ans, (height*height) % mod)

        return ans
