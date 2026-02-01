from math import perm

class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7

        # 모든 경우의 수. 각 pair를 한번만 하는 경우의 수 (n개 pair)로 나눈다.
        # factorial 하면서 짝수면 2를 하나씩 쓰면서 제거.
        total = n*2
        ans = 1
        # TODO: 한번의 루프로도 가능.
        for i in range(1, total+1, 2):
            ans *= i
            ans %= mod
        for i in range(1, n+1):
            ans *= i
            ans %= mod
        return ans
