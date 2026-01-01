from typing import List
from collections import Counter, defaultdict


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter()
        for num in nums:
            counter[num % k] += 1

        visited = [False] * k
        alt_cnt_max = 0
        for i in range(n):
            curr_last_idx = -1
            non_curr_last_idx = defaultdict(lambda: -1)

            curr = nums[i] % k
            if visited[curr]:
                continue
            visited[curr] = True
            tmp_counter = Counter()
            for j in range(i, n):
                if nums[j] % k == curr:
                    curr_last_idx = j
                else:
                    if non_curr_last_idx[nums[j] % k] < curr_last_idx:
                        tmp_counter[nums[j] % k] += 2
                    non_curr_last_idx[nums[j] % k] = j
            for key, v in non_curr_last_idx.items():
                if curr_last_idx > v:
                    tmp_counter[key] += 1

            for v in tmp_counter.values():
                alt_cnt_max = max(alt_cnt_max, v)

        return max(*counter.values(), alt_cnt_max)
