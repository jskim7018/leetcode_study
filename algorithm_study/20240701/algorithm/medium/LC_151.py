class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split() # 아무것도 안넣으면 여러 space로 짤라줌.
        s_split.reverse()
        return " ".join(s_split)
