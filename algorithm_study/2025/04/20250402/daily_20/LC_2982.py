from collections import defaultdict

# TODO: Study editorial solution
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        curr_char = ''
        char_arr = []

        counter = defaultdict(int)
        for i in range(n):
            if s[i] != curr_char:
                if i != 0:
                    counter[''.join(char_arr)] += 1
                char_arr.clear()
                char_arr.append(s[i])
                curr_char = s[i]
            else:
                char_arr.append(s[i])

        if char_arr:
            counter[''.join(char_arr)] += 1

        alphs_cnt_list = [[] for _ in range(26)]
        for k, v in counter.items():
            alphs_cnt_list[ord(k[0])-ord('a')].append((k,v))

        for lst in alphs_cnt_list:
            lst.sort()

        ans = -1

        for lst in alphs_cnt_list:
            for idx, (string, cnt) in enumerate(lst):
                if cnt >= 3:
                    ans = max(ans, len(string))
                else:
                    if idx != len(lst)-1:
                        ans = max(ans, len(string))
                    elif len(string) >= 3:
                        if cnt > 1:
                            ans = max(ans, len(string)-1)
                        else:
                            ans = max(ans, len(string)-2)

        return ans

