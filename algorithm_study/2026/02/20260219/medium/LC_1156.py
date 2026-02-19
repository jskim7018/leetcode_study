from collections import Counter, defaultdict

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # sliding window
        # keep counter with all text count
        # if curr alph cnt is 2 and min is 1 then check if bigger can swap and get max lengt

        alph_cnt = defaultdict(int)
        for ch in text:
            alph_cnt[ch] += 1

        n = len(text)
        l = 0
        curr_alph_cnt = Counter()

        ans = 0
        for r in range(n):
            curr_alph_cnt[text[r]] += 1
            while len(curr_alph_cnt) > 2 or (len(curr_alph_cnt) == 2 and
                                             min(curr_alph_cnt.values()) > 1):
                curr_alph_cnt[text[l]] -= 1
                if curr_alph_cnt[text[l]] == 0:
                    del curr_alph_cnt[text[l]]
                l += 1

            ans_cand = r - l + 1
            most_common_ch, most_common_cnt = curr_alph_cnt.most_common(1)[0]
            if alph_cnt[most_common_ch] == most_common_cnt and len(curr_alph_cnt) > 1:
                ans_cand -= 1

            ans = max(ans, ans_cand)

        return ans
