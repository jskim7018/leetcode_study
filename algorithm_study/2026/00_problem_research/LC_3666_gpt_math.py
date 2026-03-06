from math import inf

def ceil(x, y):
    return (x + y - 1) // y


class Solution:
    def minOperations(self, S: str, K: int) -> int:
        N = len(S)
        Z = S.count("0")

        # Special case: flipping entire string
        if N == K:
            if Z == 0:
                return 0
            if Z == N:
                return 1
            return -1

        ans = inf

        # Case 1: final state reached without parity flip sequence
        # Z must be even
        if Z % 2 == 0:
            M = max(ceil(Z, K), ceil(Z, N - K))
            # M must be even
            if M % 2 == 1:
                M += 1
            ans = min(ans, M)

        # Case 2: final state reached with parity alignment
        # Z and K must have same parity
        if Z % 2 == K % 2:
            M = max(ceil(Z, K), ceil(N - Z, N - K))
            # M must be odd
            if M % 2 == 0:
                M += 1
            ans = min(ans, M)

        return ans if ans != inf else -1