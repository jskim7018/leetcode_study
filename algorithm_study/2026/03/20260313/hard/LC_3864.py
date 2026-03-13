class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        # recursively. min(left + right, all)
        # using prefix_sum can find count of ones of subarray in O(1)
        # time complexity: O(n*log(n))
        n = len(s)
        prefix_ones_cnt = [0] * n

        for i in range(n):
            if s[i] == '1':
                prefix_ones_cnt[i] += 1
            if i-1 >= 0:
                prefix_ones_cnt[i] += prefix_ones_cnt[i-1]

        def calc_min(l: int, r: int) -> int:
            if l == r:
                if s[l] == '1':
                    return encCost
                else:
                    return flatCost
            length = r-l+1
            ones_cnt = prefix_ones_cnt[r]
            if l > 0:
                ones_cnt -= prefix_ones_cnt[l-1]

            if ones_cnt > 0:
                use_all = ones_cnt * length * encCost
            else:
                use_all = flatCost

            if length % 2 == 0:
                return min(use_all, calc_min(l, l+(length//2-1)) + calc_min(l+length//2, r))
            else:
                return use_all

        return calc_min(0, n-1)
