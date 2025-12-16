from typing import List
from sortedcontainers import SortedSet


class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:

        def check_if_palindrome(num: int) -> bool:
            binary = bin(num)[2:]

            for i in range(len(binary) // 2 + 1):
                if binary[i] != binary[-1 - i]:
                    return False

            return True

        maxim = max(nums)

        s = SortedSet()
        for i in range(maxim * 2 + 1):
            if check_if_palindrome(i):
                s.add(i)

        ans = []
        for num in nums:
            idx = s.bisect_left(num)
            upper = s[idx] if idx < len(s) else None

            idx = s.bisect_right(num) - 1
            lower = s[idx] if idx >= 0 else None

            ans_cand = float('inf')
            if lower is not None:
                ans_cand = min(ans_cand, abs(num-lower))
            if upper is not None:
                ans_cand = min(ans_cand, abs(num-upper))

            ans.append(int(ans_cand))

        return ans
