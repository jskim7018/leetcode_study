import heapq


class Solution:
    def smallestNumber(self, num: int) -> int:
        neg_factor = 1
        if num < 0:
            neg_factor = -1
            num = -num
        heap = []
        zero_cnt = 0
        while num != 0:
            if num % 10 != 0:
                heapq.heappush(heap, neg_factor * (num % 10))
            else:
                zero_cnt += 1
            num //= 10

        ans = 0
        if heap:
            ans += neg_factor*heapq.heappop(heap)
        for i in range(zero_cnt):
            heapq.heappush(heap, 0)
        while heap:
            ans *= 10
            val = neg_factor*heapq.heappop(heap)
            ans += val

        return neg_factor * ans
