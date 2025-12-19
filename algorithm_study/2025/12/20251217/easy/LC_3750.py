class Solution:
    def minimumFlips(self, n: int) -> int:
        bin_of_n = bin(n)[2:]

        len_n = len(bin_of_n)

        ans = 0
        for i in range(len_n//2):
            if bin_of_n[i] != bin_of_n[-1-i]:
                ans += 2
        return ans
