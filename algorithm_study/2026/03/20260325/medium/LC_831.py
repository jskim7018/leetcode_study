class Solution:
    def maskPII(self, s: str) -> str:
        # 쉬움.
        # email parse by @ symbol then do masking then rejoin
        # phone, count numbers and keep last 4 digits.
        #        mask according to count of numbers.

        if '@' in s:
            s = s.lower()
            id, domain = s.split(sep='@')

            return id[0] + "*****" + id[-1] + "@" + domain
        else:
            nums_cnt = 0
            last_4_digits = []
            for ch in s[::-1]:
                if ch.isnumeric():
                    nums_cnt += 1
                    if len(last_4_digits) < 4:
                        last_4_digits.append(ch)
            last_4_digits.reverse()
            num = ["***-***-" + ''.join(last_4_digits)]
            if nums_cnt > 10:
                rem = nums_cnt % 10
                country_code = ['+']
                for i in range(rem):
                    country_code.append('*')
                country_code.append('-')
                num = country_code + num

            return ''.join(num)
