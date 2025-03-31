from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix_xor = [0] * n
        prefix_xor[0] = arr[0]
        for i in range(1,n):
            prefix_xor[i] = arr[i] ^ prefix_xor[i-1]

        ans = []
        for q in queries:
            left = q[0]
            right = q[1]

            result = prefix_xor[right]
            if left-1 >=0:
                result ^= prefix_xor[left-1]
            ans.append(result)
        return ans
