class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)

        a_num_to_change = ''
        b_num_to_change = ''
        not_change = set()
        for i, ch in enumerate(str_num):
            if not a_num_to_change and ch != '9':
                a_num_to_change = ch
            if not b_num_to_change and ch not in not_change:
                if i == 0 and ch != '1':
                    b_num_to_change = ch
                elif i != 0 and ch != '0':
                    b_num_to_change = ch
                else:
                    not_change.add(ch)

        a = []
        b = []
        for i, digit in enumerate(str_num):
            if digit == a_num_to_change:
                a.append('9')
            else:
                a.append(digit)
            if digit == b_num_to_change and str_num[0] == b_num_to_change:
                b.append('1')
            elif digit == b_num_to_change:
                b.append('0')
            else:
                b.append(digit)

        return int(''.join(a)) - int(''.join(b))
