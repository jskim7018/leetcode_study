import heapq

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        s_arr = [int(s[i]) for i in range(len(s))]

        len_s = len(s)
        isSwapped = False
        i = len_s-1
        heap = []
        heapq.heapify(heap)
        while i > 0:

            heapq.heappush(heap, (-s_arr[i], i))
            idx_to_swap = 0
            while heap and s_arr[i-1] < -heap[0][0]:
                idx_to_swap = heapq.heappop(heap)[1]
                isSwapped = True
            if isSwapped:
                s_arr[i - 1], s_arr[idx_to_swap] = s_arr[idx_to_swap], s_arr[i - 1]
                s_arr[i:] = sorted(s_arr[i:])
                break
            i -= 1
        if not isSwapped:
            return -1
        else:
            ans = 0
            for i in range(len(s_arr)-1 , -1, -1):
                ans += 10**(len(s_arr)-i-1) * s_arr[i]
            if ans > 2**31-1:
                return -1
            else:
                return ans
