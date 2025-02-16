class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(idx, str_num, curr_num) :
            nonlocal num
            nonlocal st
            if idx >= len(str_num):
                st.add(curr_num)
                return

            for i in range(idx + 1, len(str_num)+1):
                part_num = int(str_num[idx:i])
                partition(i, str_num, curr_num + part_num)

        ans = 0
        for num in range(1,n+1):
            st = set()
            num_sqr = num*num
            partition(0, str(num_sqr), 0)
            if num in st:
                ans += num_sqr
        return ans

