class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        lst = [set("NE"), set("NW"), set("SE"), set("SW")]
        opposite = {'N':'S', 'S':'N', 'E':'W', 'W':'E'}

        def update(c):
            nonlocal ns_ans
            nonlocal we_ans

            if c == 'N':
                ns_ans += 1
            elif c == 'S':
                ns_ans -= 1
            elif c == 'W':
                we_ans -= 1
            else:
                we_ans += 1

        ans = 0
        for e in lst:
            ans_tmp = 0
            ns_ans = 0
            we_ans = 0
            tmp_k = k
            for c in s:
                if c in e and tmp_k > 0:
                    update(opposite[c])
                    tmp_k -= 1
                else:
                    update(c)
                ans_tmp = max(ans_tmp, abs(ns_ans) + abs(we_ans))

            ans = max(ans, ans_tmp)

        return ans
