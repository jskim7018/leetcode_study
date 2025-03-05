from typing import List
from collections import Counter
import math


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)

        ans = 0
        for k, v in counter.items():
            ans += math.ceil(v / (k+1)) * (k+1)

        return ans
