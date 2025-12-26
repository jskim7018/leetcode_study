from typing import List
import heapq


class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        heap_even = []
        heap_odd = []

        for num in nums:
            if num % 2 == 0:
                heap_even.append(-num)
            else:
                heap_odd.append(-num)

        heapq.heapify(heap_even)
        heapq.heapify(heap_odd)
        ans = 0
        while k > 0:
            if (k == 1 and heap_even) or (len(heap_odd) < 2 and heap_even):
                ans += -heapq.heappop(heap_even)
                k -= 1
            elif not heap_even and len(heap_odd) >= 2 and k >= 2:
                ans += -heapq.heappop(heap_odd)
                ans += -heapq.heappop(heap_odd)
                k -= 2
            elif len(heap_odd) >= 2 and len(heap_even) >= 2 and k >= 2:
                odd1 = -heapq.heappop(heap_odd)
                odd2 = -heapq.heappop(heap_odd)
                even1 = -heapq.heappop(heap_even)
                even2 = -heapq.heappop(heap_even)
                if odd1 + odd2 > even1 + even2:
                    ans += odd1 + odd2
                    heapq.heappush(heap_even, -even1)
                    heapq.heappush(heap_even, -even2)
                    k -= 2
                else:
                    ans += even1
                    heapq.heappush(heap_odd, -odd1)
                    heapq.heappush(heap_odd, -odd2)
                    heapq.heappush(heap_even, -even2)
                    k -= 1
            elif len(heap_odd) >= 2 and len(heap_even) == 1 and k >= 2:
                odd1 = -heapq.heappop(heap_odd)
                odd2 = -heapq.heappop(heap_odd)
                even1 = -heapq.heappop(heap_even)
                if odd1 + odd2 > even1 or k == 2:
                    ans += odd1 + odd2
                    heapq.heappush(heap_even, -even1)
                    k -= 2
                else:
                    ans += even1
                    heapq.heappush(heap_odd, -odd1)
                    heapq.heappush(heap_odd, -odd2)
                    k -= 1
            else:
                break
        if k > 0:
            return -1
        else:
            return ans
