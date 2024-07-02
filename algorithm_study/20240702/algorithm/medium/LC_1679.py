from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter()
        for num in nums:
            counter[num] += 1

        cnt = 0
        for num in nums:
            if counter[num] > 0:
                counter[num] -= 1
                if counter[k-num] > 0:
                    counter[k-num] -= 1

                    cnt += 1
        return cnt
