from typing import List
from collections import defaultdict


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = defaultdict(int)
        for num in arr:
            counter[num] += 1
        arr.sort()

        for num in arr:
            if counter[num] == 0:
                continue
            if num >= 0:
                if counter[num*2] == 0:
                    return False
                else:
                    counter[num] -= 1
                    counter[num*2] -= 1
            else:
                if num % 2 == 1 or counter[num//2] == 0:
                    return False
                else:
                    counter[num] -= 1
                    counter[num//2] -= 1
        return True