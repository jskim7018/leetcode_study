class Solution:
    def minPartitions(self, n: str) -> int:
        maxim = 0

        for ch in n:
            maxim = max(maxim, int(ch))
            if maxim == 9:
                break

        return maxim
