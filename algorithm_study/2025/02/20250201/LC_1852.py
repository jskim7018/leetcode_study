from typing import List
from collections import Counter

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        counter = Counter(nums[0:k])

        ans = [len(counter)]
        for i in range(1, n-k+1):
            counter[nums[i+k-1]] += 1
            counter[nums[i-1]] -= 1
            if counter[nums[i-1]] == 0:
                del counter[nums[i-1]]
            ans.append(len(counter))

        return ans
