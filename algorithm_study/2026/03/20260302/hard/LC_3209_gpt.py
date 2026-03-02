from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prev = {}  # and_value -> count
        ans = 0

        for num in nums:
            curr = defaultdict(int)

            # Start new subarray at this position
            curr[num] += 1

            # Extend previous subarrays
            # prev는 최대 30개밖이 안감. AND는 결국 줄기만 하기에 비트 갯수의 상태만 있음.
            for and_val, cnt in prev.items():
                new_and = and_val & num
                curr[new_and] += cnt

            # Count how many equal k
            ans += curr.get(k, 0)

            prev = curr

        return ans