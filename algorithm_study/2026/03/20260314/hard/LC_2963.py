from typing import List
from collections import defaultdict


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        # 2가지 숫자로 분류됨 -> 단독, 중복.
        # 중복이면 모두 하나에 포함 되어야함. 그러므로 중복이면 시작과 끝을 하나의 element로 본다.
        # 중복 중간에 중복이 있을 수 있기에 중복 last idx를 max 값으로 계속 구한다.
        n = len(nums)

        last_indexes = defaultdict(int)
        for i in range(n):
            last_indexes[nums[i]] = i

        cnt_unique = 0
        i = 0
        while i < n:
            val_last_idx = i
            while True:
                val = nums[i]
                val_last_idx = max(val_last_idx, last_indexes[val])
                if i == val_last_idx:
                    break
                else:
                    i += 1
            cnt_unique += 1
            i += 1

        return pow(2, cnt_unique-1, 10**9+7)
