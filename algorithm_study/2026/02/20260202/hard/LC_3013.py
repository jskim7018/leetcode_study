from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # sorted list 사용시 dynamic 하게 가능.
        n = len(nums)

        sorted_list = SortedList()
        curr = nums[0]
        window_size = dist + 1
        for i in range(1, window_size + 1):
            sorted_list.add(nums[i])

        for i in range(k-1):
            curr += sorted_list[i]

        ans = curr
        for i in range(window_size+1, n):
            idx = sorted_list.bisect_right(nums[i-window_size])-1
            is_sub = False
            if idx < (k-1):
                curr -= sorted_list[idx]
                is_sub = True
            sorted_list.remove(nums[i-window_size])

            if len(sorted_list) < k-1 or nums[i] < sorted_list[k-2]:
                curr += nums[i]
                if not is_sub:
                    curr -= sorted_list[k-2]
            else:
                if is_sub:
                    curr += sorted_list[k-2]
            sorted_list.add(nums[i])
            ans = min(ans, curr)

        return ans
