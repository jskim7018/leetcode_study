from typing import List
from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # TODO: count만 순회해서 빠르게 할 수 있음. num을 순회하면서 하나씩 할 필요 없음.

        rem_num_cnt = defaultdict(int)

        for num in arr:
            rem_num_cnt[num % k] += 1

        total = len(arr)
        for num in arr:
            rem = num % k
            if rem_num_cnt[rem] == 0:
                continue
            rem_num_cnt[rem] -= 1
            other = (k - rem) % k
            if rem_num_cnt[other] <= 0:
                return False
            else:
                rem_num_cnt[other] -= 1
            total -= 2
            if total == 0:
                break

        return True
