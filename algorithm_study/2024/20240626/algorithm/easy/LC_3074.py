from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)

        total_apples = sum(apple)
        ans = 0
        for c in capacity:
            if total_apples <= 0:
                return ans
            ans += 1
            if c >= total_apples:
                break
            else:
                total_apples -= c
        return ans
