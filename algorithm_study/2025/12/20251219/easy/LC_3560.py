class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        bigger_log = max(n,m)
        if bigger_log <= k:
            return 0
        else:
            cut_log_size = bigger_log-k
            return cut_log_size * (bigger_log-cut_log_size)
    