from typing import List
from collections import defaultdict


class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        prefix_sum = [0] * n
        num_to_indexes = defaultdict(list)

        # pre-process
        for i in range(n):
            prefix_sum[i] += capacity[i]
            if i - 1 >= 0:
                prefix_sum[i] += prefix_sum[i-1]
            num_to_indexes[capacity[i]].append(i)

        # solve
        ans = 0
        for num, indexes in num_to_indexes.items():
            prefix_cnt = defaultdict(int)
            prefix_mid_sum = num
            prefix_cnt[num] += 1
            for i in range(1, len(indexes)):
                l_idx = indexes[i-1]
                r_idx = indexes[i]
                mid_sum = prefix_sum[r_idx-1] - prefix_sum[l_idx]
                if r_idx - l_idx + 1 <= 2 and mid_sum == num:
                    ans -= 1
                prefix_mid_sum += mid_sum
                ans += prefix_cnt[prefix_mid_sum - num]
                prefix_mid_sum += num
                prefix_cnt[prefix_mid_sum] += 1

        return ans
