from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        def consecutive_sum_formula(start: int, end: int) -> int:
            size = end - start + 1
            return (size*(2*start + (size-1)))//2

        banned = banned + [0, n + 1]
        banned = list(set(banned))
        banned.sort()
        banned_len = len(banned)
        total_sum = 0
        ans = 0
        for i in range(banned_len - 1):
            start = banned[i] + 1
            left = banned[i] + 1
            right = banned[i+1] - 1

            if left > n:
                break
            elif right > n:
                right = n

            _sum = consecutive_sum_formula(left, right)

            if _sum + total_sum <= maxSum:
                total_sum += _sum
                ans += right - start + 1
            else:
                to_add = 0
                while left <= right:
                    mid = (left + right) // 2
                    tmp_sum = consecutive_sum_formula(start, mid)
                    if tmp_sum + total_sum <= maxSum:
                        to_add = mid - start + 1
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += to_add
                break

        return ans
