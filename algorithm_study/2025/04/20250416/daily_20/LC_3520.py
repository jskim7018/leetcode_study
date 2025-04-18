from typing import List
from sortedcontainers import SortedList


class Solution:
    def minThreshold(self, nums: List[int], k: int) -> int:

        l = 0
        r = max(nums)-min(nums)

        ans = -1
        while l <= r:
            mid = (l+r)//2

            sorted_list = SortedList()
            curr_cnt = 0
            for num in nums:
                left_index = sorted_list.bisect_right(num)
                right_index = sorted_list.bisect_left(num+mid+1)

                curr_cnt += right_index-left_index
                sorted_list.add(num)
            # if possible try with lesser threshold
            if curr_cnt >= k:
                r = mid-1
                ans = mid
            # if impossible try with greater threshold
            elif curr_cnt < k:
                l = mid+1
        return ans
