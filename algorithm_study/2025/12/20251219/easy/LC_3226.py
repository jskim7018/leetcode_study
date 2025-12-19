class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k > n:
            return -1

        bin_n = bin(n)[2:]
        bin_k = bin(k)[2:]

        size_diff = len(bin_n) - len(bin_k)

        ans = 0
        idx_n = 0

        for i in range(size_diff):
            if bin_n[i] == '1':
                ans += 1
            idx_n += 1

        for i in range(len(bin_k)):
            if bin_n[idx_n] == '1' and bin_k[i] == '0':
                ans += 1
            elif bin_n[idx_n] == '0' and bin_k[i] == '1':
                return -1
            idx_n += 1
        return ans
