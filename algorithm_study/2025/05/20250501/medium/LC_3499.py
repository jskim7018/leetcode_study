class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        curr = '1'
        curr_cnt = 0

        lst = []
        for i in range(0, n):
            if s[i] == curr:
                curr_cnt += 1
            else:
                curr = s[i]
                lst.append(curr_cnt)
                curr_cnt = 1
            if i == n-1:
                lst.append(curr_cnt)

        m = len(lst)
        ans = 0
        for i in range(m):
            if i%2 == 0:
               ans += lst[i]
        maxim_ones = 0
        for i in range(m-2):
            if i%2 == 1:
                curr = lst[i] + lst[i+2]
                maxim_ones = max(maxim_ones, curr)

        ans += maxim_ones

        return ans
