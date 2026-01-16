class Solution:
    def resultingString(self, s: str) -> str:
        stack = list()

        for ch in s:
            ch_num = ord(ch) - ord('a')
            if stack:
                if (stack[-1] + 1) % 26 == ch_num or \
                        (((stack[-1] - 1) % 26) + 26) % 26 == ch_num:
                    stack.pop()
                else:
                    stack.append(ch_num)
            else:
                stack.append(ch_num)

        return ''.join([chr(ch_num + ord('a')) for ch_num in stack])
