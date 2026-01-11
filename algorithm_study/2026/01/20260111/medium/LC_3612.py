class Solution:
    def processStr(self, s: str) -> str:
        result_list = ''
        for ch in s:
            if ch == '*':
                if result_list:
                    result_list = result_list[:len(result_list)-1]
            elif ch == '#':
                result_list.extend(result_list)
            elif ch == '%':
                result_list = ''.join(reversed(result_list))
            else:
                result_list += ch

        return ''.join(result_list)
