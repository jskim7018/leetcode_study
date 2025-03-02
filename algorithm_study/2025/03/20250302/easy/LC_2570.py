from typing import List
from collections import Counter

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        counter = Counter()

        for k, v in nums1:
            counter[k] += v
        for k,v in nums2:
            counter[k] += v

        ans = list(counter.items())
        ans.sort()

        return ans
