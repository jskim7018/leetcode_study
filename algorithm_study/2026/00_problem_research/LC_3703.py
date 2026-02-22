class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        # 그냥 k이상 balanced를 모두 찾아서 k balanced가 아닐떄까지 없에면 됨.
        left = 0
        right = 0


        def append_paren(l: int, r: int, lst: list):
            for i in range(l):
                lst.append('(')
            for i in range(r):
                lst.append(')')

        while s:
            ans = []

            for ch in s:
                if ch == '(':
                    if right != 0:
                        del_cnt = right // k
                        left -= del_cnt * k
                        right -= del_cnt * k
                        append_paren(left, right, ans)
                        left = 0
                        right = 0
                    left += 1
                else:
                    right += 1
                    if left < k:
                        append_paren(left, right, ans)
                        left = 0
                        right = 0
                    elif right == k:
                        left -= right
                        right = 0

            del_cnt = right // k
            left -= del_cnt * k
            right -= del_cnt * k
            append_paren(left, right, ans)
            left = 0
            right = 0
            nxt_s = ''.join(ans)

            if nxt_s == s:
                break
            s = nxt_s
        return s
