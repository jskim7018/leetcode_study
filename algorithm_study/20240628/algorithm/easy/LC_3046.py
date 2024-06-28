from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter()
        for num in nums:
            counter[num]+=1
            if counter[num] > 2:
                return False
        return True
