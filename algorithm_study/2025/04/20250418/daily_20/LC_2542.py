from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        num_2_1 = [(nums2[i],nums1[i]) for i in range(n)]
        num_2_1.sort(reverse=True)
        min_heap = []
        heapq.heapify(min_heap)

        minim = float('inf')
        curr_sum = 0
        for i in range(k):
            heapq.heappush(min_heap, num_2_1[i][1])
            curr_sum += num_2_1[i][1]
            minim = num_2_1[i][0]

        ans = curr_sum * minim
        for i in range(k,n):
            curr_sum -= heapq.heappop(min_heap)
            curr_sum += num_2_1[i][1]
            minim = num_2_1[i][0]
            heapq.heappush(min_heap,num_2_1[i][1])
            ans = max(ans, minim*curr_sum)

        return ans
