from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)

        ans = []
        curr_k = 0
        chosen = set()

        for num in nums:
            if curr_k >= k:
                break

            if num in chosen:
                continue
            else:
                ans.append(num)
                curr_k += 1
                chosen.add(num)
        return ans
