from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l = 1
        r = max(ribbons)
        ribbons.sort(reverse=True)

        ans = 0
        while l <= r:
            mid = (l+r)//2
            possible_cnt = 0
            cand = 0
            for rib in ribbons:
                possible_cnt += rib//mid
                if possible_cnt >= k or rib < mid:
                    break
            if possible_cnt >= k:
                cand = mid
                l = mid + 1
            else:
                r = mid - 1
            ans = max(cand, ans)

        return ans
