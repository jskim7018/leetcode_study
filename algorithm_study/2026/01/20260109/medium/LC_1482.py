from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        l = 1
        r = max(bloomDay)

        ans = float('inf')
        while l <= r:
            mid = (l+r)//2

            bouq_cnt = 0
            curr_idx = 0
            while bouq_cnt < m:
                is_possible = True
                if curr_idx + k - 1 >= n:
                    break
                for i in range(curr_idx, curr_idx + k):
                    if bloomDay[i] > mid:
                        is_possible = False
                        curr_idx = i + 1
                        break
                if is_possible:
                    bouq_cnt += 1
                    curr_idx = curr_idx + k
            if bouq_cnt >= m:
                ans = mid
                r = mid-1
            else:
                l = mid+1

        if ans == float('inf'):
            return -1
        else:
            return ans
