class Solution:
    def decodeString(self, s: str) -> str:
        return self.decodeStringDfs(0, len(s)-1, s)

    def decodeStringDfs(self, s_idx:int, e_idx: int, s:str) -> str:
        ret = ""
        i = s_idx
        while s_idx <= i <= e_idx:
            if s[i].isnumeric():
                cnt = int(s[i:s.find('[', i)])
                cut_idx = s.find('[', i) + 1
                i = s.find('[', i) - 1
                right_bracket = 0
                while True:
                    if s[cut_idx] == '[':
                        right_bracket -= 1
                    elif s[cut_idx] == ']':
                        right_bracket += 1
                    if right_bracket == 1:
                        break
                    cut_idx += 1
                ret += cnt * self.decodeStringDfs(i + 2, cut_idx-1, s)
                i = cut_idx
            else:
                ret += s[i]
            i += 1
        return ret
