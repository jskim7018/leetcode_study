class Solution:
    def longestBalanced(self, s: str) -> int:
        # 3가지로 나눔: 1개만 쓸때, 2개만 쓸대, 3개 모두 쓸때.
        # TODO: need to study gemini optimized version thoroughly
        n = len(s)
        ans = 1
        curr_cnt = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr_cnt += 1
            else:
                curr_cnt = 1
            ans = max(ans, curr_cnt)

        def get_longest(use: list[bool]) -> int:
            cnts = [0] * 3

            left_most = dict()

            left_most[(0, 0, 0)] = -1

            ans = 0
            for i, ch in enumerate(s):
                cnt_idx = ord(ch) - ord('a')
                cnts[cnt_idx] += 1
                minim = float('inf')
                for k in range(3):
                    if use[k]:
                        minim = min(minim, cnts[k])
                for k in range(3):
                    if use[k]:
                        cnts[k] -= minim
                cnts_tuple = tuple(cnts)
                if cnts_tuple in left_most:
                    ans = max(ans, i - left_most[cnts_tuple])
                else:
                    left_most[cnts_tuple] = i
            return ans
        ans = max(
            ans, # 1가지
            get_longest([True, True, False]),   # 2가지
            get_longest([True, False, True]),   # 2가지
            get_longest([False, True, True]),  # 2가지
            get_longest([True, True, True])  # 3가지
        )

        return ans