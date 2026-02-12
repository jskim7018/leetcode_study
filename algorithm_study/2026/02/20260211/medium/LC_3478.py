from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # min heap 사용, 작은 것 부터 시작.
        # 같은 것 처리를 잘하는 것이 관건
        # TODO: fenwick/segment tree 방식도 가능.
        n = len(nums1)

        nums1_with_indexes = defaultdict(list)
        for i in range(n):
            nums1_with_indexes[nums1[i]].append(i)

        nums1_with_indexes = [(k, v) for k, v in nums1_with_indexes.items()]
        nums1_with_indexes.sort()

        min_heap = []

        curr_total_sum = 0
        ans = [0] * n

        for num1, indexes in nums1_with_indexes:
            for idx in indexes:
                ans[idx] = curr_total_sum
            for idx in indexes:
                heapq.heappush(min_heap, nums2[idx])
                curr_total_sum += nums2[idx]
            while len(min_heap) > k:
                curr_total_sum -= heapq.heappop(min_heap)

        return ans
