class Solution:
    def getSmallestString(self, s: str) -> str:
        s_list = list(s)

        for i in range(1, len(s_list)):
            if int(s_list[i-1]) % 2 == int(s_list[i]) % 2 and int(s_list[i-1]) > int(s_list[i]):
                s_list[i-1], s_list[i] = s_list[i], s_list[i-1]
                break
        return ''.join(s_list)
