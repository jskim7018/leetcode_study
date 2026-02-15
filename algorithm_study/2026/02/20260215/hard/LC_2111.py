from typing import List
from collections import defaultdict
import bisect


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # 결국, mod k의 것들을 별도로 배열로 보고 non-decreasing으로 만드는 가장 적은 operation.
        # 가장 긴 non-decreasing을 subsequence 수를 구하고 나머지를 뺌. (LIS 문제 느낌)
        # LIS 구하는 법 -> Monotonic stack, binary search

        def lis(nums: List[int]) -> int:
            incr_stck = []
            idx_to_cnt = defaultdict(int)
            for num in nums:
                idx = bisect.bisect_right(incr_stck, num)

                if idx < len(incr_stck):
                    incr_stck[idx] = num
                else:
                    incr_stck.append(num)
                    idx_to_cnt[len(incr_stck)-1] = len(incr_stck)

            return len(incr_stck)

        lists_by_mod = defaultdict(list)
        for i in range(len(arr)):
            lists_by_mod[i % k].append(arr[i])

        ans = 0
        for lst in lists_by_mod.values():
            lst_len = len(lst)
            ordered_cnt = lis(lst)

            ans += lst_len - ordered_cnt

        return ans
