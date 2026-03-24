class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        prev_prev = ''
        prev = ''
        while a > 0 or b > 0:
            if a >= b and (prev_prev != 'a' or prev != 'a') \
                    or (prev_prev == 'b' and prev == 'b'):
                ans.append('a')
                new_prev = 'a'
                a -= 1
            else:
                ans.append('b')
                new_prev = 'b'
                b -= 1

            prev_prev = prev
            prev = new_prev

        return ''.join(ans)
