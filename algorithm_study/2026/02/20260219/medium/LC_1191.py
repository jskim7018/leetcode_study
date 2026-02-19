from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 1. k가 1중 제일 큰거
        # 2. k가 2 이상 일때, max suffix + max prefix, total이 양수면 (k-2) * total
        # 1,2 max로.
        mod = 10 ** 9 + 7

        n = len(arr)
        k1_max_sum = 0
        k1_sum = 0
        total_sum = 0

        max_prefix = 0
        max_suffix = 0

        sum_from_prefix = 0
        sum_from_suffix = 0

        for i in range(n):
            sum_from_prefix += arr[i]
            sum_from_suffix += arr[-1-i]

            max_prefix = max(max_prefix, sum_from_prefix)
            max_suffix = max(max_suffix, sum_from_suffix)

            num = arr[i]
            total_sum += num
            if k1_sum + num > 0:
                k1_sum += num
            else:
                k1_sum = 0
            k1_max_sum = max(k1_max_sum, k1_sum)

        if k == 1:
            return k1_max_sum
        else:
            return max(k1_max_sum, max_suffix + (k-2) * max(0, total_sum) + max_prefix) % mod
