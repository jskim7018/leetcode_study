from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        ans = [''] * n
        curr = 'a'

        # 가능한것을 일단 만듬.
        for i in range(n):
            if ans[i] == '':
                if not curr.isalpha():
                    return ""
                ans[i] = curr
                curr = chr(ord(curr) + 1)

            for j in range(i+1, n):
                if lcp[i][j] > 0:
                    if ans[j] != "" and ans[j] != ans[i]:
                        return ""
                    ans[j] = ans[i]

        def z_algorithm(s: str) -> list[int]:
            n = len(s)
            Z = [0] * n
            L = R = 0
            Z[0] = n

            for i in range(1, n):
                if i <= R:
                    Z[i] = min(R - i + 1, Z[i - L])

                while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                    Z[i] += 1

                if i + Z[i] - 1 > R:
                    L, R = i, i + Z[i] - 1

            return Z

        ans_str = ''.join(ans)
        # 실제 가능 한지 검증. (불가 케이스 찾기)
        prev_check_arrs = []
        for i in range(n):
            left_part = [0] * i

            # make it symmetric
            for j in range(len(left_part)):
                left_part[j] = prev_check_arrs[j][i]
            check_arr = left_part + z_algorithm(ans_str[i:])
            if lcp[i] != check_arr:
                return ""
            prev_check_arrs.append(check_arr)

        return ans_str
