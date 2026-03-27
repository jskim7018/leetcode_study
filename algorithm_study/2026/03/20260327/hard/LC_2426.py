from typing import List
from sortedcontainers import SortedList


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # (nums1[i] - nums2[i]) - (nums1[j]  - nums2[j]) <=  diff.
        # -> (nums1[i] - nums2[i]) <= diff +  (nums1[j]  - nums2[j])
        # => nums3 배열 -> nums1[i]-nums2[i]를 만든다.
        # => 이전 num3 값 중에서 이진 탐색으로 현재+diff보다 작거나 같은 갯수를 구한다.
        # 수학적 구조를 파악해서 문제를 단순화 하는 방식.

        n = len(nums1)

        nums3 = [0] * n
        for i in range(n):
            nums3[i] = nums1[i] - nums2[i]

        ans = 0
        sorted_list = SortedList()
        for i in range(n):
            to_find = diff + nums3[i]

            ans += sorted_list.bisect_right(to_find)
            sorted_list.add(nums3[i])

        return ans
