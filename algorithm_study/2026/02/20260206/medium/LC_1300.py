from typing import List
from itertools import accumulate
import bisect


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # binary search to find closest larger than taget.
        # check with val - 1 and check if more closer than val
        # prefix sum으로 O(1)만에 구할 수 있음.
        n = len(arr)

        arr.sort()
        prefix_sum = list(accumulate(arr))
        l = 0
        r = arr[-1]

        def get_sum_with_val(val: int) -> int:
            idx = bisect.bisect_right(arr, val)
            greater_cnt = n - idx
            ret = greater_cnt * val
            if idx - 1 >= 0:
                ret += prefix_sum[idx-1]
            return ret

        min_val = arr[-1]
        diff = abs(target - prefix_sum[-1])

        while l <= r:
            mid = (l+r)//2

            _sum = get_sum_with_val(mid)
            if target <= _sum:
                min_val = mid
                diff = _sum - target
                r = mid - 1
            else:
                l = mid + 1

        if min_val > 0 and abs(target - get_sum_with_val(min_val-1)) <= diff:
            min_val -= 1

        return min_val
