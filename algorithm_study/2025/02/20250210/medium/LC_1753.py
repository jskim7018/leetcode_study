import heapq

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a,-b,-c]
        heapq.heapify(heap)

        score = 0
        while True:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first == 0 or second == 0:
                break
            else:
                first += 1
                second += 1
                heapq.heappush(heap, first)
                heapq.heappush(heap, second)
                score += 1
        return score
