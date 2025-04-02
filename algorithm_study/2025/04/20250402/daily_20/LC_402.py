import heapq


# TODO: Study editorial (Using stack)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        heap = []
        heapq.heapify(heap)
        ans = []

        for i in range(-k, n):
            while heap and heap[0][1] <= i:
                heapq.heappop(heap)

            if i+k < n:
                heapq.heappush(heap, (int(num[i+k]),i+k))

            if i < 0:
                continue

            if heap:
                if heap[0][0] >= int(num[i]):
                    ans.append(num[i])
                else:
                    k -= 1
            else:
                ans.append(num[i])

        for i in range(k):
            ans.pop()

        ans = ''.join(ans)

        ans = ans.lstrip('0')
        if len(ans) == 0:
            ans = '0'
        return ans
