from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # 작은애가 큰 사이에 끼면 어차피 무조건 써야 함.
        # decr_mono_stack 사용.
        ans = 0
        decr_stck = []

        for num in arr:
            while decr_stck and num >= decr_stck[-1]:
                popped = decr_stck.pop()
                if decr_stck and num >= decr_stck[-1]:
                    ans += popped * decr_stck[-1]
                else:
                    ans += popped * num
            decr_stck.append(num)

        n = len(decr_stck)
        for i in range(n-2, -1, -1):
            ans += decr_stck[i] * decr_stck[i+1]

        return ans
