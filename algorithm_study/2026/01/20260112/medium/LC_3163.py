class Solution:
    def compressedString(self, word: str) -> str:
        word += '.' # sentinel

        cnt = 1
        curr_ch = word[0]
        ans = []
        for ch in word[1:]:
            if ch == curr_ch:
                cnt += 1
            if cnt == 10 or ch != curr_ch:
                if cnt == 10:
                    cnt -= 1
                ans.append(str(cnt) + curr_ch)
                cnt = 1
                curr_ch = ch

        return ''.join(ans)
