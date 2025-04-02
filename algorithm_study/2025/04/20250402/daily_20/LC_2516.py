class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)

        a_cnt_to_idx = dict()
        b_cnt_to_idx = dict()
        c_cnt_to_idx = dict()

        a_cnt = 0
        b_cnt = 0
        c_cnt = 0

        a_cnt_to_idx[0] = n
        b_cnt_to_idx[0] = n
        c_cnt_to_idx[0] = n
        for i in range(n-1,-1,-1):
            if s[i] == 'a':
                a_cnt += 1
                a_cnt_to_idx[a_cnt] = i
            elif s[i] == 'b':
                b_cnt += 1
                b_cnt_to_idx[b_cnt] = i
            else:
                c_cnt += 1
                c_cnt_to_idx[c_cnt] = i
        if a_cnt < k or b_cnt < k or c_cnt <k:
            return -1
        a_cnt = 0
        b_cnt = 0
        c_cnt = 0
        ans = float('inf')
        for i in range(-1, n):
            if s[i] == 'a' and a_cnt < k and i >= 0:
                a_cnt += 1
            elif s[i] == 'b' and b_cnt < k and i >= 0:
                b_cnt += 1
            elif s[i] == 'c' and c_cnt < k and i >= 0:
                c_cnt += 1
            ans = min(ans, n-min(a_cnt_to_idx[k-a_cnt], b_cnt_to_idx[k-b_cnt],c_cnt_to_idx[k-c_cnt])+(i+1))

        return ans
