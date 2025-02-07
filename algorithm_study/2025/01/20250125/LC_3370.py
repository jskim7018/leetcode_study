class Solution:
    def smallestNumber(self, n: int) -> int:
        bin_n = bin(n)[2:]
        return int(bin_n.replace('0','1'), 2)
