class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)

        prefix_sum = [0] * n

        for i, ch in enumerate(s):
            score = ord(ch) - ord('a') + 1
            prefix_sum[i] += score
            if i - 1 >= 0:
                prefix_sum[i] += prefix_sum[i - 1]

        for i in range(n):
            if prefix_sum[i] == prefix_sum[n - 1] - prefix_sum[i]:
                return True

        return False
