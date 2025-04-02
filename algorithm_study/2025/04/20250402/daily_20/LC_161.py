class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m == n:
            diff_cnt = 0
            for i in range(m):
                if s[i] != t[i]:
                    diff_cnt+=1
            if diff_cnt == 1:
                return True
        elif m+1 == n:
            i = 0
            j = 0
            diff_cnt = 0
            while i < m and j < n:
                if s[i] != t[j]:
                    diff_cnt += 1
                    j+=1
                else:
                    i += 1
                    j += 1
            if diff_cnt <= 1:
                return True

        elif m-1 == n:
            i = 0
            j = 0
            diff_cnt = 0
            while i < m and j < n:
                if s[i] != t[j]:
                    diff_cnt += 1
                    i += 1
                else:
                    i += 1
                    j += 1
            if diff_cnt <= 1:
                return True

        return False
