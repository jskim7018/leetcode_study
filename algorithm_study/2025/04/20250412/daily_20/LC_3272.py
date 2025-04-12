from collections import Counter
from math import perm


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half_size = n//2 + n % 2
        end = pow(10, n//2 + n % 2)-1

        ans = 0
        st = set()
        for num in range(1, end+1):
            # normalize
            num_str = str(num)
            num_str = num_str.zfill(half_size)
            full_num = int(num_str[(n % 2 == 1):][::-1] + num_str)
            str_full_num = str(full_num)

            # conditions to move on
            if full_num % k != 0:
                continue
            if len(str_full_num) != n:
                continue
            sorted_full_num = tuple(sorted(str_full_num))
            if sorted_full_num in st:
                continue
            st.add(sorted_full_num)

            # calculate permutations
            counter = Counter(str_full_num)
            good_int_cnt = perm(len(str_full_num), len(str_full_num))
            for v in counter.values():
                good_int_cnt //= perm(v, v)
            if counter['0'] > 0:
                first_zero_cnt = perm(len(str_full_num) - 1, len(str_full_num) - 1)
                counter['0'] -= 1
                for v in counter.values():
                    first_zero_cnt //= perm(v,v)
                good_int_cnt -= first_zero_cnt

            ans += good_int_cnt

        return ans
