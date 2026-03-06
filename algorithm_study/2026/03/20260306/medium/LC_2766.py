from typing import List
from collections import defaultdict


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        pos_marble_cnt = defaultdict(int)
        # TODO: marble의 갯수는 중요하지 않기에 set으로 해도 가능.
        for pos in nums:
            pos_marble_cnt[pos] += 1

        n = len(moveFrom)

        for i in range(n):
            if moveTo[i] != moveFrom[i]:
                pos_marble_cnt[moveTo[i]] += pos_marble_cnt[moveFrom[i]]
                pos_marble_cnt[moveFrom[i]] = 0
                del pos_marble_cnt[moveFrom[i]]

        return list(sorted(pos_marble_cnt.keys()))
